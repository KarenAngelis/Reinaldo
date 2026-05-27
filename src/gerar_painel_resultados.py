"""
Gera um painel HTML estatico para apresentar os resultados da modelagem.

Execute depois de rodar:
    python src/modelagem_revisada_reinaldo.py

Saida:
    outputs/painel_resultados.html
"""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = PROJECT_ROOT / "outputs"
PANEL_PATH = OUTPUT_DIR / "painel_resultados.html"


def read_csv(name: str) -> pd.DataFrame:
    # Pequeno atalho para ler arquivos da pasta outputs.
    # Se a pessoa esquecer de rodar a modelagem antes, a mensagem ja explica o que fazer.
    path = OUTPUT_DIR / name
    if not path.exists():
        raise FileNotFoundError(
            f"Arquivo nao encontrado: {path}. Execute src/modelagem_revisada_reinaldo.py antes."
        )
    return pd.read_csv(path)


def pct(value: float) -> str:
    # Transforma 0.134 em "13.4%", que e bem melhor para apresentar.
    return f"{value * 100:.1f}%"


def number(value: float) -> str:
    # Formata numeros no padrao brasileiro, sem casas decimais.
    return f"{value:,.0f}".replace(",", ".")


def prepare_payload() -> dict:
    # Esta funcao prepara os dados para o painel.
    # Em vez de fazer contas no HTML, deixamos tudo organizado aqui no Python.
    monthly = read_csv("dados_mensais_limpos.csv")
    validation_metrics = read_csv("metricas_validacao_interna.csv")
    test_metrics = read_csv("metricas_teste_final.csv")
    test_forecasts = read_csv("previsoes_teste_final.csv")
    stock = read_csv("dimensionamento_estoque.csv")

    for frame in [monthly, test_forecasts, stock]:
        frame["data"] = pd.to_datetime(frame["data"]).dt.strftime("%Y-%m-%d")

    validation_metrics = validation_metrics.sort_values(["WMAPE", "RMSE"]).reset_index(drop=True)
    test_metrics = test_metrics.sort_values(["WMAPE", "RMSE"]).reset_index(drop=True)

    best_validation = validation_metrics.iloc[0].to_dict()
    best_test = test_metrics.iloc[0].to_dict()

    # Selecionamos apenas as colunas que o painel realmente precisa.
    # Isso deixa o HTML mais leve e mais facil de entender.
    monthly_demand = monthly[["data", "vol_total", "estoque_total_medio", "cobertura_observada_meses"]]
    stock_view = stock[
        [
            "data",
            "real",
            "previsto",
            "estoque_total_medio",
            "estoque_seguranca",
            "estoque_necessario",
            "saldo_vs_estoque_medio",
        ]
    ]

    return {
        "summary": {
            "months": int(len(monthly)),
            "period_start": monthly["data"].iloc[0],
            "period_end": monthly["data"].iloc[-1],
            "best_validation_model": best_validation["modelo"],
            "best_validation_wmape": pct(float(best_validation["WMAPE"])),
            "best_test_model": best_test["modelo"],
            "best_test_wmape": pct(float(best_test["WMAPE"])),
            "average_monthly_demand": number(float(monthly["vol_total"].mean())),
            "latest_month_demand": number(float(monthly["vol_total"].iloc[-1])),
            "latest_stock_need": number(float(stock["estoque_necessario"].iloc[-1])),
            "latest_stock_gap": number(float(stock["saldo_vs_estoque_medio"].iloc[-1])),
        },
        "monthly": monthly_demand.to_dict(orient="records"),
        "validationMetrics": validation_metrics.to_dict(orient="records"),
        "testMetrics": test_metrics.to_dict(orient="records"),
        "testForecasts": test_forecasts.to_dict(orient="records"),
        "stock": stock_view.to_dict(orient="records"),
    }


def build_html(payload: dict) -> str:
    # O painel e um HTML unico: ele ja leva os dados, o estilo e os graficos.
    # Assim a pessoa pode abrir o arquivo no navegador sem instalar servidor web.
    data_json = json.dumps(payload, ensure_ascii=False)
    return f"""<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Painel de Resultados | Reinaldo</title>
  <style>
    :root {{
      --bg: #F7F8FA;
      --surface: #FFFFFF;
      --text: #1D2430;
      --muted: #637083;
      --line: #D8DEE8;
      --teal: #0F766E;
      --indigo: #4F46E5;
      --amber: #B7791F;
      --rose: #C2415B;
      --green-soft: #E6F4F1;
      --indigo-soft: #ECEBFF;
      --amber-soft: #FFF4D8;
      --rose-soft: #FCE7EC;
      --shadow: 0 12px 30px rgba(29, 36, 48, 0.08);
    }}

    * {{ box-sizing: border-box; }}

    body {{
      margin: 0;
      background: var(--bg);
      color: var(--text);
      font-family: Arial, Helvetica, sans-serif;
      letter-spacing: 0;
    }}

    .shell {{
      width: min(1280px, calc(100% - 32px));
      margin: 0 auto;
      padding: 28px 0 44px;
    }}

    header {{
      display: grid;
      grid-template-columns: minmax(0, 1fr) auto;
      gap: 20px;
      align-items: end;
      padding: 4px 0 22px;
      border-bottom: 1px solid var(--line);
    }}

    h1 {{
      margin: 0 0 8px;
      font-size: 30px;
      line-height: 1.12;
      font-weight: 700;
    }}

    .subtitle {{
      margin: 0;
      color: var(--muted);
      font-size: 14px;
      line-height: 1.45;
      max-width: 760px;
    }}

    .badge {{
      display: inline-flex;
      align-items: center;
      min-height: 34px;
      padding: 8px 12px;
      border: 1px solid var(--line);
      border-radius: 8px;
      background: var(--surface);
      color: var(--muted);
      font-size: 13px;
      white-space: nowrap;
    }}

    .kpis {{
      display: grid;
      grid-template-columns: repeat(4, minmax(0, 1fr));
      gap: 12px;
      margin: 18px 0;
    }}

    .card {{
      background: var(--surface);
      border: 1px solid var(--line);
      border-radius: 8px;
      box-shadow: var(--shadow);
    }}

    .kpi {{
      min-height: 116px;
      padding: 16px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      border-top: 4px solid var(--teal);
    }}

    .kpi:nth-child(2) {{ border-top-color: var(--indigo); }}
    .kpi:nth-child(3) {{ border-top-color: var(--amber); }}
    .kpi:nth-child(4) {{ border-top-color: var(--rose); }}

    .kpi-label {{
      color: var(--muted);
      font-size: 12px;
      text-transform: uppercase;
      font-weight: 700;
    }}

    .kpi-value {{
      margin-top: 12px;
      font-size: 26px;
      line-height: 1.05;
      font-weight: 700;
    }}

    .kpi-note {{
      margin-top: 8px;
      color: var(--muted);
      font-size: 12px;
      line-height: 1.35;
    }}

    .grid {{
      display: grid;
      grid-template-columns: 1.25fr 0.75fr;
      gap: 14px;
      margin-top: 14px;
    }}

    .panel {{
      padding: 16px;
      min-width: 0;
    }}

    .panel-head {{
      display: flex;
      justify-content: space-between;
      gap: 14px;
      align-items: flex-start;
      margin-bottom: 12px;
    }}

    h2 {{
      margin: 0;
      font-size: 17px;
      line-height: 1.25;
    }}

    .hint {{
      margin: 5px 0 0;
      color: var(--muted);
      font-size: 12px;
      line-height: 1.35;
    }}

    .segmented {{
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      justify-content: flex-end;
    }}

    button {{
      border: 1px solid var(--line);
      border-radius: 8px;
      background: #F9FAFB;
      color: var(--text);
      padding: 8px 10px;
      font-size: 12px;
      cursor: pointer;
    }}

    button.active {{
      border-color: var(--teal);
      background: var(--green-soft);
      color: #0B4F49;
      font-weight: 700;
    }}

    .chart-wrap {{
      position: relative;
      width: 100%;
      height: 310px;
    }}

    .chart-wrap.tall {{ height: 370px; }}
    canvas {{ width: 100%; height: 100%; display: block; }}

    table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 12px;
    }}

    th, td {{
      padding: 10px 8px;
      border-bottom: 1px solid var(--line);
      text-align: right;
      white-space: nowrap;
    }}

    th:first-child, td:first-child {{
      text-align: left;
      white-space: normal;
    }}

    th {{
      color: var(--muted);
      font-size: 11px;
      text-transform: uppercase;
    }}

    .pill {{
      display: inline-block;
      padding: 4px 7px;
      border-radius: 8px;
      font-size: 11px;
      font-weight: 700;
      background: var(--indigo-soft);
      color: #3730A3;
    }}

    .note-band {{
      margin-top: 14px;
      padding: 14px 16px;
      border-left: 4px solid var(--amber);
      background: var(--amber-soft);
      color: #5D4214;
      border-radius: 8px;
      font-size: 13px;
      line-height: 1.45;
    }}

    .two-col {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 14px;
      margin-top: 14px;
    }}

    @media (max-width: 980px) {{
      header, .grid, .two-col {{ grid-template-columns: 1fr; }}
      .kpis {{ grid-template-columns: repeat(2, minmax(0, 1fr)); }}
      .panel-head {{ flex-direction: column; }}
      .segmented {{ justify-content: flex-start; }}
    }}

    @media (max-width: 620px) {{
      .shell {{ width: min(100% - 20px, 1280px); padding-top: 18px; }}
      .kpis {{ grid-template-columns: 1fr; }}
      h1 {{ font-size: 24px; }}
      .chart-wrap, .chart-wrap.tall {{ height: 280px; }}
      th, td {{ padding: 8px 6px; }}
    }}
  </style>
</head>
<body>
  <main class="shell">
    <header>
      <div>
        <h1>Painel de resultados da modelagem</h1>
        <p class="subtitle">Comparativo de modelos de previsao de demanda, validacao temporal, teste final e reflexos no dimensionamento de estoque.</p>
      </div>
      <div class="badge" id="periodBadge"></div>
    </header>

    <section class="kpis">
      <article class="card kpi">
        <div class="kpi-label">Melhor validacao</div>
        <div>
          <div class="kpi-value" id="bestValidation"></div>
          <div class="kpi-note" id="bestValidationNote"></div>
        </div>
      </article>
      <article class="card kpi">
        <div class="kpi-label">Melhor teste final</div>
        <div>
          <div class="kpi-value" id="bestTest"></div>
          <div class="kpi-note" id="bestTestNote"></div>
        </div>
      </article>
      <article class="card kpi">
        <div class="kpi-label">Demanda mensal media</div>
        <div>
          <div class="kpi-value" id="avgDemand"></div>
          <div class="kpi-note">Toneladas no periodo agregado</div>
        </div>
      </article>
      <article class="card kpi">
        <div class="kpi-label">Estoque necessario final</div>
        <div>
          <div class="kpi-value" id="latestStockNeed"></div>
          <div class="kpi-note" id="latestStockGap"></div>
        </div>
      </article>
    </section>

    <section class="grid">
      <article class="card panel">
        <div class="panel-head">
          <div>
            <h2>Serie mensal de demanda</h2>
            <p class="hint">Volume expedido total em toneladas, agregado da base diaria.</p>
          </div>
        </div>
        <div class="chart-wrap tall"><canvas id="monthlyChart"></canvas></div>
      </article>

      <article class="card panel">
        <div class="panel-head">
          <div>
            <h2>Ranking por WMAPE</h2>
            <p class="hint">Quanto menor, melhor. A validacao escolhe o modelo; o teste final mede robustez.</p>
          </div>
        </div>
        <div class="chart-wrap tall"><canvas id="wmapeChart"></canvas></div>
      </article>
    </section>

    <section class="card panel" style="margin-top: 14px;">
      <div class="panel-head">
        <div>
          <h2>Previsao no teste final</h2>
          <p class="hint">Selecione o modelo para comparar a previsao contra a demanda observada nos ultimos 12 meses.</p>
        </div>
        <div class="segmented" id="modelButtons"></div>
      </div>
      <div class="chart-wrap tall"><canvas id="forecastChart"></canvas></div>
    </section>

    <section class="two-col">
      <article class="card panel">
        <div class="panel-head">
          <div>
            <h2>Metricas do teste final</h2>
            <p class="hint">Tabela pronta para leitura rapida dos modelos comparados.</p>
          </div>
        </div>
        <div style="overflow-x:auto;">
          <table id="metricsTable"></table>
        </div>
      </article>

      <article class="card panel">
        <div class="panel-head">
          <div>
            <h2>Dimensionamento de estoque</h2>
            <p class="hint">Estoque necessario calculado com previsao, erro validado e nivel de servico.</p>
          </div>
        </div>
        <div class="chart-wrap"><canvas id="stockChart"></canvas></div>
      </article>
    </section>

    <section class="note-band">
      Leitura metodologica: os resultados confirmam que a previsao deve ser apresentada com cautela. A diferenca entre o melhor modelo na validacao e o melhor no teste final reforca a recomendacao de posicionar a tese como framework gerencial de apoio a decisao, nao como demonstracao de acuracia perfeita ou otimizacao matematica.
    </section>
  </main>

  <script>
    const DATA = {data_json};

    // Funcoes pequenas de formatacao para deixar numeros e datas mais amigaveis.
    const fmtPct = value => `${{(Number(value) * 100).toFixed(1)}}%`;
    const fmtNum = value => Number(value).toLocaleString("pt-BR", {{ maximumFractionDigits: 0 }});
    const fmtMonth = value => {{
      const date = new Date(`${{value}}T00:00:00`);
      const months = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"];
      return `${{months[date.getMonth()]}}/${{String(date.getFullYear()).slice(-2)}}`;
    }};

    function setText(id, value) {{
      document.getElementById(id).textContent = value;
    }}

    // Desenha os eixos dos graficos no canvas.
    // Foi feito sem biblioteca externa para o painel continuar portavel.
    function drawAxes(ctx, area, maxY, labels) {{
      ctx.strokeStyle = "#D8DEE8";
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(area.left, area.top);
      ctx.lineTo(area.left, area.bottom);
      ctx.lineTo(area.right, area.bottom);
      ctx.stroke();

      ctx.fillStyle = "#637083";
      ctx.font = "11px Arial";
      ctx.textAlign = "right";
      ctx.textBaseline = "middle";
      for (let i = 0; i <= 4; i += 1) {{
        const y = area.bottom - (area.height * i / 4);
        const value = maxY * i / 4;
        ctx.strokeStyle = "#EEF1F5";
        ctx.beginPath();
        ctx.moveTo(area.left, y);
        ctx.lineTo(area.right, y);
        ctx.stroke();
        ctx.fillText(fmtNum(value), area.left - 8, y);
      }}

      if (labels.length > 0) {{
        ctx.textAlign = "center";
        ctx.textBaseline = "top";
        const step = Math.max(1, Math.floor(labels.length / 6));
        labels.forEach((label, index) => {{
          if (index % step === 0 || index === labels.length - 1) {{
            const x = area.left + (area.width * index / Math.max(labels.length - 1, 1));
            ctx.fillText(fmtMonth(label), x, area.bottom + 10);
          }}
        }});
      }}
    }}

    function setupCanvas(canvas) {{
      // Ajusta o canvas para telas comuns e telas de alta resolucao.
      const rect = canvas.getBoundingClientRect();
      const dpr = window.devicePixelRatio || 1;
      canvas.width = Math.floor(rect.width * dpr);
      canvas.height = Math.floor(rect.height * dpr);
      const ctx = canvas.getContext("2d");
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      return {{ ctx, width: rect.width, height: rect.height }};
    }}

    function lineChart(canvasId, series, options) {{
      // Grafico de linha usado para demanda, previsao e estoque.
      const canvas = document.getElementById(canvasId);
      const {{ ctx, width, height }} = setupCanvas(canvas);
      ctx.clearRect(0, 0, width, height);
      const area = {{ left: 62, right: width - 20, top: 20, bottom: height - 42 }};
      area.width = area.right - area.left;
      area.height = area.bottom - area.top;
      const labels = series[0].points.map(point => point.x);
      const maxY = Math.max(...series.flatMap(item => item.points.map(point => point.y))) * 1.12;
      drawAxes(ctx, area, maxY, labels);

      series.forEach(item => {{
        ctx.strokeStyle = item.color;
        ctx.lineWidth = item.width || 2;
        ctx.setLineDash(item.dash || []);
        ctx.beginPath();
        item.points.forEach((point, index) => {{
          const x = area.left + (area.width * index / Math.max(item.points.length - 1, 1));
          const y = area.bottom - (point.y / maxY) * area.height;
          if (index === 0) ctx.moveTo(x, y);
          else ctx.lineTo(x, y);
        }});
        ctx.stroke();
        ctx.setLineDash([]);
      }});

      if (options?.legend) drawLegend(ctx, options.legend, area.left, 4);
    }}

    function drawLegend(ctx, items, x, y) {{
      // Legenda simples desenhada no proprio canvas.
      ctx.font = "12px Arial";
      ctx.textAlign = "left";
      ctx.textBaseline = "middle";
      let offset = 0;
      items.forEach(item => {{
        ctx.fillStyle = item.color;
        ctx.fillRect(x + offset, y + 6, 18, 3);
        ctx.fillStyle = "#637083";
        ctx.fillText(item.label, x + offset + 24, y + 8);
        offset += ctx.measureText(item.label).width + 54;
      }});
    }}

    function barChart(canvasId, rows, options) {{
      // Grafico de barras horizontais usado para comparar WMAPE dos modelos.
      const canvas = document.getElementById(canvasId);
      const {{ ctx, width, height }} = setupCanvas(canvas);
      ctx.clearRect(0, 0, width, height);
      const area = {{ left: 142, right: width - 22, top: 24, bottom: height - 24 }};
      area.width = area.right - area.left;
      area.height = area.bottom - area.top;
      const maxValue = Math.max(...rows.flatMap(row => row.values)) * 1.18;
      const rowHeight = area.height / rows.length;
      ctx.font = "11px Arial";
      rows.forEach((row, index) => {{
        const y = area.top + index * rowHeight + rowHeight * 0.18;
        ctx.fillStyle = "#1D2430";
        ctx.textAlign = "right";
        ctx.textBaseline = "middle";
        ctx.fillText(row.label, area.left - 10, y + rowHeight * 0.32);
        row.values.forEach((value, seriesIndex) => {{
          const barHeight = Math.min(16, rowHeight * 0.28);
          const barY = y + seriesIndex * (barHeight + 4);
          const barWidth = (value / maxValue) * area.width;
          ctx.fillStyle = options.colors[seriesIndex];
          ctx.fillRect(area.left, barY, barWidth, barHeight);
          ctx.fillStyle = "#637083";
          ctx.textAlign = "left";
          ctx.fillText(fmtPct(value), area.left + barWidth + 6, barY + barHeight / 2);
        }});
      }});
      drawLegend(ctx, options.legend, area.left, 2);
    }}

    function stockChart() {{
      // Mostra estoque necessario versus estoque medio observado no teste final.
      const rows = DATA.stock;
      lineChart("stockChart", [
        {{ color: "#0F766E", points: rows.map(row => ({{ x: row.data, y: Number(row.estoque_necessario) }})) }},
        {{ color: "#C2415B", points: rows.map(row => ({{ x: row.data, y: Number(row.estoque_total_medio) }})), dash: [5, 4] }},
      ], {{
        legend: [
          {{ label: "Estoque necessario", color: "#0F766E" }},
          {{ label: "Estoque medio observado", color: "#C2415B" }},
        ]
      }});
    }}

    function renderForecast(model) {{
      // Atualiza o grafico Real vs Previsto quando a pessoa clica em outro modelo.
      document.querySelectorAll("#modelButtons button").forEach(button => {{
        button.classList.toggle("active", button.dataset.model === model);
      }});
      const rows = DATA.testForecasts.filter(row => row.modelo === model);
      lineChart("forecastChart", [
        {{ color: "#1D2430", width: 2.5, points: rows.map(row => ({{ x: row.data, y: Number(row.real) }})) }},
        {{ color: "#4F46E5", width: 2.5, points: rows.map(row => ({{ x: row.data, y: Number(row.previsto) }})) }},
      ], {{
        legend: [
          {{ label: "Real", color: "#1D2430" }},
          {{ label: "Previsto", color: "#4F46E5" }},
        ]
      }});
    }}

    function renderMetricsTable() {{
      // Monta a tabela final de metricas em HTML.
      const table = document.getElementById("metricsTable");
      table.innerHTML = `
        <thead>
          <tr>
            <th>Modelo</th>
            <th>WMAPE</th>
            <th>MAE</th>
            <th>RMSE</th>
            <th>Vies</th>
          </tr>
        </thead>
        <tbody>
          ${{DATA.testMetrics.map((row, index) => `
            <tr>
              <td>${{index === 0 ? '<span class="pill">melhor teste</span> ' : ''}}${{row.modelo}}</td>
              <td>${{fmtPct(row.WMAPE)}}</td>
              <td>${{fmtNum(row.MAE)}}</td>
              <td>${{fmtNum(row.RMSE)}}</td>
              <td>${{fmtPct(row.BIAS_PCT)}}</td>
            </tr>
          `).join("")}}
        </tbody>
      `;
    }}

    function init() {{
      // Ponto de entrada do painel: preenche cards, graficos, botoes e tabela.
      const summary = DATA.summary;
      setText("periodBadge", `${{summary.months}} meses | ${{fmtMonth(summary.period_start)}} a ${{fmtMonth(summary.period_end)}}`);
      setText("bestValidation", summary.best_validation_wmape);
      setText("bestValidationNote", summary.best_validation_model);
      setText("bestTest", summary.best_test_wmape);
      setText("bestTestNote", summary.best_test_model);
      setText("avgDemand", summary.average_monthly_demand);
      setText("latestStockNeed", summary.latest_stock_need);
      setText("latestStockGap", `Saldo vs estoque medio: ${{summary.latest_stock_gap}} t`);

      lineChart("monthlyChart", [
        {{ color: "#0F766E", width: 2.5, points: DATA.monthly.map(row => ({{ x: row.data, y: Number(row.vol_total) }})) }},
        {{ color: "#B7791F", width: 2, points: DATA.monthly.map(row => ({{ x: row.data, y: Number(row.estoque_total_medio) }})), dash: [5, 4] }},
      ], {{
        legend: [
          {{ label: "Demanda", color: "#0F766E" }},
          {{ label: "Estoque medio", color: "#B7791F" }},
        ]
      }});

      const metricRows = DATA.validationMetrics.map(row => {{
        const test = DATA.testMetrics.find(item => item.modelo === row.modelo);
        return {{ label: row.modelo, values: [Number(row.WMAPE), Number(test?.WMAPE || 0)] }};
      }});
      barChart("wmapeChart", metricRows, {{
        colors: ["#0F766E", "#4F46E5"],
        legend: [
          {{ label: "Validacao", color: "#0F766E" }},
          {{ label: "Teste", color: "#4F46E5" }},
        ]
      }});

      const models = [...new Set(DATA.testForecasts.map(row => row.modelo))];
      const buttons = document.getElementById("modelButtons");
      buttons.innerHTML = models.map(model => `<button type="button" data-model="${{model}}">${{model}}</button>`).join("");
      buttons.querySelectorAll("button").forEach(button => {{
        button.addEventListener("click", () => renderForecast(button.dataset.model));
      }});
      renderForecast(DATA.summary.best_validation_model);
      renderMetricsTable();
      stockChart();
    }}

    window.addEventListener("resize", () => {{
      clearTimeout(window.__resizeTimer);
      window.__resizeTimer = setTimeout(init, 150);
    }});

    init();
  </script>
</body>
</html>
"""


def main() -> None:
    # Garante que a pasta outputs exista, monta os dados e grava o HTML final.
    OUTPUT_DIR.mkdir(exist_ok=True)
    payload = prepare_payload()
    PANEL_PATH.write_text(build_html(payload), encoding="utf-8")
    print(f"Painel gerado em: {PANEL_PATH}")


if __name__ == "__main__":
    main()
