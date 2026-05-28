# Auditoria visual e estrutural - Tese Prophet/LSTM

Arquivo auditado: `docs/Tese_Reinaldo_T_Ribeiro_final_com_teste_prophet_lstm_marcado_azul.docx`

Status: relatório de auditoria gerado sem alterar o documento.

## Método de auditoria

- A paginação foi coletada pelo Microsoft Word, totalizando 139 páginas.
- Foram cruzados texto por página, legendas, contagem de tabelas/imagens e blocos em azul.
- Como o LibreOffice/soffice não está disponível neste ambiente, a auditoria visual foi feita pela extração do layout no Word e não por renderização PNG página a página.
- O conteúdo interno das imagens não foi interpretado por OCR; quando a figura antiga pode contradizer a modelagem revisada, a recomendação é substituir ou revisar manualmente no Word.

## Achados gerais

- Linha solta `. 133` no sumário: detectada.
- Páginas com ação diferente de manter: 8, 11, 12, 13, 14, 15, 16, 17, 26, 27, 34, 36, 38, 40, 41, 42, 45, 46, 48, 49, 51, 52, 53, 54, 55, 72, 78, 80, 87, 88, 89, 90, 91, 94, 95, 96, 98, 99, 101, 102, 122, 123, 125, 126, 130, 131, 132
- Página(s) onde a Tabela 15 aparece: 17, 125
- Contagem de ações: {'manter': 99, 'revisar texto': 41, 'corrigir formatação': 5, 'substituir imagem': 7}

## Pontos críticos antes de qualquer nova edição

- Listas automáticas apresentam duplicações aparentes em várias entradas, especialmente Lista de Figuras e Lista de Tabelas.
- Figura 2 deve ser substituída por um fluxo atualizado se ainda apresentar Prophet/LSTM como eixo principal.
- Figuras antigas de SARIMA, Holt-Winters, LSTM, Prophet e 5 modelos testados devem ser tratadas como exploratórias ou substituídas por gráficos da modelagem revisada.
- Quadro 14 ainda apresenta R²/valor métrica e deve ser revisado para não sugerir ajuste perfeito.
- Tabelas comparativas antigas ainda podem mencionar Prophet/otimização/WMAPE incompatível com a versão revisada.

## Auditoria página por página

### Página 1

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 2

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 3

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: há figura/tabela/quadro; verificar conforme legendas. Tabelas detectadas: 1; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 4

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 5

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 6

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 7

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 8

1. Texto azul: sim.
2. Coerência do azul: coerente com a modelagem revisada, desde que mantido como complemento exploratório.
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: otimização.
6. Problemas observados: termo "otimização" aparece fora de contexto claramente bibliográfico; verificar se deve virar dimensionamento/calibração..
7. Ação recomendada: revisar texto.

### Página 9

1. Texto azul: sim.
2. Coerência do azul: coerente com a modelagem revisada, desde que mantido como complemento exploratório.
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 10

1. Texto azul: sim.
2. Coerência do azul: coerente como marcação de campos/listas alterados, mas exige revisão de duplicações.
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 11

1. Texto azul: sim.
2. Coerência do azul: coerente como marcação de campos/listas alterados, mas exige revisão de duplicações.
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: linha solta ". 133" detectada no sumário.
7. Ação recomendada: corrigir formatação.

### Página 12

1. Texto azul: sim.
2. Coerência do azul: coerente como marcação de campos/listas alterados, mas exige revisão de duplicações.
3. Figura/tabela/quadro: há figura/tabela/quadro; verificar conforme legendas. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: Figura 1 - Exportações e faturamento do Brasil na venda de carne bovina. 23, Figura 2 - Fases da pesquisa 29Figura 2 - Fases da pesquisa 29, Figura 3 - Revisão Sistemática da Literatura 34Figura 3 - Revisão Sistemática da Literatura 34, Figura 4 - Palavras-chave para combinação dos três pilares 36Figura 4 - Palavras-chave para combinação dos três pilares 36, Figura 5 - Etapas para seleção de artigos – Critérios de Inclusão e Exclusão. 38Figura 5 - Etapas para seleção de artigos – Critérios de Inclusão e Exclusão. 38, Figura 6 - Nuvem de palavras-chave 42Figura 6 - Nuvem de palavras-chave 42, Figura 7 - Ano de publicações das 29 publicações. 50, Figura 8 - Número de publicações por país. 50Figura 8 - Número de publicações por país. 50, Figura 9A - Framework proposto simplificado 58Figura 9A - Framework proposto simplificado 58, Figura 10B - Framework proposto detalhado 58Figura 10B - Framework proposto detalhado 58, Figura 11 - Equações LSTM 75Figura 11 - Equações LSTM 75, Figura 12 - Mapa Mental do Estudo 83Figura 12 - Mapa Mental do Estudo 83, Figura 13 - Linhas para os pesos faturados de 2022-2023 85Figura 13 - Linhas para os pesos faturados de 2022-2023 85, Figura 14 - Boxplot para os pesos faturados por ano 87Figura 14 - Boxplot para os pesos faturados por ano 87, Figura 15 - Normal Q-Q Plot para os pesos faturados por ano 87Figura 15 - Normal Q-Q Plot para os pesos faturados por ano 87, Figura 16 - Histograma da normalidade para os pesos faturados de 2022-2023 88Figura 16 - Histograma da normalidade para os pesos faturados de 2022-2023 88.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: duplicação aparente em lista automática de figuras/tabelas/quadros; Figura 2 deve ser confrontada com o fluxo metodológico revisado; risco de mostrar Prophet/LSTM como eixo principal.; figura antiga/exploratória exige conferência: Figura 11 - Equações LSTM 75Figura 11 - Equações LSTM 75.
7. Ação recomendada: corrigir formatação, substituir imagem, revisar texto.

### Página 13

1. Texto azul: sim.
2. Coerência do azul: provável alteração textual/estrutural; revisar visualmente no Word.
3. Figura/tabela/quadro: há figura/tabela/quadro; verificar conforme legendas. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: Figura 17 - Projeção para os pesos faturados de 2024 com modelo Holt-Winters aditivo 91Figura 17 - Projeção para os pesos faturados de 2024 com modelo Holt-Winters aditivo 91, Figura 18 - Projeção para os pesos faturados de 2024 com modelo Holt-Winters multiplicativo 92Figura 18 - Projeção para os pesos faturados de 2024 com modelo Holt-Winters multiplicativo 92, Figura 19 - Projeção o valor real (Observado) X 5 modelos testados 93Figura 19 - Projeção o valor real (Observado) X 5 modelos testados 93, Figura 20 - Parte da tabela dados_estoque, demonstrando a modificação da posição dos dados e nomes das colunas. 96Figura 20 - Parte da tabela dados_estoque, demonstrando a modificação da posição dos dados e nomes das colunas. 96, Figura 21 - Modelo de Dimensionamento de estoque com α demanda calculado 98Figura 21 - Modelo de Dimensionamento de estoque com α demanda calculado 98, Figura 22 - Modelo de Dimensionamento de estoque com α demanda calculado 99Figura 22 - Modelo de Dimensionamento de estoque com α demanda calculado 99, Figura 23 - Modelo com a constante atualizada (c=0,2) 100Figura 23 - Modelo com a constante atualizada (c=0,2) 100, Figura 24 - Distribuição normal e probabilidade e estoque de segurança 111Figura 24 - Distribuição normal e probabilidade e estoque de segurança 111, Figura 25 - Figura 5 - Gráfico do comportamento da demanda e lead time (1º caso) 116Figura 25 - Figura 5 - Gráfico do comportamento da demanda e lead time (1º caso) 116, Figura 26 - Figura 6 - Gráfico do comportamento da demanda e lead time (2º caso) 117Figura 26 - Figura 6 - Gráfico do comportamento da demanda e lead time (2º caso) 117, Figura 27 - Gráfico do comportamento da demanda e lead time (3º caso) 118Figura 27 - Gráfico do comportamento da demanda e lead time (3º caso) 118, Figura 28 - Gráfico do comportamento da demanda e lead time (4º caso) 118Figura 28 - Gráfico do comportamento da demanda e lead time (4º caso) 118, Figura 29 - Exemplo de Efeito Chicote 122Figura 29 - Exemplo de Efeito Chicote 122.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: figura antiga/exploratória exige conferência: Figura 17 - Projeção para os pesos faturados de 2024 com modelo Holt-Winters aditivo 91Figura 17 - Projeção para os peso; figura antiga/exploratória exige conferência: Figura 18 - Projeção para os pesos faturados de 2024 com modelo Holt-Winters multiplicativo 92Figura 18 - Projeção para ; figura antiga/exploratória exige conferência: Figura 19 - Projeção o valor real (Observado) X 5 modelos testados 93Figura 19 - Projeção o valor real (Observado) X 5 m.
7. Ação recomendada: substituir imagem.

### Página 14

1. Texto azul: sim.
2. Coerência do azul: provável alteração textual/estrutural; revisar visualmente no Word.
3. Figura/tabela/quadro: há figura/tabela/quadro; verificar conforme legendas. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: Figura 30 - Gráfico da Curva ABC 130Figura 30 - Gráfico da Curva ABC 130, Figura 31 - Metodologia CRISP-DM 131Figura 31 - Metodologia CRISP-DM 131, Figura 32 - Exemplos de séries temporais 132Figura 32 - Exemplos de séries temporais 132, Quadro 1 - Resumo da metodologia da pesquisa 28.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: duplicação aparente em lista automática de figuras/tabelas/quadros.
7. Ação recomendada: corrigir formatação.

### Página 15

1. Texto azul: sim.
2. Coerência do azul: provável alteração textual/estrutural; revisar visualmente no Word.
3. Figura/tabela/quadro: há figura/tabela/quadro; verificar conforme legendas. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: Quadro 2 - Classificação de periódicos conforme SJR. 39Quadro 2 - Classificação de periódicos conforme SJR. 39, Quadro 3 - Distribuição de publicações entre os anos de 2010 e 2025. 40Quadro 3 - Distribuição de publicações entre os anos de 2010 e 2025. 40, Quadro 4 - Nível de aderência dos artigos 41Quadro 4 - Nível de aderência dos artigos 41, Quadro 5 - Palavras-chave da Análise do Conteúdo 43Quadro 5 - Palavras-chave da Análise do Conteúdo 43, Quadro 6 - Categorização das pesquisas por área 45Quadro 6 - Categorização das pesquisas por área 45, Quadro 7 - Concentração de estudos por área. 48Quadro 7 - Concentração de estudos por área. 48, Quadro 8 - Contribuições, Aplicações e limitações dos artigos 51Quadro 8 - Contribuições, Aplicações e limitações dos artigos 51, Quadro 9 - Parte das informações relacionadas à família 1 105Quadro 9 - Parte das informações relacionadas à família 1 105, Quadro 10 - Parte das informações relacionadas à família 2 105Quadro 10 - Parte das informações relacionadas à família 2 105, Quadro 11 - Parte das informações relacionadas à família 3 106Quadro 11 - Parte das informações relacionadas à família 3 106, Quadro 12 - Parte das informações relacionadas à família 4 106Quadro 12 - Parte das informações relacionadas à família 4 106, Quadro 13 - Parte das informações relacionadas à família 5 106Quadro 13 - Parte das informações relacionadas à família 5 106, Quadro 14 - Algumas métricas do modelo proposto 129Quadro 14 - Algumas métricas do modelo proposto 129.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: R² / Quadro 14 pode induzir interpretação antiga de ajuste perfeito..
7. Ação recomendada: revisar texto.

### Página 16

1. Texto azul: sim.
2. Coerência do azul: coerente como marcação de campos/listas alterados, mas exige revisão de duplicações.
3. Figura/tabela/quadro: há figura/tabela/quadro; verificar conforme legendas. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: Tabela 1 - Descritiva para os pesos faturados de 2022-2023 (em kg) 85, Tabela 2 - Testes de normalidade, estacionariedade, tendência e sazonalidade 88Tabela 2 - Testes de normalidade, estacionariedade, tendência e sazonalidade 88, Tabela 3 - Comparativo dos pesos faturados 2024 - observados e estimados 94Tabela 3 - Comparativo dos pesos faturados 2024 - observados e estimados 94, Tabela 4 - Medidas de erros de previsão 94Tabela 4 - Medidas de erros de previsão 94, Tabela 5 - Parte dos dados relacionados à Família 1 101Tabela 5 - Parte dos dados relacionados à Família 1 101, Tabela 6 - Primeira linha referente aos dados relacionados à Família 1 102Tabela 6 - Primeira linha referente aos dados relacionados à Família 1 102, Tabela 7 - Cálculo do Estoque de Segurança para cada constante 103Tabela 7 - Cálculo do Estoque de Segurança para cada constante 103, Tabela 8 - Cálculo do Estoque Necessário para cada constante 103Tabela 8 - Cálculo do Estoque Necessário para cada constante 103, Tabela 9 - Cálculo do MSE para cada constante 104Tabela 9 - Cálculo do MSE para cada constante 104, Tabela 10 - Cálculo do MSE e da Penalidade para cada constante 104Tabela 10 - Cálculo do MSE e da Penalidade para cada constante 104, Tabela 11 - Comparação entre o nosso modelo e um modelo clássico utilizando redes neurais artificiais 125Tabela 11 - Comparação entre o nosso modelo e um modelo clássico utilizando redes neurais artificiais 125.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: duplicação aparente em lista automática de figuras/tabelas/quadros.
7. Ação recomendada: corrigir formatação.

### Página 17

1. Texto azul: sim.
2. Coerência do azul: coerente com a modelagem revisada, desde que mantido como complemento exploratório.
3. Figura/tabela/quadro: há figura/tabela/quadro; verificar conforme legendas. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: Tabela 12 - Comparação entre o modelo proposto e um modelo do artigo de Gomes, G. et al.(2023) 126Tabela 12 - Comparação entre o modelo proposto e um modelo do artigo de Gomes, G. et al.(2023) 126, Tabela 15 - Resultados do teste exploratório Prophet/LSTM no recorte de 2025 123.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: figura antiga/exploratória exige conferência: Tabela 15 - Resultados do teste exploratório Prophet/LSTM no recorte de 2025 123; Tabela Prophet/LSTM presente; conferir lista de tabelas e numeração.; Tabela 15 aparece na lista de tabelas; página também inicia Introdução, sugerindo quebra/espacamento apertado..
7. Ação recomendada: revisar texto, manter, corrigir formatação.

### Página 18

1. Texto azul: sim.
2. Coerência do azul: coerente com a modelagem revisada, desde que mantido como complemento exploratório.
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 19

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 20

1. Texto azul: sim.
2. Coerência do azul: provável alteração textual/estrutural; revisar visualmente no Word.
3. Figura/tabela/quadro: elementos presentes, sem contradição automática detectada. Tabelas detectadas: 0; imagens detectadas: 1.
4. Legendas detectadas: Figura 1 - Exportações e faturamento do Brasil na venda de carne bovina..
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 21

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 22

1. Texto azul: sim.
2. Coerência do azul: coerente com a modelagem revisada, desde que mantido como complemento exploratório.
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 23

1. Texto azul: sim.
2. Coerência do azul: coerente com a modelagem revisada, desde que mantido como complemento exploratório.
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 24

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 25

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: elementos presentes, sem contradição automática detectada. Tabelas detectadas: 1; imagens detectadas: 0.
4. Legendas detectadas: Quadro 1 - Resumo da metodologia da pesquisa.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 26

1. Texto azul: sim.
2. Coerência do azul: coerente com a modelagem revisada, desde que mantido como complemento exploratório.
3. Figura/tabela/quadro: há figura/tabela/quadro; verificar conforme legendas. Tabelas detectadas: 0; imagens detectadas: 1.
4. Legendas detectadas: Figura 2 - Fases da pesquisa.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: Figura 2 deve ser confrontada com o fluxo metodológico revisado; risco de mostrar Prophet/LSTM como eixo principal..
7. Ação recomendada: substituir imagem.

### Página 27

1. Texto azul: sim.
2. Coerência do azul: coerente com a modelagem revisada, desde que mantido como complemento exploratório.
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: otimização.
6. Problemas observados: termo "otimização" aparece fora de contexto claramente bibliográfico; verificar se deve virar dimensionamento/calibração..
7. Ação recomendada: revisar texto.

### Página 28

1. Texto azul: sim.
2. Coerência do azul: coerente com a modelagem revisada, desde que mantido como complemento exploratório.
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 29

1. Texto azul: sim.
2. Coerência do azul: coerente com a modelagem revisada, desde que mantido como complemento exploratório.
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 30

1. Texto azul: sim.
2. Coerência do azul: coerente com a modelagem revisada, desde que mantido como complemento exploratório.
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 31

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: elementos presentes, sem contradição automática detectada. Tabelas detectadas: 0; imagens detectadas: 1.
4. Legendas detectadas: Figura 3 - Revisão Sistemática da Literatura.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 32

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 33

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: elementos presentes, sem contradição automática detectada. Tabelas detectadas: 0; imagens detectadas: 1.
4. Legendas detectadas: Figura 4 - Palavras-chave para combinação dos três pilares.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 34

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: otimização.
6. Problemas observados: termo "otimização" aparece fora de contexto claramente bibliográfico; verificar se deve virar dimensionamento/calibração..
7. Ação recomendada: revisar texto.

### Página 35

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 36

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: há figura/tabela/quadro; verificar conforme legendas. Tabelas detectadas: 1; imagens detectadas: 0.
4. Legendas detectadas: Quadro 2 - Classificação de periódicos conforme SJR..
5. Termos antigos/atenção: otimização.
6. Problemas observados: termo "otimização" aparece fora de contexto claramente bibliográfico; verificar se deve virar dimensionamento/calibração..
7. Ação recomendada: revisar texto.

### Página 37

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: elementos presentes, sem contradição automática detectada. Tabelas detectadas: 2; imagens detectadas: 0.
4. Legendas detectadas: Quadro 3 - Distribuição de publicações entre os anos de 2010 e 2025..
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 38

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: há figura/tabela/quadro; verificar conforme legendas. Tabelas detectadas: 1; imagens detectadas: 0.
4. Legendas detectadas: Quadro 4 - Nível de aderência dos artigos.
5. Termos antigos/atenção: otimização.
6. Problemas observados: termo "otimização" aparece fora de contexto claramente bibliográfico; verificar se deve virar dimensionamento/calibração..
7. Ação recomendada: revisar texto.

### Página 39

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: elementos presentes, sem contradição automática detectada. Tabelas detectadas: 0; imagens detectadas: 1.
4. Legendas detectadas: Figura 6 - Nuvem de palavras-chave.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 40

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: há figura/tabela/quadro; verificar conforme legendas. Tabelas detectadas: 1; imagens detectadas: 0.
4. Legendas detectadas: Quadro 5 - Palavras-chave da Análise do Conteúdo.
5. Termos antigos/atenção: otimização.
6. Problemas observados: termo "otimização" aparece fora de contexto claramente bibliográfico; verificar se deve virar dimensionamento/calibração..
7. Ação recomendada: revisar texto.

### Página 41

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: otimização.
6. Problemas observados: termo "otimização" aparece fora de contexto claramente bibliográfico; verificar se deve virar dimensionamento/calibração..
7. Ação recomendada: revisar texto.

### Página 42

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: há figura/tabela/quadro; verificar conforme legendas. Tabelas detectadas: 1; imagens detectadas: 0.
4. Legendas detectadas: Quadro 6 - Categorização das pesquisas por área.
5. Termos antigos/atenção: otimização.
6. Problemas observados: termo "otimização" aparece fora de contexto claramente bibliográfico; verificar se deve virar dimensionamento/calibração..
7. Ação recomendada: revisar texto.

### Página 43

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: há figura/tabela/quadro; verificar conforme legendas. Tabelas detectadas: 1; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 44

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: há figura/tabela/quadro; verificar conforme legendas. Tabelas detectadas: 1; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 45

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: há figura/tabela/quadro; verificar conforme legendas. Tabelas detectadas: 2; imagens detectadas: 0.
4. Legendas detectadas: Quadro 7 - Concentração de estudos por área..
5. Termos antigos/atenção: otimização.
6. Problemas observados: termo "otimização" aparece fora de contexto claramente bibliográfico; verificar se deve virar dimensionamento/calibração..
7. Ação recomendada: revisar texto.

### Página 46

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: otimização.
6. Problemas observados: termo "otimização" aparece fora de contexto claramente bibliográfico; verificar se deve virar dimensionamento/calibração..
7. Ação recomendada: revisar texto.

### Página 47

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: elementos presentes, sem contradição automática detectada. Tabelas detectadas: 0; imagens detectadas: 2.
4. Legendas detectadas: Figura 7 - Ano de publicações das 29 publicações., Figura 8 - Número de publicações por país..
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 48

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: há figura/tabela/quadro; verificar conforme legendas. Tabelas detectadas: 1; imagens detectadas: 0.
4. Legendas detectadas: Quadro 8 - Contribuições, Aplicações e limitações dos artigos.
5. Termos antigos/atenção: otimização.
6. Problemas observados: termo "otimização" aparece fora de contexto claramente bibliográfico; verificar se deve virar dimensionamento/calibração..
7. Ação recomendada: revisar texto.

### Página 49

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: há figura/tabela/quadro; verificar conforme legendas. Tabelas detectadas: 1; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: otimização.
6. Problemas observados: termo "otimização" aparece fora de contexto claramente bibliográfico; verificar se deve virar dimensionamento/calibração..
7. Ação recomendada: revisar texto.

### Página 50

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: há figura/tabela/quadro; verificar conforme legendas. Tabelas detectadas: 1; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 51

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: há figura/tabela/quadro; verificar conforme legendas. Tabelas detectadas: 1; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: otimização.
6. Problemas observados: termo "otimização" aparece fora de contexto claramente bibliográfico; verificar se deve virar dimensionamento/calibração..
7. Ação recomendada: revisar texto.

### Página 52

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: há figura/tabela/quadro; verificar conforme legendas. Tabelas detectadas: 1; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: otimização.
6. Problemas observados: termo "otimização" aparece fora de contexto claramente bibliográfico; verificar se deve virar dimensionamento/calibração..
7. Ação recomendada: revisar texto.

### Página 53

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: otimização.
6. Problemas observados: termo "otimização" aparece fora de contexto claramente bibliográfico; verificar se deve virar dimensionamento/calibração..
7. Ação recomendada: revisar texto.

### Página 54

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: otimização.
6. Problemas observados: termo "otimização" aparece fora de contexto claramente bibliográfico; verificar se deve virar dimensionamento/calibração..
7. Ação recomendada: revisar texto.

### Página 55

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: há figura/tabela/quadro; verificar conforme legendas. Tabelas detectadas: 0; imagens detectadas: 2.
4. Legendas detectadas: Figura 9A - Framework proposto simplificado, Figura 10B - Framework proposto detalhado.
5. Termos antigos/atenção: otimização.
6. Problemas observados: termo "otimização" aparece fora de contexto claramente bibliográfico; verificar se deve virar dimensionamento/calibração..
7. Ação recomendada: revisar texto.

### Página 56

1. Texto azul: sim.
2. Coerência do azul: coerente com a modelagem revisada, desde que mantido como complemento exploratório.
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: otimização.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 57

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 58

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 59

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 60

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 61

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 62

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 63

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 64

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 65

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 66

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: otimização.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 67

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 68

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 69

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 70

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: otimização.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 71

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 72

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: há figura/tabela/quadro; verificar conforme legendas. Tabelas detectadas: 0; imagens detectadas: 1.
4. Legendas detectadas: Figura 11 - Equações LSTM.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: figura antiga/exploratória exige conferência: Figura 11 - Equações LSTM.
7. Ação recomendada: revisar texto.

### Página 73

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 74

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 75

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 76

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 77

1. Texto azul: sim.
2. Coerência do azul: coerente com a modelagem revisada, desde que mantido como complemento exploratório.
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 78

1. Texto azul: sim.
2. Coerência do azul: coerente com a modelagem revisada, desde que mantido como complemento exploratório.
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: Peso Faturado.
6. Problemas observados: termo antigo "Peso Faturado" aparece; avaliar troca por volume expedido total em toneladas ou rotular como legado..
7. Ação recomendada: revisar texto.

### Página 79

1. Texto azul: sim.
2. Coerência do azul: coerente com a modelagem revisada, desde que mantido como complemento exploratório.
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 80

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: há figura/tabela/quadro; verificar conforme legendas. Tabelas detectadas: 0; imagens detectadas: 1.
4. Legendas detectadas: Figura 12 - Mapa Mental do Estudo.
5. Termos antigos/atenção: Peso Faturado.
6. Problemas observados: termo antigo "Peso Faturado" aparece; avaliar troca por volume expedido total em toneladas ou rotular como legado..
7. Ação recomendada: revisar texto.

### Página 81

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 82

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: elementos presentes, sem contradição automática detectada. Tabelas detectadas: 0; imagens detectadas: 2.
4. Legendas detectadas: Tabela 1 - Descritiva para os pesos faturados de 2022-2023 (em kg), Figura 13 - Linhas para os pesos faturados de 2022-2023.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 83

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: há figura/tabela/quadro; verificar conforme legendas. Tabelas detectadas: 0; imagens detectadas: 1.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 84

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: elementos presentes, sem contradição automática detectada. Tabelas detectadas: 0; imagens detectadas: 2.
4. Legendas detectadas: Figura 14 - Boxplot para os pesos faturados por ano, Figura 15 - Normal Q-Q Plot para os pesos faturados por ano.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 85

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: elementos presentes, sem contradição automática detectada. Tabelas detectadas: 0; imagens detectadas: 2.
4. Legendas detectadas: Figura 16 - Histograma da normalidade para os pesos faturados de 2022-2023, Tabela 2 - Testes de normalidade, estacionariedade, tendência e sazonalidade.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 86

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 87

1. Texto azul: sim.
2. Coerência do azul: coerente com a modelagem revisada, desde que mantido como complemento exploratório.
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: Peso Faturado.
6. Problemas observados: termo antigo "Peso Faturado" aparece; avaliar troca por volume expedido total em toneladas ou rotular como legado..
7. Ação recomendada: revisar texto.

### Página 88

1. Texto azul: sim.
2. Coerência do azul: coerente com a modelagem revisada, desde que mantido como complemento exploratório.
3. Figura/tabela/quadro: há figura/tabela/quadro; verificar conforme legendas. Tabelas detectadas: 0; imagens detectadas: 2.
4. Legendas detectadas: Figura 26 - Rodada exploratória anterior com modelo SARIMA, Figura 17 - Projeção para os pesos faturados de 2024 com modelo Holt-Winters aditivo.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: figura antiga/exploratória exige conferência: Figura 26 - Rodada exploratória anterior com modelo SARIMA; figura antiga/exploratória exige conferência: Figura 17 - Projeção para os pesos faturados de 2024 com modelo Holt-Winters aditivo; bloco de figuras antigas de modelos; imagens podem não representar a modelagem mensal revisada..
7. Ação recomendada: substituir imagem.

### Página 89

1. Texto azul: sim.
2. Coerência do azul: coerente com a modelagem revisada, desde que mantido como complemento exploratório.
3. Figura/tabela/quadro: há figura/tabela/quadro; verificar conforme legendas. Tabelas detectadas: 0; imagens detectadas: 2.
4. Legendas detectadas: Figura 18 - Projeção para os pesos faturados de 2024 com modelo Holt-Winters multiplicativo, Figura 29 - Rodada exploratória anterior com modelo LSTM.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: figura antiga/exploratória exige conferência: Figura 18 - Projeção para os pesos faturados de 2024 com modelo Holt-Winters multiplicativo; figura antiga/exploratória exige conferência: Figura 29 - Rodada exploratória anterior com modelo LSTM; bloco de figuras antigas de modelos; imagens podem não representar a modelagem mensal revisada.; resultados-chave presentes: 20,61% (teste final simples / média móvel 3m); 21,97% (LSTM simples exploratório).
7. Ação recomendada: substituir imagem, revisar texto, manter.

### Página 90

1. Texto azul: sim.
2. Coerência do azul: coerente com a modelagem revisada, desde que mantido como complemento exploratório.
3. Figura/tabela/quadro: há figura/tabela/quadro; verificar conforme legendas. Tabelas detectadas: 0; imagens detectadas: 2.
4. Legendas detectadas: Figura 30 - Rodada exploratória anterior com modelo Prophet, Figura 19 - Projeção o valor real (Observado) X 5 modelos testados.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: figura antiga/exploratória exige conferência: Figura 30 - Rodada exploratória anterior com modelo Prophet; figura antiga/exploratória exige conferência: Figura 19 - Projeção o valor real (Observado) X 5 modelos testados; bloco de figuras antigas de modelos; imagens podem não representar a modelagem mensal revisada.; resultados-chave presentes: 20,61% (teste final simples / média móvel 3m); 18,60% (Prophet exploratório).
7. Ação recomendada: revisar texto, substituir imagem, manter.

### Página 91

1. Texto azul: sim.
2. Coerência do azul: coerente com a modelagem revisada, desde que mantido como complemento exploratório.
3. Figura/tabela/quadro: há figura/tabela/quadro; verificar conforme legendas. Tabelas detectadas: 0; imagens detectadas: 2.
4. Legendas detectadas: Tabela 3 - Comparativo dos pesos faturados 2024 - observados e estimados, Tabela 4 - Medidas de erros de previsão.
5. Termos antigos/atenção: otimização.
6. Problemas observados: bloco de figuras antigas de modelos; imagens podem não representar a modelagem mensal revisada.; termo "otimização" aparece fora de contexto claramente bibliográfico; verificar se deve virar dimensionamento/calibração.; resultados-chave presentes: 13,43% (validação interna / naive sazonal 12m); 20,61% (teste final simples / média móvel 3m); 18,60% (Prophet exploratório); 21,97% (LSTM simples exploratório).
7. Ação recomendada: substituir imagem, revisar texto, manter.

### Página 92

1. Texto azul: sim.
2. Coerência do azul: provável alteração textual/estrutural; revisar visualmente no Word.
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 93

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: elementos presentes, sem contradição automática detectada. Tabelas detectadas: 0; imagens detectadas: 1.
4. Legendas detectadas: Figura 24 - Parte da tabela dados_estoque, demonstrando a modificação da posição dos dados e nomes das colunas., Figura 20 - Parte da tabela dados_estoque, demonstrando a modificação da posição dos dados e nomes das colunas..
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 94

1. Texto azul: sim.
2. Coerência do azul: coerente com a modelagem revisada, desde que mantido como complemento exploratório.
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: Peso Faturado.
6. Problemas observados: termo antigo "Peso Faturado" aparece; avaliar troca por volume expedido total em toneladas ou rotular como legado..
7. Ação recomendada: revisar texto.

### Página 95

1. Texto azul: sim.
2. Coerência do azul: provável alteração textual/estrutural; revisar visualmente no Word.
3. Figura/tabela/quadro: há figura/tabela/quadro; verificar conforme legendas. Tabelas detectadas: 0; imagens detectadas: 1.
4. Legendas detectadas: Figura 21 - Modelo de Dimensionamento de estoque com α demanda calculado.
5. Termos antigos/atenção: Peso Faturado.
6. Problemas observados: termo antigo "Peso Faturado" aparece; avaliar troca por volume expedido total em toneladas ou rotular como legado..
7. Ação recomendada: revisar texto.

### Página 96

1. Texto azul: sim.
2. Coerência do azul: provável alteração textual/estrutural; revisar visualmente no Word.
3. Figura/tabela/quadro: há figura/tabela/quadro; verificar conforme legendas. Tabelas detectadas: 0; imagens detectadas: 1.
4. Legendas detectadas: Figura 22 - Modelo de Dimensionamento de estoque com α demanda calculado.
5. Termos antigos/atenção: otimização.
6. Problemas observados: termo "otimização" aparece fora de contexto claramente bibliográfico; verificar se deve virar dimensionamento/calibração..
7. Ação recomendada: revisar texto.

### Página 97

1. Texto azul: sim.
2. Coerência do azul: provável alteração textual/estrutural; revisar visualmente no Word.
3. Figura/tabela/quadro: elementos presentes, sem contradição automática detectada. Tabelas detectadas: 0; imagens detectadas: 2.
4. Legendas detectadas: Figura 35 - Escolha da constante de calibração para o modelo, Figura 23 - Modelo com a constante atualizada (c=0,2).
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 98

1. Texto azul: sim.
2. Coerência do azul: coerente com a modelagem revisada, desde que mantido como complemento exploratório.
3. Figura/tabela/quadro: há figura/tabela/quadro; verificar conforme legendas. Tabelas detectadas: 1; imagens detectadas: 0.
4. Legendas detectadas: Tabela 5 - Parte dos dados relacionados à Família 1.
5. Termos antigos/atenção: Peso Faturado.
6. Problemas observados: termo antigo "Peso Faturado" aparece; avaliar troca por volume expedido total em toneladas ou rotular como legado..
7. Ação recomendada: revisar texto.

### Página 99

1. Texto azul: sim.
2. Coerência do azul: provável alteração textual/estrutural; revisar visualmente no Word.
3. Figura/tabela/quadro: há figura/tabela/quadro; verificar conforme legendas. Tabelas detectadas: 2; imagens detectadas: 0.
4. Legendas detectadas: Tabela 6 - Primeira linha referente aos dados relacionados à Família 1.
5. Termos antigos/atenção: Peso Faturado.
6. Problemas observados: termo antigo "Peso Faturado" aparece; avaliar troca por volume expedido total em toneladas ou rotular como legado..
7. Ação recomendada: revisar texto.

### Página 100

1. Texto azul: sim.
2. Coerência do azul: provável alteração textual/estrutural; revisar visualmente no Word.
3. Figura/tabela/quadro: elementos presentes, sem contradição automática detectada. Tabelas detectadas: 2; imagens detectadas: 0.
4. Legendas detectadas: Tabela 7 - Cálculo do Estoque de Segurança para cada constante, Tabela 8 - Cálculo do Estoque Necessário para cada constante.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 101

1. Texto azul: sim.
2. Coerência do azul: provável alteração textual/estrutural; revisar visualmente no Word.
3. Figura/tabela/quadro: há figura/tabela/quadro; verificar conforme legendas. Tabelas detectadas: 2; imagens detectadas: 0.
4. Legendas detectadas: Tabela 9 - Cálculo do MSE para cada constante, Tabela 10 - Cálculo do MSE e da Penalidade para cada constante.
5. Termos antigos/atenção: Peso Faturado.
6. Problemas observados: termo antigo "Peso Faturado" aparece; avaliar troca por volume expedido total em toneladas ou rotular como legado..
7. Ação recomendada: revisar texto.

### Página 102

1. Texto azul: sim.
2. Coerência do azul: coerente com a modelagem revisada, desde que mantido como complemento exploratório.
3. Figura/tabela/quadro: há figura/tabela/quadro; verificar conforme legendas. Tabelas detectadas: 0; imagens detectadas: 2.
4. Legendas detectadas: Quadro 9 - Parte das informações relacionadas à família 1, Quadro 10 - Parte das informações relacionadas à família 2.
5. Termos antigos/atenção: Peso Faturado.
6. Problemas observados: termo antigo "Peso Faturado" aparece; avaliar troca por volume expedido total em toneladas ou rotular como legado..
7. Ação recomendada: revisar texto.

### Página 103

1. Texto azul: sim.
2. Coerência do azul: coerente com a modelagem revisada, desde que mantido como complemento exploratório.
3. Figura/tabela/quadro: elementos presentes, sem contradição automática detectada. Tabelas detectadas: 0; imagens detectadas: 4.
4. Legendas detectadas: Quadro 11 - Parte das informações relacionadas à família 3, Quadro 12 - Parte das informações relacionadas à família 4, Quadro 13 - Parte das informações relacionadas à família 5, Figura 37 - Análise exploratória por família.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 104

1. Texto azul: sim.
2. Coerência do azul: coerente com a modelagem revisada, desde que mantido como complemento exploratório.
3. Figura/tabela/quadro: elementos presentes, sem contradição automática detectada. Tabelas detectadas: 1; imagens detectadas: 0.
4. Legendas detectadas: Tabela 14 - Análise exploratória de previsão de estoque por família.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 105

1. Texto azul: sim.
2. Coerência do azul: coerente com a modelagem revisada, desde que mantido como complemento exploratório.
3. Figura/tabela/quadro: elementos presentes, sem contradição automática detectada. Tabelas detectadas: 0; imagens detectadas: 2.
4. Legendas detectadas: Figura 38 - Análise exploratória de dimensionamento por família, Figura 39 - Busca em grade para calibrar a constante..
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 106

1. Texto azul: sim.
2. Coerência do azul: coerente com a modelagem revisada, desde que mantido como complemento exploratório.
3. Figura/tabela/quadro: elementos presentes, sem contradição automática detectada. Tabelas detectadas: 0; imagens detectadas: 1.
4. Legendas detectadas: Figura 40 - Modelo de dimensionamento de estoque com constante calibrada.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 107

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 108

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: elementos presentes, sem contradição automática detectada. Tabelas detectadas: 0; imagens detectadas: 1.
4. Legendas detectadas: Figura 24 - Distribuição normal e probabilidade e estoque de segurança.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 109

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 110

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 111

1. Texto azul: sim.
2. Coerência do azul: coerente com a modelagem revisada, desde que mantido como complemento exploratório.
3. Figura/tabela/quadro: elementos presentes, sem contradição automática detectada. Tabelas detectadas: 0; imagens detectadas: 1.
4. Legendas detectadas: Figura 12 - Forma intuitiva de representar a calibração da constante.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 112

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 113

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: elementos presentes, sem contradição automática detectada. Tabelas detectadas: 0; imagens detectadas: 1.
4. Legendas detectadas: Figura 25 - Figura 5 - Gráfico do comportamento da demanda e lead time (1º caso).
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 114

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: elementos presentes, sem contradição automática detectada. Tabelas detectadas: 0; imagens detectadas: 1.
4. Legendas detectadas: Figura 26 - Figura 6 - Gráfico do comportamento da demanda e lead time (2º caso).
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 115

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: elementos presentes, sem contradição automática detectada. Tabelas detectadas: 0; imagens detectadas: 2.
4. Legendas detectadas: Figura 27 - Gráfico do comportamento da demanda e lead time (3º caso), Figura 28 - Gráfico do comportamento da demanda e lead time (4º caso).
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 116

1. Texto azul: sim.
2. Coerência do azul: provável alteração textual/estrutural; revisar visualmente no Word.
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 117

1. Texto azul: sim.
2. Coerência do azul: coerente com a modelagem revisada, desde que mantido como complemento exploratório.
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 118

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 119

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: elementos presentes, sem contradição automática detectada. Tabelas detectadas: 0; imagens detectadas: 1.
4. Legendas detectadas: Figura 29 - Exemplo de Efeito Chicote.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 120

1. Texto azul: sim.
2. Coerência do azul: provável alteração textual/estrutural; revisar visualmente no Word.
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 121

1. Texto azul: sim.
2. Coerência do azul: provável alteração textual/estrutural; revisar visualmente no Word.
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 122

1. Texto azul: sim.
2. Coerência do azul: coerente com a modelagem revisada, desde que mantido como complemento exploratório.
3. Figura/tabela/quadro: há figura/tabela/quadro; verificar conforme legendas. Tabelas detectadas: 1; imagens detectadas: 0.
4. Legendas detectadas: Tabela 11 - Comparação entre o nosso modelo e um modelo clássico utilizando redes neurais artificiais.
5. Termos antigos/atenção: Prophet + variáveis operacionais.
6. Problemas observados: Tabela/comparação antiga ainda menciona Prophet como modelo operacional ou WMAPE incompatível..
7. Ação recomendada: revisar texto.

### Página 123

1. Texto azul: sim.
2. Coerência do azul: coerente com a modelagem revisada, desde que mantido como complemento exploratório.
3. Figura/tabela/quadro: há figura/tabela/quadro; verificar conforme legendas. Tabelas detectadas: 1; imagens detectadas: 0.
4. Legendas detectadas: Tabela 12 - Comparação entre o modelo proposto e um modelo do artigo de Gomes, G. et al.(2023).
5. Termos antigos/atenção: otimização, Prophet + variáveis operacionais, WMAPE de 1,06%.
6. Problemas observados: Tabela/comparação antiga ainda menciona Prophet como modelo operacional ou WMAPE incompatível.; termo "otimização" aparece fora de contexto claramente bibliográfico; verificar se deve virar dimensionamento/calibração..
7. Ação recomendada: revisar texto.

### Página 124

1. Texto azul: sim.
2. Coerência do azul: coerente com a modelagem revisada, desde que mantido como complemento exploratório.
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 125

1. Texto azul: sim.
2. Coerência do azul: coerente com a modelagem revisada, desde que mantido como complemento exploratório.
3. Figura/tabela/quadro: há figura/tabela/quadro; verificar conforme legendas. Tabelas detectadas: 1; imagens detectadas: 0.
4. Legendas detectadas: Tabela 15 - Resultados do teste exploratório Prophet/LSTM no recorte de 2025.
5. Termos antigos/atenção: R² igual a 1,0000, R².
6. Problemas observados: figura antiga/exploratória exige conferência: Tabela 15 - Resultados do teste exploratório Prophet/LSTM no recorte de 2025; Tabela Prophet/LSTM presente; conferir lista de tabelas e numeração.; R² / Quadro 14 pode induzir interpretação antiga de ajuste perfeito.; resultados-chave presentes: 13,43% (validação interna / naive sazonal 12m); 20,61% (teste final simples / média móvel 3m); 18,60% (Prophet exploratório); 21,97% (LSTM simples exploratório).
7. Ação recomendada: revisar texto, manter.

### Página 126

1. Texto azul: sim.
2. Coerência do azul: coerente com a modelagem revisada, desde que mantido como complemento exploratório.
3. Figura/tabela/quadro: há figura/tabela/quadro; verificar conforme legendas. Tabelas detectadas: 1; imagens detectadas: 0.
4. Legendas detectadas: Quadro 14 - Algumas métricas do modelo proposto.
5. Termos antigos/atenção: R².
6. Problemas observados: R² / Quadro 14 pode induzir interpretação antiga de ajuste perfeito..
7. Ação recomendada: revisar texto.

### Página 127

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: elementos presentes, sem contradição automática detectada. Tabelas detectadas: 0; imagens detectadas: 1.
4. Legendas detectadas: Figura 30 - Gráfico da Curva ABC.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 128

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: elementos presentes, sem contradição automática detectada. Tabelas detectadas: 0; imagens detectadas: 1.
4. Legendas detectadas: Figura 31 - Metodologia CRISP-DM.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 129

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: elementos presentes, sem contradição automática detectada. Tabelas detectadas: 0; imagens detectadas: 1.
4. Legendas detectadas: Figura 32 - Exemplos de séries temporais.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 130

1. Texto azul: sim.
2. Coerência do azul: coerente com a modelagem revisada, desde que mantido como complemento exploratório.
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: Peso Faturado.
6. Problemas observados: termo antigo "Peso Faturado" aparece; avaliar troca por volume expedido total em toneladas ou rotular como legado.; resultados-chave presentes: 18,60% (Prophet exploratório); 21,97% (LSTM simples exploratório).
7. Ação recomendada: revisar texto, manter.

### Página 131

1. Texto azul: sim.
2. Coerência do azul: coerente com a modelagem revisada, desde que mantido como complemento exploratório.
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: Peso Faturado.
6. Problemas observados: termo antigo "Peso Faturado" aparece; avaliar troca por volume expedido total em toneladas ou rotular como legado.; resultados-chave presentes: 18,60% (Prophet exploratório); 21,97% (LSTM simples exploratório).
7. Ação recomendada: revisar texto, manter.

### Página 132

1. Texto azul: sim.
2. Coerência do azul: coerente com a modelagem revisada, desde que mantido como complemento exploratório.
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: Peso Faturado.
6. Problemas observados: termo antigo "Peso Faturado" aparece; avaliar troca por volume expedido total em toneladas ou rotular como legado..
7. Ação recomendada: revisar texto.

### Página 133

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 134

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: otimização.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 135

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 136

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 137

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 138

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

### Página 139

1. Texto azul: não.
2. Coerência do azul: sem texto azul
3. Figura/tabela/quadro: não há figura/tabela/quadro detectado. Tabelas detectadas: 0; imagens detectadas: 0.
4. Legendas detectadas: nenhuma.
5. Termos antigos/atenção: nenhum termo crítico automático.
6. Problemas observados: nenhum problema automático relevante.
7. Ação recomendada: manter.

## Recomendações de novas imagens

1. **Gráfico da série mensal 2021-2025**: recomendado. Substitui parte da dependência de gráficos antigos de peso faturado e mostra claramente a base mensal revisada.
2. **Gráfico observado x previsto em 2025**: recomendado. Deve comparar o observado de 2025 com o melhor modelo simples e, se desejado, Prophet/LSTM como linhas exploratórias.
3. **Gráfico de barras WMAPE comparando média móvel, Prophet e LSTM**: altamente recomendado. Ajuda a comunicar que Prophet superou o benchmark no teste exploratório e LSTM não superou.
4. **Fluxo atualizado do framework**: altamente recomendado. Deve mostrar leitura da base, agregação mensal, validação temporal, teste final, modelos simples como eixo principal, Prophet/LSTM como teste exploratório e dimensionamento por nível de serviço.

## Conclusão da auditoria

O documento está estruturalmente legível, mas ainda possui elementos visuais e tabelas antigas que podem confundir a banca se não forem claramente atualizados ou rotulados como exploração anterior. A prioridade é corrigir listas automáticas, substituir/atualizar figuras antigas da modelagem, revisar o Quadro 14 e inserir gráficos novos da modelagem revisada.
