# Nota tecnica de ajuste metodologico da modelagem

## Diagnostico

A revisao recebida nao pede apenas nova execucao dos modelos. Ela questiona a coerencia do desenho experimental, a quantidade de dados, a selecao dos modelos, a validacao, os parametros usados e a conexao entre previsao de demanda e dimensionamento de estoque.

O script original tem fragilidades importantes:

- O Prophet e ajustado com a serie completa antes de extrair a previsao do periodo de teste. Isso gera vazamento de informacao e invalida a comparacao treino/teste.
- A tese menciona 24 amostras mensais, mas a planilha entregue contem 1.826 observacoes diarias entre 2021-01-01 e 2025-12-31. Ao agregar mensalmente, ha 60 observacoes mensais.
- A base tem demanda expedida e estoque por familia, mas o script usa um estoque digitado manualmente de 24 meses, desconectado da planilha principal.
- Nao fica claro qual horizonte esta sendo previsto. O script mistura previsao para teste, grafico e calculo de estoque.
- A modelagem de estoque usa demanda real em etapas em que deveria usar demanda prevista, o que pode inflar artificialmente o desempenho.
- A busca por constante e descrita como "otimizacao", mas nao ha formulacao formal de funcao objetivo, restricoes, variaveis de decisao e algoritmo de otimizacao.
- O uso de LSTM/machine learning e metodologicamente fragil para uma serie mensal pequena. Mesmo com 60 meses, o volume de dados ainda e baixo para sustentar rede neural como contribuicao central.

## Encaminhamento recomendado

O caminho mais defensavel e reposicionar a contribuicao da tese como um framework gerencial de apoio a decisao, usando previsao de demanda como insumo. A previsao deve ser apresentada de forma conservadora, transparente e validada temporalmente.

Para a parte de series temporais:

- Usar a base diaria completa e declarar a agregacao mensal.
- Declarar a variavel alvo: volume expedido total em toneladas.
- Separar treino, validacao interna por janela expansiva e teste final.
- Declarar horizonte de previsao, por exemplo 1 mes a frente.
- Comparar modelos simples e interpretaveis: naive, naive sazonal, media movel, suavizacao exponencial e Holt.
- Manter Prophet ou SARIMA apenas se forem treinados sem vazamento e comparados sob o mesmo protocolo.
- Remover LSTM da proposta principal ou deslocar para limitacoes/trabalhos futuros.
- Usar MAE, RMSE, WMAPE e vies percentual. Evitar conclusoes de acuracia perfeita ou R2 igual a 100%.

Para a parte de estoque:

- Tratar estoque como dimensionamento por nivel de servico, nao como otimizacao.
- Calcular demanda no lead time a partir da previsao.
- Calcular estoque de seguranca com base no erro historico de previsao validado fora da amostra.
- Explicitar o nivel de servico e o valor de Z.
- Separar claramente cobertura observada estoque/demanda de lead time operacional real.
- Se nao houver lead time real na base, assumir um valor e declarar como parametro de cenario.

## Formula operacional sugerida

Para demanda mensal prevista `D_hat`, erro historico de previsao `sigma_e`, lead time em meses `L` e nivel de servico associado a `Z`:

```text
demanda_no_lead_time = D_hat * L
estoque_seguranca = Z * sigma_e * sqrt(L)
estoque_necessario = demanda_no_lead_time + estoque_seguranca
```

Se houver dados reais de variabilidade do lead time, pode-se evoluir para:

```text
estoque_seguranca = Z * sqrt(L * sigma_demanda^2 + media_demanda^2 * sigma_lead_time^2)
```

Mas essa segunda formula so deve ser usada se a tese tiver dados reais de lead time.

## Ajuste textual sugerido

Substituir expressoes como "modelo otimizado" por:

- "dimensionamento de estoque por nivel de servico";
- "calibracao do fator de seguranca";
- "parametrizacao do estoque de seguranca";
- "avaliacao de cenarios de cobertura".

Uma redacao defensavel seria:

> O framework proposto integra a previsao de demanda ao dimensionamento de estoque por nivel de servico. A previsao mensal e obtida por modelos de series temporais avaliados em validacao temporal fora da amostra. O estoque de seguranca e entao calculado a partir da incerteza empirica da previsao, do nivel de servico definido e do lead time assumido. Assim, o modelo nao busca determinar um otimo global, mas oferecer uma regra transparente e parametrizavel para apoio a decisao gerencial.

## Arquivo tecnico gerado

Foi criado o script `modelagem_revisada_reinaldo.py`, que executa uma versao conservadora e reproduzivel da modelagem sem sobrescrever o script original.
