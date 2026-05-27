"""
Modelagem revisada para previsao de demanda e dimensionamento de estoque.

Este script foi escrito para responder aos pontos metodologicos levantados na
revisao da tese:
- explicitar a base usada e a agregacao temporal;
- separar treino, validacao temporal e teste final;
- declarar horizonte de previsao;
- comparar modelos simples e interpretaveis antes de modelos complexos;
- ligar previsao de demanda ao dimensionamento de estoque por nivel de servico;
- evitar chamar calibracao simples de "otimizacao".

Entrada:
    data/base de dados resumida140526 .xlsx

Saidas:
    outputs/dados_mensais_limpos.csv
    outputs/metricas_validacao_interna.csv
    outputs/metricas_teste_final.csv
    outputs/previsoes_teste_final.csv
    outputs/dimensionamento_estoque.csv
    outputs/resumo_metodologico.txt
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Callable

import numpy as np
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
BASE_PATH = PROJECT_ROOT / "data" / "base de dados resumida140526 .xlsx"
OUTPUT_DIR = PROJECT_ROOT / "outputs"

# Parametros metodologicos explicitos.
SHEET_NAME = "BD RESUMIDA"
FREQ = "MS"  # serie mensal, inicio do mes
TEST_MONTHS = 12  # teste final: ultimos 12 meses
HORIZON_MONTHS = 1  # avaliacao um passo a frente
MIN_TRAIN_MONTHS = 36  # minimo para validacao rolante
SERVICE_LEVEL = 0.95
DEFAULT_LEAD_TIME_MONTHS = 1.0


Z_BY_SERVICE_LEVEL = {
    0.90: 1.28,
    0.95: 1.65,
    0.975: 1.96,
    0.99: 2.33,
}


@dataclass(frozen=True)
class ForecastResult:
    model: str
    forecast: pd.Series


def read_base(path: Path) -> pd.DataFrame:
    """Read the thesis workbook and normalize columns to stable ASCII names."""
    raw = pd.read_excel(path, sheet_name=SHEET_NAME, header=None)
    df = raw.iloc[2:, 1:].copy()
    df.columns = [
        "ano",
        "mes",
        "semana",
        "dia_semana",
        "dia_semana_extenso",
        "data",
        "dia_mes",
        "vol_f1",
        "vol_f2",
        "vol_f3",
        "vol_f4",
        "vol_f5",
        "vol_total",
        "est_f1",
        "est_f2",
        "est_f3",
        "est_f4",
        "est_f5",
    ]

    for col in df.columns:
        if col not in {"dia_semana_extenso", "data"}:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    df["data"] = pd.to_datetime(df["data"], errors="coerce")

    if df["data"].isna().any():
        raise ValueError("A coluna de data contem valores invalidos.")
    if df["data"].duplicated().any():
        raise ValueError("A base contem datas duplicadas; revisar antes de modelar.")

    return df


def monthly_series(df_daily: pd.DataFrame) -> pd.DataFrame:
    """Aggregate daily volume and stock by month."""
    volume_cols = ["vol_f1", "vol_f2", "vol_f3", "vol_f4", "vol_f5"]
    stock_cols = ["est_f1", "est_f2", "est_f3", "est_f4", "est_f5"]

    monthly = (
        df_daily.set_index("data")
        .resample(FREQ)
        .agg(
            {
                "vol_total": "sum",
                **{col: "sum" for col in volume_cols},
                **{col: "mean" for col in stock_cols},
            }
        )
    )
    monthly["estoque_total_medio"] = monthly[stock_cols].sum(axis=1)

    # Isto e cobertura observada, nao lead time operacional.
    monthly["cobertura_observada_meses"] = (
        monthly["estoque_total_medio"] / monthly["vol_total"].replace(0, np.nan)
    )
    return monthly


def mae(y_true: pd.Series, y_pred: pd.Series) -> float:
    return float(np.mean(np.abs(y_true - y_pred)))


def rmse(y_true: pd.Series, y_pred: pd.Series) -> float:
    return float(np.sqrt(np.mean((y_true - y_pred) ** 2)))


def wmape(y_true: pd.Series, y_pred: pd.Series) -> float:
    denom = float(np.sum(np.abs(y_true)))
    if denom == 0:
        return np.nan
    return float(np.sum(np.abs(y_true - y_pred)) / denom)


def bias_pct(y_true: pd.Series, y_pred: pd.Series) -> float:
    denom = float(np.sum(y_true))
    if denom == 0:
        return np.nan
    return float(np.sum(y_pred - y_true) / denom)


def metric_row(model: str, y_true: pd.Series, y_pred: pd.Series) -> dict[str, float | str]:
    aligned = pd.concat([y_true.rename("real"), y_pred.rename("previsto")], axis=1).dropna()
    return {
        "modelo": model,
        "n_obs": len(aligned),
        "MAE": mae(aligned["real"], aligned["previsto"]),
        "RMSE": rmse(aligned["real"], aligned["previsto"]),
        "WMAPE": wmape(aligned["real"], aligned["previsto"]),
        "BIAS_PCT": bias_pct(aligned["real"], aligned["previsto"]),
    }


def forecast_naive(train: pd.Series, periods: int, index: pd.DatetimeIndex) -> ForecastResult:
    return ForecastResult("naive_ultimo_mes", pd.Series(train.iloc[-1], index=index))


def forecast_seasonal_naive(train: pd.Series, periods: int, index: pd.DatetimeIndex) -> ForecastResult:
    values = []
    history = list(train.astype(float))
    for i in range(periods):
        if len(history) >= 12:
            values.append(history[-12])
        else:
            values.append(history[-1])
        history.append(values[-1])
    return ForecastResult("naive_sazonal_12m", pd.Series(values, index=index))


def forecast_moving_average(train: pd.Series, periods: int, index: pd.DatetimeIndex, window: int = 3) -> ForecastResult:
    value = float(train.tail(window).mean())
    return ForecastResult(f"media_movel_{window}m", pd.Series(value, index=index))


def forecast_drift(train: pd.Series, periods: int, index: pd.DatetimeIndex) -> ForecastResult:
    slope = (float(train.iloc[-1]) - float(train.iloc[0])) / max(len(train) - 1, 1)
    values = [max(float(train.iloc[-1]) + slope * step, 0.0) for step in range(1, periods + 1)]
    return ForecastResult("drift_linear", pd.Series(values, index=index))


def _ses_fit(train: pd.Series, alpha: float) -> tuple[float, float]:
    level = float(train.iloc[0])
    sse = 0.0
    for obs in train.iloc[1:].astype(float):
        pred = level
        sse += (obs - pred) ** 2
        level = alpha * obs + (1 - alpha) * level
    return level, sse


def forecast_ses(train: pd.Series, periods: int, index: pd.DatetimeIndex) -> ForecastResult:
    alphas = np.arange(0.05, 1.00, 0.05)
    best_alpha = min(alphas, key=lambda a: _ses_fit(train, float(a))[1])
    level, _ = _ses_fit(train, float(best_alpha))
    return ForecastResult("suav_exp_simples", pd.Series(level, index=index))


def _holt_fit(train: pd.Series, alpha: float, beta: float) -> tuple[float, float, float]:
    values = train.astype(float).to_numpy()
    level = values[0]
    trend = values[1] - values[0] if len(values) > 1 else 0.0
    sse = 0.0
    for obs in values[1:]:
        pred = level + trend
        sse += (obs - pred) ** 2
        old_level = level
        level = alpha * obs + (1 - alpha) * (level + trend)
        trend = beta * (level - old_level) + (1 - beta) * trend
    return level, trend, sse


def forecast_holt(train: pd.Series, periods: int, index: pd.DatetimeIndex) -> ForecastResult:
    grid = np.arange(0.05, 1.00, 0.10)
    best = None
    for alpha in grid:
        for beta in grid:
            level, trend, sse = _holt_fit(train, float(alpha), float(beta))
            if best is None or sse < best[2]:
                best = (float(alpha), float(beta), sse, level, trend)
    assert best is not None
    _, _, _, level, trend = best
    values = [max(level + step * trend, 0.0) for step in range(1, periods + 1)]
    return ForecastResult("holt_tendencia", pd.Series(values, index=index))


FORECASTERS: list[Callable[[pd.Series, int, pd.DatetimeIndex], ForecastResult]] = [
    forecast_naive,
    forecast_seasonal_naive,
    forecast_moving_average,
    forecast_drift,
    forecast_ses,
    forecast_holt,
]


def rolling_validation(series: pd.Series) -> tuple[pd.DataFrame, pd.DataFrame]:
    forecasts = []
    for origin in range(MIN_TRAIN_MONTHS, len(series) - TEST_MONTHS - HORIZON_MONTHS + 1):
        train = series.iloc[:origin]
        target_index = series.index[origin + HORIZON_MONTHS - 1 : origin + HORIZON_MONTHS]
        y_real = float(series.loc[target_index[0]])
        for forecaster in FORECASTERS:
            result = forecaster(train, HORIZON_MONTHS, target_index)
            forecasts.append(
                {
                    "data": target_index[0],
                    "modelo": result.model,
                    "real": y_real,
                    "previsto": float(result.forecast.iloc[-1]),
                    "horizonte_meses": HORIZON_MONTHS,
                }
            )
    validation = pd.DataFrame(forecasts)
    metrics = (
        validation.groupby("modelo", group_keys=False)
        .apply(lambda g: pd.Series(metric_row(g.name, g["real"], g["previsto"])), include_groups=False)
        .reset_index(drop=True)
        .sort_values(["WMAPE", "RMSE"])
    )
    return validation, metrics


def final_holdout(series: pd.Series) -> tuple[pd.DataFrame, pd.DataFrame]:
    train = series.iloc[:-TEST_MONTHS]
    test = series.iloc[-TEST_MONTHS:]
    rows = []
    for forecaster in FORECASTERS:
        result = forecaster(train, TEST_MONTHS, test.index)
        for date, real, pred in zip(test.index, test, result.forecast):
            rows.append({"data": date, "modelo": result.model, "real": float(real), "previsto": float(pred)})
    forecasts = pd.DataFrame(rows)
    metrics = (
        forecasts.groupby("modelo", group_keys=False)
        .apply(lambda g: pd.Series(metric_row(g.name, g["real"], g["previsto"])), include_groups=False)
        .reset_index(drop=True)
        .sort_values(["WMAPE", "RMSE"])
    )
    return forecasts, metrics


def stock_dimensioning(
    monthly: pd.DataFrame,
    validation: pd.DataFrame,
    final_forecasts: pd.DataFrame,
    selected_model: str,
) -> pd.DataFrame:
    z = Z_BY_SERVICE_LEVEL[SERVICE_LEVEL]
    residuals = validation.loc[validation["modelo"] == selected_model].copy()
    sigma_error = float((residuals["real"] - residuals["previsto"]).std(ddof=1))

    selected = final_forecasts.loc[final_forecasts["modelo"] == selected_model].copy()
    selected["nivel_servico"] = SERVICE_LEVEL
    selected["z"] = z
    selected["lead_time_meses_assumido"] = DEFAULT_LEAD_TIME_MONTHS
    selected["desvio_erro_validacao"] = sigma_error
    selected["demanda_no_lead_time"] = selected["previsto"] * DEFAULT_LEAD_TIME_MONTHS
    selected["estoque_seguranca"] = z * sigma_error * np.sqrt(DEFAULT_LEAD_TIME_MONTHS)
    selected["estoque_necessario"] = selected["demanda_no_lead_time"] + selected["estoque_seguranca"]
    selected = selected.merge(
        monthly[["estoque_total_medio", "cobertura_observada_meses"]].reset_index().rename(columns={"data": "data"}),
        on="data",
        how="left",
    )
    selected["saldo_vs_estoque_medio"] = selected["estoque_total_medio"] - selected["estoque_necessario"]
    return selected


def write_summary(
    df_daily: pd.DataFrame,
    monthly: pd.DataFrame,
    validation_metrics: pd.DataFrame,
    test_metrics: pd.DataFrame,
    selected_model: str,
) -> str:
    date_min = df_daily["data"].min().date()
    date_max = df_daily["data"].max().date()
    zero_days = int((df_daily["vol_total"] == 0).sum())
    text = f"""Resumo metodologico da modelagem revisada

Base:
- Periodo diario: {date_min} a {date_max}
- Observacoes diarias: {len(df_daily)}
- Dias com demanda zero: {zero_days}
- Agregacao usada na modelagem principal: mensal
- Observacoes mensais: {len(monthly)}

Desenho experimental:
- Teste final: ultimos {TEST_MONTHS} meses
- Validacao interna: janela expansiva com minimo de {MIN_TRAIN_MONTHS} meses
- Horizonte avaliado: {HORIZON_MONTHS} mes(es) a frente
- Variavel alvo: volume expedido total em toneladas
- Variaveis exogenas: nao usadas nesta versao, pois nao ha justificativa estatistica suficiente no script original.

Modelos comparados:
- naive ultimo mes
- naive sazonal de 12 meses
- media movel de 3 meses
- drift linear
- suavizacao exponencial simples
- Holt com tendencia

Modelo selecionado por menor WMAPE na validacao interna:
- {selected_model}

Melhores metricas de validacao interna:
{validation_metrics.head(6).to_string(index=False)}

Metricas no teste final:
{test_metrics.to_string(index=False)}

Dimensionamento de estoque:
- O calculo usa previsao de demanda + estoque de seguranca por nivel de servico.
- Nivel de servico assumido: {SERVICE_LEVEL:.1%}
- Lead time assumido: {DEFAULT_LEAD_TIME_MONTHS:.2f} mes(es)
- A coluna cobertura_observada_meses e uma cobertura estoque/demanda, nao um lead time operacional.
- O termo recomendado no texto e "dimensionamento" ou "calibracao de parametro", nao "otimizacao", salvo se uma funcao objetivo e restricoes forem formalmente propostas.
"""
    return text


def main() -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)

    df_daily = read_base(BASE_PATH)
    monthly = monthly_series(df_daily)
    series = monthly["vol_total"].astype(float)

    validation, validation_metrics = rolling_validation(series)
    final_forecasts, test_metrics = final_holdout(series)

    selected_model = str(validation_metrics.iloc[0]["modelo"])
    stock = stock_dimensioning(monthly, validation, final_forecasts, selected_model)

    monthly.to_csv(OUTPUT_DIR / "dados_mensais_limpos.csv", index_label="data", encoding="utf-8-sig")
    validation.to_csv(OUTPUT_DIR / "previsoes_validacao_interna.csv", index=False, encoding="utf-8-sig")
    validation_metrics.to_csv(OUTPUT_DIR / "metricas_validacao_interna.csv", index=False, encoding="utf-8-sig")
    final_forecasts.to_csv(OUTPUT_DIR / "previsoes_teste_final.csv", index=False, encoding="utf-8-sig")
    test_metrics.to_csv(OUTPUT_DIR / "metricas_teste_final.csv", index=False, encoding="utf-8-sig")
    stock.to_csv(OUTPUT_DIR / "dimensionamento_estoque.csv", index=False, encoding="utf-8-sig")

    summary = write_summary(df_daily, monthly, validation_metrics, test_metrics, selected_model)
    (OUTPUT_DIR / "resumo_metodologico.txt").write_text(summary, encoding="utf-8")

    print(summary)
    print(f"Arquivos gerados em: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
