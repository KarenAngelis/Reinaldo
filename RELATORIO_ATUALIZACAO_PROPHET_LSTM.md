# Relatório de atualização Prophet/LSTM

Data: 2026-05-27

Arquivo de entrada:

- `docs\Tese_Reinaldo_T_Ribeiro_final_limpa_entrega.docx`

Arquivo gerado:

- `docs\Tese_Reinaldo_T_Ribeiro_final_com_teste_prophet_lstm.docx`

## Objetivo da atualização

Incorporar à tese o teste exploratório complementar com Prophet e LSTM no recorte de 2025, sem alterar a modelagem principal conservadora baseada em modelos simples e interpretáveis.

## Resultados incorporados

- Benchmark `media_movel_3m`: WMAPE de 20,61%.
- Prophet: WMAPE de 18,60%, superou o benchmark no recorte exploratório.
- LSTM simples: WMAPE de 21,97%, foi executada com sucesso, mas não superou o benchmark.
- Ambiente LSTM registrado: Python 3.12.10 com TensorFlow 2.21.0.
- Controles de reprodutibilidade registrados: seed=42, random/numpy/tensorflow fixados, TF_ENABLE_ONEDNN_OPTS=0, operações determinísticas quando disponíveis, shuffle=False e threads limitadas.

## Seções alteradas

- Resumo
- Abstract
- 1.7.1 Estrutura da Pesquisa
- 3.1.4 Modelos Selecionados para Aplicação na Pesquisa
- 3.1.5 Implementação computacional da modelagem
- 3.1.5 Implementação computacional da modelagem
- 3.2.3 Previsão de Demanda
- 3.2.3 Previsão de Demanda
- 3.2.3 Previsão de Demanda - LSTM
- 3.2.3 Previsão de Demanda - Prophet
- 3.2.3 Previsão de Demanda - Resultado principal
- 4. Resultados do Framework e Discussão
- 4. Resultados do Framework e Discussão
- Discussão final - LSTM
- Discussão final - Prophet
- 5. Conclusão
- 5. Conclusão - LSTM
- 5. Conclusão - Prophet

## Tabela inserida

- `Tabela 15 - Resultados do teste exploratório Prophet/LSTM no recorte de 2025`: sim
- A entrada correspondente foi incluída na Lista de Tabelas após a atualização dos campos do Word, pois a estrutura original da tese não incorporou automaticamente a nova legenda ao atualizar a lista.

## Cuidados metodológicos preservados

- A tese não foi reescrita integralmente.
- Prophet e LSTM foram tratados como teste exploratório complementar.
- A modelagem principal permaneceu conservadora, com modelos simples e interpretáveis como sustentação principal.
- O Prophet foi reconhecido como superior ao benchmark apenas no recorte exploratório de 2025.
- A LSTM foi registrada como executada com sucesso, mas sem superar o benchmark.
