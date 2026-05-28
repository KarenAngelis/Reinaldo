"""
Teste complementar com 2025 reservado como teste final.

Este script nao altera a modelagem oficial em src/modelagem_revisada_reinaldo.py.
Ele apenas reaproveita as funcoes ja existentes para responder a uma pergunta
especifica: usando o historico de 2021 a 2024 como ponto de partida, os modelos
conseguem acompanhar os 12 meses observados de 2025?

Saidas geradas:
    outputs/teste_2025/previsoes_2025_teste_final.csv
    outputs/teste_2025/metricas_2025_teste_final.csv
    outputs/teste_2025/resumo_teste_2025.txt
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from modelagem_revisada_reinaldo import (
    BASE_PATH,
    FORECASTERS,
    HORIZON_MONTHS,
    OUTPUT_DIR,
    metric_row,
    monthly_series,
    read_base,
)


TEST_2025_DIR = OUTPUT_DIR / "teste_2025"
TRAIN_START = pd.Timestamp("2021-01-01")
TRAIN_END = pd.Timestamp("2024-12-01")
TEST_START = pd.Timestamp("2025-01-01")
TEST_END = pd.Timestamp("2025-12-01")


def select_train_and_test(series: pd.Series) -> tuple[pd.Series, pd.Series]:
    """Separa a serie mensal no recorte pedido: treino 2021-2024 e teste 2025."""
    train = series.loc[TRAIN_START:TRAIN_END].astype(float)
    test = series.loc[TEST_START:TEST_END].astype(float)

    # Essas validacoes deixam claro quando a base nao tem exatamente o recorte
    # esperado. Assim a pessoa nao interpreta um resultado incompleto como final.
    if train.empty:
        raise ValueError("Nao foram encontrados meses de treino entre jan/2021 e dez/2024.")
    if test.empty:
        raise ValueError("Nao foram encontrados meses de teste entre jan/2025 e dez/2025.")
    if len(test) != 12:
        raise ValueError(f"O teste de 2025 deveria ter 12 meses, mas foram encontrados {len(test)}.")

    return train, test


def forecast_2025_from_previous_years(train: pd.Series, test: pd.Series) -> pd.DataFrame:
    """
    Gera previsoes para os 12 meses de 2025 usando apenas 2021-2024.

    A separacao fica bem rigida: nada observado em 2025 entra no treino. Isso
    preserva o ano inteiro como teste final fora da amostra e permite comparar
    diretamente o previsto com o observado em cada mes de 2025.
    """
    rows: list[dict[str, object]] = []

    for forecaster in FORECASTERS:
        result = forecaster(train, len(test), test.index)
        for target_date, real_value, predicted_value in zip(test.index, test, result.forecast):
            rows.append(
                {
                    "data": target_date,
                    "modelo": result.model,
                    "real": float(real_value),
                    "previsto": float(predicted_value),
                    "horizonte_meses": HORIZON_MONTHS,
                    "treino_inicio": train.index.min(),
                    "treino_fim": train.index.max(),
                    "n_meses_treino": len(train),
                }
            )

    return pd.DataFrame(rows)


def calculate_metrics(forecasts: pd.DataFrame) -> pd.DataFrame:
    """Calcula MAE, RMSE, WMAPE e vies percentual para cada modelo."""
    return (
        forecasts.groupby("modelo", group_keys=False)
        .apply(lambda g: pd.Series(metric_row(g.name, g["real"], g["previsto"])), include_groups=False)
        .reset_index(drop=True)
        .sort_values(["WMAPE", "RMSE"])
    )


def official_test_comparison(project_outputs: Path, best_wmape_2025: float) -> str:
    """
    Compara o novo teste com o teste oficial, se o CSV oficial ja existir.

    O teste oficial em outputs/metricas_teste_final.csv e mantido intacto. Aqui
    apenas lemos o arquivo para contextualizar se o resultado de 2025 ficou
    melhor, pior ou parecido.
    """
    official_path = project_outputs / "metricas_teste_final.csv"
    if not official_path.exists():
        return "- Comparacao com o teste oficial: nao realizada, pois metricas_teste_final.csv nao foi encontrado."

    official = pd.read_csv(official_path)
    if official.empty or "WMAPE" not in official.columns or "modelo" not in official.columns:
        return "- Comparacao com o teste oficial: nao realizada, pois o CSV oficial nao tem as colunas esperadas."

    official_best = official.sort_values(["WMAPE", "RMSE"]).iloc[0]
    official_model = str(official_best["modelo"])
    official_wmape = float(official_best["WMAPE"])
    diff = best_wmape_2025 - official_wmape

    if abs(diff) < 0.005:
        reading = "resultado muito proximo do teste oficial"
    elif diff > 0:
        reading = "erro maior do que no teste oficial"
    else:
        reading = "erro menor do que no teste oficial"

    return (
        "- Comparacao com o teste oficial: "
        f"o melhor WMAPE oficial foi {official_wmape:.2%} ({official_model}); "
        f"no teste complementar de 2025 foi {best_wmape_2025:.2%}, indicando {reading}."
    )


def write_summary(
    train: pd.Series,
    test: pd.Series,
    metrics: pd.DataFrame,
    comparison_text: str,
) -> str:
    """Monta um resumo em texto simples para leitura rapida e auditoria."""
    best = metrics.iloc[0]
    best_model = str(best["modelo"])
    best_wmape = float(best["WMAPE"])

    return f"""Teste complementar: ano de 2025 como teste final fora da amostra

Periodo de treino inicial:
- {train.index.min().date()} a {train.index.max().date()}
- Meses no treino inicial: {len(train)}

Periodo de teste:
- {test.index.min().date()} a {test.index.max().date()}
- Meses no teste: {len(test)}

Desenho do teste:
- Base diaria lida de: {BASE_PATH}
- Agregacao usada: mensal
- Variavel alvo: volume expedido total em toneladas
- Horizonte de previsao: {HORIZON_MONTHS} mes(es) a frente
- O teste usa 2021-2024 como historico fixo de treino e reserva todo o ano de 2025 como teste fora da amostra.

Modelos comparados:
- naive ultimo mes
- naive sazonal de 12 meses
- media movel de 3 meses
- drift linear
- suavizacao exponencial simples
- Holt com tendencia

Melhor modelo por WMAPE no teste complementar de 2025:
- {best_model}
- WMAPE: {best_wmape:.2%}

Metricas por modelo:
{metrics.to_string(index=False)}

{comparison_text}
"""


def main() -> None:
    TEST_2025_DIR.mkdir(parents=True, exist_ok=True)

    df_daily = read_base(BASE_PATH)
    monthly = monthly_series(df_daily)
    series = monthly["vol_total"].astype(float)

    train, test = select_train_and_test(series)
    forecasts = forecast_2025_from_previous_years(train, test)
    metrics = calculate_metrics(forecasts)

    best_wmape = float(metrics.iloc[0]["WMAPE"])
    comparison = official_test_comparison(OUTPUT_DIR, best_wmape)
    summary = write_summary(train, test, metrics, comparison)

    forecasts.to_csv(TEST_2025_DIR / "previsoes_2025_teste_final.csv", index=False, encoding="utf-8-sig")
    metrics.to_csv(TEST_2025_DIR / "metricas_2025_teste_final.csv", index=False, encoding="utf-8-sig")
    (TEST_2025_DIR / "resumo_teste_2025.txt").write_text(summary, encoding="utf-8")

    print(summary)
    print(f"Arquivos gerados em: {TEST_2025_DIR}")


if __name__ == "__main__":
    main()
