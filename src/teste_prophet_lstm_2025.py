"""
Teste exploratorio com Prophet e LSTM para o ano de 2025.

Este script nao altera src/modelagem_revisada_reinaldo.py nem os arquivos
oficiais em outputs/. Ele cria uma pasta separada para registrar uma comparacao
exploratoria entre Prophet/LSTM e o melhor modelo simples ja observado.

Se Prophet ou TensorFlow/Keras nao estiverem instalados, o script nao quebra:
ele registra a ausencia da biblioteca no terminal, no CSV de metricas e no
resumo em texto.
"""

from __future__ import annotations

import importlib.util
import os
import platform
import random
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from modelagem_revisada_reinaldo import (
    BASE_PATH,
    HORIZON_MONTHS,
    OUTPUT_DIR,
    metric_row,
    monthly_series,
    read_base,
)


OUTPUT_TEST_DIR = OUTPUT_DIR / "teste_prophet_lstm_2025"
TRAIN_START = pd.Timestamp("2021-01-01")
TRAIN_END = pd.Timestamp("2024-12-01")
TEST_START = pd.Timestamp("2025-01-01")
TEST_END = pd.Timestamp("2025-12-01")
SIMPLE_BENCHMARK_MODEL = "media_movel_3m"
SIMPLE_BENCHMARK_WMAPE = 0.2061
LSTM_LOOKBACK_MONTHS = 12
RANDOM_SEED = 42

# Estas variaveis precisam ser definidas antes da importacao do TensorFlow.
# Elas ajudam a reduzir variacoes entre execucoes, especialmente quando ha GPU.
os.environ.setdefault("PYTHONHASHSEED", str(RANDOM_SEED))
os.environ.setdefault("TF_DETERMINISTIC_OPS", "1")
os.environ.setdefault("TF_CUDNN_DETERMINISTIC", "1")
os.environ.setdefault("TF_ENABLE_ONEDNN_OPTS", "0")


def set_global_seeds() -> None:
    """Fixa as sementes usadas por Python e NumPy."""
    random.seed(RANDOM_SEED)
    np.random.seed(RANDOM_SEED)


def has_module(name: str) -> bool:
    """Verifica se uma biblioteca existe sem importar o pacote inteiro."""
    return importlib.util.find_spec(name) is not None


def select_train_and_test(series: pd.Series) -> tuple[pd.Series, pd.Series]:
    """Separa treino em 2021-2024 e teste em 2025."""
    train = series.loc[TRAIN_START:TRAIN_END].astype(float)
    test = series.loc[TEST_START:TEST_END].astype(float)

    if len(train) != 48:
        raise ValueError(f"O treino deveria ter 48 meses entre 2021 e 2024, mas tem {len(train)}.")
    if len(test) != 12:
        raise ValueError(f"O teste deveria ter 12 meses em 2025, mas tem {len(test)}.")

    return train, test


def build_forecast_rows(model: str, test: pd.Series, forecast: pd.Series) -> list[dict[str, Any]]:
    """Padroniza as previsoes para salvar em CSV."""
    rows: list[dict[str, Any]] = []
    for date, real_value, predicted_value in zip(test.index, test, forecast):
        rows.append(
            {
                "data": date,
                "modelo": model,
                "real": float(real_value),
                "previsto": float(predicted_value),
                "horizonte_meses": HORIZON_MONTHS,
                "treino_inicio": TRAIN_START,
                "treino_fim": TRAIN_END,
                "n_meses_treino": 48,
            }
        )
    return rows


def run_prophet(train: pd.Series, test: pd.Series) -> tuple[pd.DataFrame, str]:
    """
    Roda Prophet se a biblioteca estiver disponivel.

    O Prophet trabalha com colunas chamadas ds (data) e y (valor). Depois do
    treino em 2021-2024, ele projeta os 12 meses de 2025 em frequencia mensal.
    """
    prophet_class = None
    if has_module("prophet"):
        from prophet import Prophet

        prophet_class = Prophet
    elif has_module("fbprophet"):
        from fbprophet import Prophet

        prophet_class = Prophet
    else:
        message = "Prophet nao executado: biblioteca 'prophet' ou 'fbprophet' nao instalada."
        return pd.DataFrame(), message

    train_df = train.reset_index()
    train_df.columns = ["ds", "y"]

    try:
        model = prophet_class(
            yearly_seasonality=True,
            weekly_seasonality=False,
            daily_seasonality=False,
            seasonality_mode="additive",
        )
        model.fit(train_df)
        future = pd.DataFrame({"ds": test.index})
        predicted = model.predict(future)
        forecast = pd.Series(predicted["yhat"].to_numpy(dtype=float), index=test.index).clip(lower=0)
    except Exception as exc:
        message = f"Prophet nao executado: erro durante ajuste/previsao ({exc})."
        return pd.DataFrame(), message

    return pd.DataFrame(build_forecast_rows("prophet", test, forecast)), "Prophet executado com sucesso."


def minmax_scale(values: np.ndarray) -> tuple[np.ndarray, float, float]:
    """Escala valores para 0-1 sem depender de scikit-learn."""
    v_min = float(np.min(values))
    v_max = float(np.max(values))
    span = v_max - v_min
    if span == 0:
        return np.zeros_like(values, dtype=float), v_min, v_max
    return (values - v_min) / span, v_min, v_max


def inverse_minmax(values: np.ndarray, v_min: float, v_max: float) -> np.ndarray:
    """Volta da escala 0-1 para toneladas."""
    return values * (v_max - v_min) + v_min


def make_lstm_windows(values: np.ndarray, lookback: int) -> tuple[np.ndarray, np.ndarray]:
    """Cria janelas de treino: ultimos 12 meses para prever o mes seguinte."""
    x_values = []
    y_values = []
    for idx in range(lookback, len(values)):
        x_values.append(values[idx - lookback : idx])
        y_values.append(values[idx])
    x = np.array(x_values, dtype=float).reshape(-1, lookback, 1)
    y = np.array(y_values, dtype=float)
    return x, y


def run_lstm(train: pd.Series, test: pd.Series) -> tuple[pd.DataFrame, str]:
    """
    Roda uma LSTM simples se TensorFlow/Keras estiver disponivel.

    Como ha apenas 48 meses de treino, este resultado deve ser lido como
    exploratorio. A previsao dos 12 meses de 2025 e recursiva: o modelo preve o
    proximo mes e esse valor entra na janela para prever o mes seguinte.
    """
    if not has_module("tensorflow"):
        return pd.DataFrame(), "LSTM nao executado: biblioteca 'tensorflow' nao instalada."

    try:
        import tensorflow as tf
        from tensorflow.keras.layers import LSTM, Dense
        from tensorflow.keras.models import Sequential
    except Exception as exc:
        return pd.DataFrame(), f"LSTM nao executado: erro ao importar TensorFlow/Keras ({exc})."

    deterministic_notes = []
    set_global_seeds()
    try:
        tf.keras.utils.set_random_seed(RANDOM_SEED)
        deterministic_notes.append("sementes random/numpy/tensorflow fixadas")
    except Exception:
        tf.random.set_seed(RANDOM_SEED)
        deterministic_notes.append("sementes random/numpy/tensorflow fixadas parcialmente")

    deterministic_notes.append("TF_ENABLE_ONEDNN_OPTS=0")

    try:
        tf.config.experimental.enable_op_determinism()
        deterministic_notes.append("operacoes deterministicas do TensorFlow ativadas")
    except Exception:
        deterministic_notes.append("operacoes deterministicas do TensorFlow nao disponiveis neste ambiente")

    try:
        tf.config.threading.set_inter_op_parallelism_threads(1)
        tf.config.threading.set_intra_op_parallelism_threads(1)
        deterministic_notes.append("threads do TensorFlow limitadas a 1")
    except Exception:
        deterministic_notes.append("limite de threads do TensorFlow nao aplicado")

    train_values = train.to_numpy(dtype=float)
    scaled_train, v_min, v_max = minmax_scale(train_values)
    x_train, y_train = make_lstm_windows(scaled_train, LSTM_LOOKBACK_MONTHS)

    if len(x_train) == 0:
        return pd.DataFrame(), "LSTM nao executado: historico insuficiente para formar janelas de treino."

    try:
        tf.keras.backend.clear_session()
        tf.keras.utils.set_random_seed(RANDOM_SEED)
        model = Sequential(
            [
                LSTM(16, input_shape=(LSTM_LOOKBACK_MONTHS, 1)),
                Dense(1),
            ]
        )
        model.compile(optimizer="adam", loss="mse")
        model.fit(x_train, y_train, epochs=120, batch_size=8, verbose=0, shuffle=False)

        history = list(scaled_train)
        scaled_predictions = []
        for _ in range(len(test)):
            x_input = np.array(history[-LSTM_LOOKBACK_MONTHS:], dtype=float).reshape(1, LSTM_LOOKBACK_MONTHS, 1)
            next_scaled = float(model.predict(x_input, verbose=0)[0, 0])
            next_scaled = float(np.clip(next_scaled, 0.0, 1.5))
            scaled_predictions.append(next_scaled)
            history.append(next_scaled)

        forecast_values = inverse_minmax(np.array(scaled_predictions), v_min, v_max)
        forecast = pd.Series(forecast_values, index=test.index).clip(lower=0)
    except Exception as exc:
        return pd.DataFrame(), f"LSTM nao executado: erro durante ajuste/previsao ({exc})."

    python_version = platform.python_version()
    tensorflow_version = getattr(tf, "__version__", "versao nao identificada")
    status = (
        "LSTM executado com sucesso. "
        f"Ambiente: Python {python_version}, TensorFlow {tensorflow_version}. "
        f"Reprodutibilidade: seed={RANDOM_SEED}; {'; '.join(deterministic_notes)}."
    )
    return pd.DataFrame(build_forecast_rows("lstm_simples", test, forecast)), status


def metrics_for_model(forecasts: pd.DataFrame, model_name: str, status: str) -> dict[str, Any]:
    """Calcula metricas quando ha previsoes; caso contrario registra NaN."""
    if forecasts.empty:
        return {
            "modelo": model_name,
            "n_obs": 0,
            "MAE": np.nan,
            "RMSE": np.nan,
            "WMAPE": np.nan,
            "BIAS_PCT": np.nan,
            "status": status,
            "superou_media_movel_3m": False,
        }

    row = metric_row(model_name, forecasts["real"], forecasts["previsto"])
    wmape_value = float(row["WMAPE"])
    row["status"] = status
    row["superou_media_movel_3m"] = wmape_value < SIMPLE_BENCHMARK_WMAPE
    return row


def build_summary(
    train: pd.Series,
    test: pd.Series,
    metrics: pd.DataFrame,
    statuses: list[str],
) -> str:
    """Monta o resumo do teste exploratorio."""
    executed = metrics.loc[metrics["n_obs"] > 0].copy()
    if executed.empty:
        comparison_lines = [
            "- Nenhum dos modelos exploratorios foi executado, pois as bibliotecas necessarias nao estao instaladas."
        ]
    else:
        comparison_lines = []
        for _, row in metrics.sort_values(["WMAPE", "RMSE"], na_position="last").iterrows():
            model_name = str(row["modelo"])
            if int(row["n_obs"]) == 0 or pd.isna(row["WMAPE"]):
                comparison_lines.append(
                    f"- {model_name}: nao avaliado contra o benchmark, pois nao houve previsoes calculadas."
                )
                continue

            wmape_value = float(row["WMAPE"])
            if wmape_value < SIMPLE_BENCHMARK_WMAPE:
                result = "superou"
            else:
                result = "nao superou"
            comparison_lines.append(
                f"- {model_name}: WMAPE {wmape_value:.2%}; {result} "
                f"o benchmark {SIMPLE_BENCHMARK_MODEL} ({SIMPLE_BENCHMARK_WMAPE:.2%})."
            )

    return f"""Teste exploratorio Prophet/LSTM - 2025

Objetivo:
- Comparar Prophet e LSTM, apenas de forma exploratoria, com o melhor modelo simples ja testado.

Desenho temporal:
- Treino: {train.index.min().date()} a {train.index.max().date()}
- Teste: {test.index.min().date()} a {test.index.max().date()}
- Frequencia: mensal
- Variavel alvo: volume expedido total em toneladas
- Horizonte: {HORIZON_MONTHS} mes(es) a frente

Benchmark simples:
- Modelo: {SIMPLE_BENCHMARK_MODEL}
- WMAPE: {SIMPLE_BENCHMARK_WMAPE:.2%}

Controle de reprodutibilidade do LSTM:
- Semente fixa usada: {RANDOM_SEED}
- O script fixa random, numpy e tensorflow quando TensorFlow esta instalado.
- O script tenta ativar operacoes deterministicas do TensorFlow, define TF_ENABLE_ONEDNN_OPTS=0 e desativa embaralhamento no treino da LSTM.

Status de execucao:
{chr(10).join(f"- {status}" for status in statuses)}

Metricas calculadas:
{metrics.to_string(index=False)}

Comparacao com o benchmark:
{chr(10).join(comparison_lines)}

Observacao metodologica:
- Estes testes nao substituem a modelagem principal. Prophet e LSTM permanecem como comparacao exploratoria, especialmente porque a serie mensal tem apenas 48 meses de treino neste recorte.
"""


def main() -> None:
    set_global_seeds()
    OUTPUT_TEST_DIR.mkdir(parents=True, exist_ok=True)

    df_daily = read_base(BASE_PATH)
    monthly = monthly_series(df_daily)
    series = monthly["vol_total"].astype(float)
    train, test = select_train_and_test(series)

    prophet_forecasts, prophet_status = run_prophet(train, test)
    lstm_forecasts, lstm_status = run_lstm(train, test)

    forecast_frames = [df for df in [prophet_forecasts, lstm_forecasts] if not df.empty]
    if forecast_frames:
        forecasts = pd.concat(forecast_frames, ignore_index=True)
    else:
        forecasts = pd.DataFrame(
            columns=[
                "data",
                "modelo",
                "real",
                "previsto",
                "horizonte_meses",
                "treino_inicio",
                "treino_fim",
                "n_meses_treino",
            ]
        )

    metrics = pd.DataFrame(
        [
            metrics_for_model(prophet_forecasts, "prophet", prophet_status),
            metrics_for_model(lstm_forecasts, "lstm_simples", lstm_status),
        ]
    ).sort_values(["WMAPE", "RMSE"], na_position="last")

    statuses = [prophet_status, lstm_status]
    summary = build_summary(train, test, metrics, statuses)

    forecasts.to_csv(OUTPUT_TEST_DIR / "previsoes_prophet_lstm_2025.csv", index=False, encoding="utf-8-sig")
    metrics.to_csv(OUTPUT_TEST_DIR / "metricas_prophet_lstm_2025.csv", index=False, encoding="utf-8-sig")
    (OUTPUT_TEST_DIR / "resumo_prophet_lstm_2025.txt").write_text(summary, encoding="utf-8")

    print(summary)
    print(f"Arquivos gerados em: {OUTPUT_TEST_DIR}")


if __name__ == "__main__":
    main()
