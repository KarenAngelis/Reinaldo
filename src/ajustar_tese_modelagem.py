"""
Gera uma copia ajustada da tese com base nos resultados reais da modelagem.

Importante:
- o arquivo original nao e sobrescrito;
- os estilos de paragrafo do DOCX sao mantidos;
- as alteracoes ficam restritas aos trechos metodologicos ligados a previsao,
  validacao, estoque e uso do termo "otimizacao".
"""

from __future__ import annotations

from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from docx import Document
from lxml import etree


PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_DOCX = PROJECT_ROOT / "docs" / "Tese_Reinaldo_T_Ribeiro_19fev (1).docx"
OUTPUT_DOCX = PROJECT_ROOT / "docs" / "Tese_Reinaldo_T_Ribeiro_ajustada_modelagem.docx"


REPLACEMENTS = {
    "A previsão de demanda e o dimensionamento de estoques são aspectos fundamentais para a eficiência operacional das empresas": (
        "A previsão de demanda e o dimensionamento de estoques são aspectos fundamentais para a eficiência operacional das empresas, "
        "especialmente em setores com alta variabilidade e necessidade de resposta rápida às flutuações do mercado. Este trabalho propõe "
        "um framework integrado para apoiar a previsão de demanda e o dimensionamento de estoques com base em séries temporais, com foco "
        "em transparência metodológica e apoio à decisão gerencial. A aplicação empírica utilizou a base diária disponível, agregada em "
        "60 observações mensais, e avaliou modelos simples e interpretáveis por meio de validação temporal e teste final. Os resultados "
        "indicam que a previsão deve ser utilizada com cautela, pois o desempenho variou entre a validação interna e o teste final. A "
        "integração com o estoque foi tratada como dimensionamento por nível de serviço, utilizando demanda prevista, erro histórico de "
        "previsão e estoque de segurança, sem caracterizar uma otimização matemática formal. Dessa forma, o framework contribui como uma "
        "estrutura prática de apoio à decisão para empresas que buscam organizar a relação entre previsão de demanda, incerteza e níveis "
        "de estoque."
    ),
    "Palavras-chave: Previsão de demanda, dimensionamento de estoques, séries temporais, otimização da cadeia de suprimentos.": (
        "Palavras-chave: Previsão de demanda, dimensionamento de estoques, séries temporais, nível de serviço, apoio à decisão."
    ),
    "A proposta deste trabalho é desenvolver um modelo de previsão de demanda e dimensionamento de estoque baseado em séries temporais": (
        "A proposta deste trabalho é desenvolver um framework de previsão de demanda e dimensionamento de estoque baseado em séries temporais, "
        "com o objetivo de apoiar a tomada de decisão no setor frigorífico. A integração entre previsão e estoque não é tratada como um "
        "processo de otimização matemática, mas como uma forma estruturada de transformar previsões, erros e parâmetros operacionais em "
        "estimativas de estoque necessário e estoque de segurança. Esse processo é essencial para que empresas do setor possam analisar o "
        "equilíbrio entre oferta e demanda, evitando tanto o excesso quanto a falta de produtos no estoque (HEIZER; RENDER; MUNSON, 2016; "
        "BARROS; CORTEZ; CARVALHO, 2021)."
    ),
    "A previsão de demanda baseada em séries temporais é capaz de suportar e otimizar o dimensionamento de estoques": (
        "A previsão de demanda baseada em séries temporais pode apoiar o dimensionamento de estoques quando seus limites são explicitados e "
        "quando a avaliação é feita fora da amostra. A precisão das previsões de demanda é relevante para estimar níveis de estoque, mas "
        "não deve ser interpretada isoladamente como garantia de desempenho operacional. Ao aplicar modelos de séries temporais, é possível "
        "estimar tendências, sazonalidades e variações recentes da demanda. Essas informações podem alimentar o cálculo do estoque necessário "
        "e do estoque de segurança, desde que associadas ao erro histórico de previsão e ao nível de serviço adotado."
    ),
    "O objetivo geral desta pesquisa é desenvolver um framework integrado para previsão de demanda e dimensionamento de estoques": (
        "O objetivo geral desta pesquisa é desenvolver um framework integrado para previsão de demanda e dimensionamento de estoques, com base "
        "em modelos de séries temporais, visando apoiar a gestão de estoques. A partir deste objetivo principal, foram delineados os seguintes "
        "objetivos específicos:"
    ),
    "Desenvolver uma estrutura conceitual para a construção do framework de previsão de demanda e dimensionamento de estoques, que selecione técnicas de séries temporais como SARIMA, LSTM, Prophet e Holt-Winters.": (
        "Desenvolver uma estrutura conceitual para a construção do framework de previsão de demanda e dimensionamento de estoques, considerando "
        "técnicas de séries temporais descritas na literatura e priorizando, na aplicação empírica, modelos compatíveis com o volume de dados "
        "disponível. A estrutura será construída com base nos conceitos revisados e nas lacunas identificadas na literatura;"
    ),
    "No terceiro módulo (previsão de demanda), aplicam-se métodos estatísticos e computacionais capazes de capturar diferentes padrões da série temporal.": (
        "No terceiro módulo (previsão de demanda), aplicam-se métodos de séries temporais capazes de capturar padrões da série observada, com "
        "ênfase em modelos simples, interpretáveis e compatíveis com a quantidade de dados disponível. Na aplicação empírica revisada, foram "
        "comparados modelo ingênuo, modelo ingênuo sazonal de 12 meses, média móvel de 3 meses, drift linear, suavização exponencial simples "
        "e Holt com tendência. A escolha do modelo foi orientada por métricas de desempenho calculadas em validação temporal e teste final, "
        "com destaque para MAE, RMSE, WMAPE e viés percentual."
    ),
    "O quarto módulo (dimensionamento de estoque) integra os resultados da previsão com fórmulas clássicas e ajustes otimizados": (
        "O quarto módulo (dimensionamento de estoque) integra os resultados da previsão com fórmulas de estoque de segurança e estoque necessário, "
        "considerando demanda prevista, erro histórico de previsão, nível de serviço e lead time assumido. Essa etapa não caracteriza uma "
        "otimização matemática formal, mas uma parametrização operacional voltada ao apoio à decisão, permitindo avaliar a relação entre risco "
        "de ruptura e necessidade de cobertura de estoque (WANKE, 2011; HEIZER; RENDER; MUNSON, 2016)."
    ),
    ". Os dados utilizados correspondem ao histórico de peso faturado mensal de um item estratégico": (
        "Os dados utilizados correspondem ao histórico diário de volume expedido e estoque por família de produto, coletado entre 2021 e 2025. "
        "Para a modelagem de previsão, a base diária foi agregada em frequência mensal, resultando em 60 observações mensais. A variável alvo "
        "foi o volume expedido total em toneladas. A avaliação de desempenho dos modelos foi realizada por meio de métricas amplamente reconhecidas: "
        "Erro Absoluto Médio (MAE), Raiz do Erro Quadrático Médio (RMSE), WMAPE e viés percentual. O desenho experimental adotou validação temporal "
        "com janela expansiva e teste final nos últimos 12 meses, com horizonte de previsão de um mês à frente. No dimensionamento de estoques, foram "
        "considerados a demanda prevista, o erro empírico de previsão, o nível de serviço e um lead time assumido como parâmetro de cenário. Assim, "
        "os recursos e métodos empregados integram previsão de demanda e gestão de estoques em um framework de apoio à decisão aplicável a itens "
        "perecíveis de alto valor agregado."
    ),
    "No Capítulo 3 – Aplicação do Framework, são detalhados os dados utilizados no estudo": (
        "No Capítulo 3 – Aplicação do Framework, são detalhados os dados utilizados no estudo, o processo de agregação mensal da base diária, a "
        "validação temporal dos modelos de previsão e a comparação dos resultados por métricas de erro. Apresenta-se ainda a metodologia de "
        "dimensionamento de estoques por nível de serviço, bem como a forma de integração entre previsão, incerteza e estoque de segurança."
    ),
    "Embora diversos métodos de previsão de séries temporais tenham sido apresentados nas subseções anteriores": (
        "Embora diversos métodos de previsão de séries temporais tenham sido apresentados nas subseções anteriores, a aplicação empírica revisada "
        "concentrou-se em modelos compatíveis com o tamanho da série mensal disponível: modelo ingênuo, modelo ingênuo sazonal de 12 meses, média "
        "móvel de 3 meses, drift linear, suavização exponencial simples e Holt com tendência."
    ),
    "O modelo SARIMA foi selecionado por sua robustez no tratamento de séries com sazonalidade bem definida": (
        "Modelos como SARIMA, Prophet e LSTM permanecem relevantes no referencial teórico, pois aparecem com frequência na literatura de previsão "
        "de demanda. Entretanto, para a aplicação empírica desta pesquisa, optou-se por priorizar modelos mais simples e interpretáveis, em razão "
        "do volume de dados disponível após a agregação mensal. Essa decisão reduz o risco de superajuste e torna mais transparente a ligação entre "
        "previsão, erro e dimensionamento de estoque."
    ),
    "Todos os modelos foram implementados e comparados com base em métricas de desempenho amplamente utilizadas na literatura": (
        "Os modelos foram comparados com base em métricas de desempenho amplamente utilizadas na literatura, incluindo MAE, RMSE, WMAPE e viés "
        "percentual. O modelo selecionado para alimentar o módulo de dimensionamento de estoques foi definido pelo desempenho na validação temporal, "
        "sem utilizar o teste final como critério de escolha."
    ),
    "Para a projeção dos pesos faturados de 2024, foram aplicados diferentes modelos de séries temporais": (
        "Para a projeção do volume expedido mensal, a aplicação revisada utilizou a base diária agregada em 60 observações mensais, referentes ao "
        "período de janeiro de 2021 a dezembro de 2025. O desenho experimental separou os últimos 12 meses para teste final e utilizou validação "
        "temporal com janela expansiva, preservando a ordem cronológica dos dados. O horizonte avaliado foi de um mês à frente. Foram comparados "
        "modelos simples e interpretáveis: ingênuo do último mês, ingênuo sazonal de 12 meses, média móvel de 3 meses, drift linear, suavização "
        "exponencial simples e Holt com tendência. Essa escolha foi adotada porque a série mensal, embora mais ampla do que a versão inicial do "
        "experimento, ainda é pequena para sustentar conclusões robustas com redes neurais ou modelos altamente parametrizados."
    ),
    "A Figura 26 apresenta as previsões geradas pelo modelo SARIMA": (
        "A Figura 26 registra uma rodada exploratória anterior com o modelo SARIMA. Na versão revisada da aplicação, esse resultado não foi utilizado "
        "como critério principal de seleção do modelo, pois a comparação metodologicamente adotada passou a considerar validação temporal, teste final "
        "e modelos compatíveis com o tamanho efetivo da série mensal."
    ),
    "A Figura 29 apresenta as previsões geradas pelo modelo LSTM": (
        "A Figura 29 registra uma rodada exploratória anterior com LSTM. Considerando a quantidade limitada de observações mensais disponível, o uso "
        "de redes neurais foi tratado com cautela e não foi mantido como sustentação principal do framework empírico."
    ),
    "A Figura 30 apresenta as previsões obtidas com o modelo Prophet": (
        "A Figura 30 registra uma rodada exploratória anterior com Prophet. Embora o modelo seja relevante na literatura e útil em diversos contextos "
        "empresariais, os testes revisados indicaram a necessidade de comparar seu uso com modelos simples e de evitar conclusões fortes baseadas em "
        "uma série mensal reduzida."
    ),
    "Analisando os resultados juntos com os erros, podemos concluir que o melhor método de previsão identificado foi o Prophet": (
        "Na validação temporal revisada, o menor WMAPE foi obtido pelo modelo ingênuo sazonal de 12 meses, com WMAPE de 13,43%. No teste final, que "
        "considerou os últimos 12 meses da série, a média móvel de 3 meses apresentou o menor WMAPE, com 20,61%. Essa diferença entre validação e teste "
        "indica que os resultados devem ser interpretados com cautela e que a contribuição principal do framework está na integração transparente entre "
        "previsão, incerteza e dimensionamento de estoque, e não na superioridade absoluta de um único modelo preditivo."
    ),
    "O modelo de Dimensionamento de Estoque será otimizado por meio de uma abordagem integrada": (
        "O modelo de dimensionamento de estoque foi estruturado por meio de uma abordagem integrada, combinando a previsão de demanda selecionada na "
        "validação temporal com parâmetros operacionais de estoque. A integração considera a demanda prevista, o erro histórico de previsão e o nível "
        "de serviço desejado. Assim, o procedimento é tratado como dimensionamento por nível de serviço, e não como otimização matemática formal."
    ),
    "A introdução dessa variável possibilita a estimativa do tempo necessário para repor o estoque": (
        "A relação entre estoque médio e demanda mensal foi utilizada como indicador de cobertura observada. Essa medida auxilia a leitura gerencial "
        "da disponibilidade de estoque, mas não deve ser confundida com o lead time operacional real de reposição. Na ausência de dados observados de "
        "lead time, o tempo de reposição deve ser tratado como parâmetro de cenário."
    ),
    "3.4 OTIMIZAÇÃO": "3.4 DIMENSIONAMENTO DE ESTOQUES POR NÍVEL DE SERVIÇO",
    "O modelo de previsão Prophet já foi treinado e apresentou o melhor desempenho entre os demais": (
        "Na versão revisada, o modelo utilizado no dimensionamento de estoque é aquele selecionado pela validação temporal. O estoque necessário é "
        "calculado a partir da demanda prevista no período de análise, acrescida de um estoque de segurança baseado no erro histórico de previsão, "
        "no nível de serviço de 95% e no lead time assumido de 1 mês."
    ),
    "3.4.2 Otimização da Constante": "3.4.2 Calibração do Fator de Segurança",
    "No gráfico da Figura acima, a linha azul representa a demanda real": (
        "No gráfico da Figura acima, a linha azul representa a demanda real observada. A linha de previsão deve ser interpretada como estimativa de "
        "demanda sujeita a erro, e não como valor definitivo. O estoque necessário é calculado pela soma entre a demanda prevista no lead time e o "
        "estoque de segurança. O estoque de segurança, por sua vez, representa uma reserva para cobrir variações de demanda e incertezas de previsão."
    ),
    "3.4.3.1 Resumo das Etapas de Otimização": "3.4.3.1 Resumo das Etapas de Dimensionamento",
    "Os dados abrangem o período de janeiro de 2020 até dezembro de 2025": (
        "Os dados utilizados na versão revisada abrangem o período de janeiro de 2021 a dezembro de 2025. A base original é diária e foi agregada em "
        "60 observações mensais para a modelagem de demanda. Os últimos 12 meses foram reservados para teste final, enquanto a etapa de validação "
        "temporal utilizou janela expansiva com mínimo de 36 meses de treinamento."
    ),
    "Em relação à organização dos dados, os valores até o ano de 2023 são utilizados para treinar o modelo Prophet": (
        "Em relação à organização dos dados, a aplicação revisada utilizou validação temporal com janela expansiva e teste final nos últimos 12 meses. "
        "Esse procedimento evita treinar o modelo com dados do próprio período que será avaliado e reduz o risco de vazamento de informação."
    ),
    "Através dos valores de predição do modelo Prophet": (
        "A leitura dos valores previstos deve considerar que se trata de estimativas sujeitas a erro. Por isso, os resultados foram avaliados com "
        "métricas fora da amostra e utilizados no estoque apenas em conjunto com o erro histórico de previsão."
    ),
    "Inicialmente, aplicou-se a fórmula clássica de dimensionamento de estoque sem atualizar a constante de segurança": (
        "Inicialmente, aplicou-se a fórmula clássica de dimensionamento de estoque com parâmetros explícitos de nível de serviço e lead time. Observou-se "
        "que a escolha desses parâmetros afeta diretamente o estoque de segurança e, consequentemente, o estoque necessário total."
    ),
    "A curva de erro da Figura 37 confirma que o modelo é sensível à escolha da constante": (
        "A curva de erro da Figura 37 confirma que o modelo é sensível à escolha da constante. Assim, a constante deve ser interpretada como parâmetro "
        "de calibração e cenário, e não como resultado ótimo em sentido matemático formal."
    ),
    "Seguindo as demais análises de dimensionamento de estoque": (
        "Seguindo as demais análises de dimensionamento de estoque, os gráficos apresentam comportamento semelhante e reforçam a sensibilidade do "
        "estoque necessário aos parâmetros escolhidos."
    ),
    "O modelo de dimensionamento de estoque, aprimorado com a otimização da constante de segurança": (
        "O modelo de dimensionamento de estoque, ajustado por parâmetros de segurança e nível de serviço, mostrou-se útil para organizar a relação entre "
        "demanda prevista, incerteza e estoque necessário. Os resultados devem ser interpretados como apoio à decisão e análise de cenários, evitando "
        "a conclusão de que há um ótimo global ou garantia de desempenho perfeito."
    ),
    "3.5.2 Otimização da constante": "3.5.2 Calibração da constante",
    "Com o objetivo de avaliar a precisão e a robustez do modelo proposto de dimensionamento de estoque": (
        "Com o objetivo de avaliar a precisão e a robustez do framework proposto, foram utilizadas métricas consagradas de previsão, como MAE, RMSE, "
        "WMAPE e viés percentual. Na validação interna, o modelo ingênuo sazonal de 12 meses apresentou o menor WMAPE, igual a 13,43%. No teste final, "
        "a média móvel de 3 meses apresentou o menor WMAPE, igual a 20,61%. Essas métricas permitem avaliar a qualidade da previsão fora da amostra e "
        "servem como base para dimensionar o estoque de segurança."
    ),
    "A avaliação do modelo de dimensionamento de estoque proposto, após a otimização da constante de segurança": (
        "A avaliação revisada não sustenta a conclusão de erro próximo de zero no dimensionamento de estoque. O desempenho observado indica que há erro "
        "relevante de previsão, especialmente no teste final, e que esse erro deve ser incorporado ao estoque de segurança. Assim, o resultado mais "
        "adequado é interpretar o framework como ferramenta de apoio à decisão, e não como modelo de precisão perfeita."
    ),
    "O valor de R² obtido foi igual a 1,0000": (
        "O uso de R² igual a 1,0000 não foi mantido como evidência de desempenho, pois esse resultado decorre da própria forma de construção da meta "
        "operacional e pode induzir interpretação de ajuste perfeito. Na versão revisada, a avaliação prioriza métricas fora da amostra, especialmente "
        "WMAPE, MAE, RMSE e viés percentual, por serem mais adequadas para comparar previsões de demanda."
    ),
    "A análise das métricas de desempenho do modelo proposto evidenciou sua robustez": (
        "A análise das métricas de desempenho mostra que o framework é útil para organizar a decisão de estoque, mas deve ser interpretado com cautela. "
        "A diferença entre o melhor modelo na validação interna e o melhor modelo no teste final indica sensibilidade da série e reforça que a previsão "
        "não deve ser apresentada como perfeita. De forma geral, os indicadores sustentam o uso do framework como apoio gerencial para transformar "
        "previsão e incerteza em parâmetros de estoque de segurança e estoque necessário."
    ),
    "No caso dos dados analisados, o modelo SARIMA foi eficaz": (
        "No caso dos dados analisados, os modelos mais complexos descritos no referencial teórico devem ser interpretados como alternativas metodológicas, "
        "mas não como base principal da conclusão empírica revisada. A quantidade de observações mensais disponível recomenda cautela na escolha de modelos "
        "muito parametrizados."
    ),
    "Nos dados analisados, o modelo LSTM conseguiu capturar as tendências gerais": (
        "Nos dados analisados, o uso de LSTM foi considerado metodologicamente frágil para sustentar a proposta principal, devido à quantidade limitada "
        "de observações mensais. Por esse motivo, redes neurais são tratadas como possibilidade para estudos futuros com bases maiores."
    ),
    "Para os dados de \"Peso Faturado\", o modelo Prophet apresentou uma boa performance": (
        "Para os dados analisados, o Prophet foi tratado como alternativa exploratória, mas a versão revisada priorizou a comparação temporal entre modelos "
        "simples e interpretáveis. Os resultados indicaram que nenhum modelo deve ser apresentado como superior de forma absoluta sem considerar o desenho "
        "de validação e o teste final."
    ),
    "A análise realizada neste estudo teve como objetivo avaliar e comparar a performance de diferentes técnicas de séries temporais": (
        "A análise realizada neste estudo teve como objetivo avaliar a integração entre previsão de demanda e dimensionamento de estoques a partir de uma "
        "base histórica agregada mensalmente. A comparação empírica revisada utilizou modelos simples e interpretáveis de séries temporais, avaliados por "
        "validação temporal e teste final, com o objetivo de apoiar decisões de estoque sem superestimar a capacidade preditiva da base disponível."
    ),
    "SARIMA se destacou por sua capacidade de incorporar sazonalidade e tendência": (
        "Modelos como SARIMA, Prophet e LSTM permanecem relevantes como fundamentação teórica, mas os resultados empíricos revisados indicam que, para a "
        "base mensal disponível, a escolha de modelos simples e transparentes é mais defensável metodologicamente."
    ),
    "LSTM, como uma abordagem de redes neurais": (
        "LSTM, como abordagem de redes neurais, exige maior volume de dados para treinamento e validação robusta. Assim, seu uso não foi mantido como eixo "
        "central da aplicação empírica, sendo recomendado apenas para estudos futuros com séries mais longas ou dados de maior frequência."
    ),
    "Prophet mostrou-se um modelo robusto e fácil de usar": (
        "Prophet mostrou-se relevante como alternativa de modelagem, mas os testes revisados não sustentam a conclusão de que ele possui erros muito menores "
        "que todos os demais modelos. A validação temporal apontou melhor desempenho do modelo ingênuo sazonal de 12 meses, enquanto o teste final apontou "
        "melhor desempenho da média móvel de 3 meses."
    ),
    "Para empresas que precisam de previsões rápidas e robustas": (
        "Para empresas que precisam de previsões rápidas e interpretáveis, modelos simples podem ser uma alternativa útil quando a base histórica é limitada. "
        "A escolha do modelo deve considerar o desempenho fora da amostra, a estabilidade entre validação e teste e a facilidade de explicar os resultados "
        "para a tomada de decisão."
    ),
    "Apesar dos resultados obtidos demonstrarem aderência do modelo selecionado": (
        "Apesar de o framework organizar de forma coerente a relação entre previsão de demanda e dimensionamento de estoque, esta pesquisa apresenta limitações "
        "que devem ser consideradas na interpretação dos achados."
    ),
    "Primeiramente, o estudo foi conduzido com base em dados históricos de um único item": (
        "Primeiramente, o estudo foi conduzido com base em dados históricos de uma base específica e em um horizonte temporal limitado, o que restringe a "
        "generalização dos resultados para outros produtos ou períodos com dinâmicas distintas. Além disso, variáveis externas que podem influenciar a demanda, "
        "como preços, promoções, sazonalidades específicas do setor, alterações regulatórias ou eventos extraordinários, não foram explicitamente incorporadas "
        "aos modelos."
    ),
}


REPLACEMENTS.update(
    {
        "Este estudo foca especificamente na previsão de vendas de um produto de alto valor agregado": (
            "Este estudo foca especificamente na previsão de vendas de um produto de alto valor agregado, pertencente a uma categoria de elevada "
            "importância dentro da indústria frigorífica. Itens com essas características demandam planejamento rigoroso, pois apresentam maior "
            "sensibilidade a variações de mercado e perdas podem acarretar impactos financeiros significativos. A escolha do item a ser analisado "
            "seguiu a metodologia de Classificação ABC (BARROS; CORTEZ; CARVALHO, 2021; SILVER; PYKE; PETERSON, 2016), amplamente usada para "
            "categorizar produtos conforme sua importância para a empresa. O item selecionado é classificado como de alta prioridade, justificando "
            "a ênfase em melhorar a previsão de demanda e apoiar o dimensionamento de estoques."
        ),
        "Conforme Ahrens et al. (2021), o nível real de vendas registrado nos dados disponíveis": (
            "Conforme Ahrens et al. (2021), o nível real de vendas registrado nos dados disponíveis pode ser tomado como a demanda efetiva. Assim, "
            "esta pesquisa parte da premissa de que os dados históricos de volume expedido são representativos do comportamento da demanda observada, "
            "desde que adequadamente tratados e avaliados fora da amostra. A utilização desses dados possibilita comparar modelos de previsão e "
            "transformar seus erros em parâmetros para dimensionamento de estoque. Considera-se, ainda, que a previsão de demanda deve estar integrada "
            "ao estoque de segurança, pois previsões imprecisas podem conduzir tanto a excesso de estoque quanto a rupturas. Dessa forma, a premissa "
            "central não é obter previsão perfeita, mas estruturar uma regra transparente de apoio à decisão."
        ),
        "Desta forma, com base no que foi apresentado, a questão problema a ser respondida nesta tese": (
            "Desta forma, com base no que foi apresentado, a questão problema a ser respondida nesta tese é: de que maneira é possível desenvolver "
            "um modelo conceitual integrado de previsão de demanda e dimensionamento de estoques, utilizando séries temporais, para apoiar a gestão "
            "de estoques e reduzir perdas no setor frigorífico, considerando a variabilidade da demanda e as flutuações sazonais?"
        ),
        "A primeira fase é Fase de Contextualização e Fundamentação Teórica": (
            "A primeira fase é a Fase de Contextualização e Fundamentação Teórica. Nesta etapa, foi realizado o levantamento bibliográfico sobre previsão "
            "de demanda, séries temporais e gestão de estoques. A segunda fase é a Fase de Definição do Problema e Objetivos, com formulação do problema "
            "central e dos objetivos da pesquisa. A terceira fase é a Fase de Coleta e Tratamento de Dados, na qual foram organizados dados reais de uma "
            "empresa frigorífica, agregados em frequência mensal para a modelagem. A quarta fase é a Fase de Modelagem e Simulação, com comparação de "
            "modelos de séries temporais por validação temporal. A quinta fase é a Fase de Dimensionamento de Estoques, com cálculo de estoque necessário "
            "e estoque de segurança a partir da previsão, do erro histórico e do nível de serviço. A sexta fase é a Fase de Análise e Discussão dos "
            "Resultados, na qual os achados são interpretados à luz da literatura e de suas limitações."
        ),
        "Como objetivo otimizar o cálculo do estoque em um sistema de gestão de estoques": (
            "Com o objetivo de parametrizar o cálculo do estoque em um sistema de gestão de estoques, foi utilizada uma constante de ajuste associada "
            "ao estoque de segurança. Na versão revisada, esse procedimento é interpretado como calibração de parâmetro e análise de cenário, não como "
            "otimização matemática formal. O estoque necessário deve ser calculado a partir da demanda prevista, do erro histórico de previsão, do nível "
            "de serviço e do lead time assumido. Essa abordagem permite avaliar a necessidade de cobertura adicional sem afirmar a existência de uma "
            "solução ótima global."
        ),
        "Figura 35 - Escolha da melhor constante para otimizar o modelo": (
            "Figura 35 - Escolha da constante de calibração para o modelo"
        ),
        "O gráfico demonstra que o estoque necessário otimizado acompanha de perto a demanda real": (
            "O gráfico demonstra que o estoque necessário acompanha a demanda de referência e mantém uma margem de segurança. Essa leitura deve ser "
            "entendida como análise de cenário, pois utiliza parâmetros definidos no modelo e não comprova desempenho perfeito em operação real."
        ),
        "Para garantir maior precisão no cálculo do estoque de segurança, implementou-se uma abordagem sistemática de otimização": (
            "Para avaliar a sensibilidade do cálculo do estoque de segurança, implementou-se uma abordagem sistemática de calibração da constante de "
            "ajuste c, por meio de busca em grade (grid search). Essa técnica testa diferentes valores de um parâmetro dentro de um intervalo definido, "
            "permitindo observar como o erro se comporta em cada cenário."
        ),
        "O procedimento adotado para encontrar a constante otimizada segue os passos abaixo.": (
            "O procedimento adotado para calibrar a constante segue os passos abaixo."
        ),
        "O erro MSE compara o estoque necessário com 105% da demanda real:": (
            "O erro MSE compara o estoque necessário com uma referência operacional baseada na demanda real. Essa referência é usada apenas como cenário "
            "de calibração e não deve ser interpretada como validação perfeita do modelo:"
        ),
        "De maneira resumida, para definir a melhor constante de ajuste no cálculo do estoque de segurança": (
            "De maneira resumida, para calibrar a constante de ajuste no cálculo do estoque de segurança, aplicou-se uma busca em grade. Foram testados "
            "valores de constante entre 0,0 e 5,0 (com passo 0,1). Para cada constante, foi calculado o erro quadrático médio (MSE) em relação a uma "
            "referência operacional. Além do MSE, foram somados ao erro total uma penalização para constantes muito baixas e um custo por falta de estoque. "
            "A constante escolhida deve ser entendida como parâmetro calibrado para o cenário analisado, e não como ótimo global."
        ),
        "Anteriormente, já foram realizados ajustes nos modelos Prophet e no cálculo do dimensionamento do estoque": (
            "Anteriormente, foram realizados ajustes no cálculo do dimensionamento do estoque. O objetivo agora é aplicar os dados disponíveis ao modelo "
            "revisado, analisando o comportamento das variáveis ao longo do tempo e o impacto dos parâmetros de segurança no estoque necessário."
        ),
        "Para encontrar o valor ideal desta constante, foi realizada uma busca em grade": (
            "Para avaliar a constante, foi realizada uma busca em grade (grid search), comparando o erro médio quadrático (MSE) para diferentes valores "
            "do parâmetro. O resultado está representado na Figura 37. A leitura adequada é que a constante afeta diretamente o estoque de segurança, "
            "devendo ser interpretada como calibração do cenário analisado."
        ),
        "Figura 39 - Busca em grade do gradiente para encontrar a constante otimizada.": (
            "Figura 39 - Busca em grade para calibrar a constante."
        ),
        "Com essa constante otimizada, foi possível gerar a projeção de estoques": (
            "Com essa constante calibrada, foi possível gerar a projeção de estoques ao longo do tempo, apresentada na Figura 38. Nela, é possível "
            "comparar a demanda real, o estoque necessário e o estoque de segurança. O gráfico mostra o efeito do parâmetro sobre a cobertura de estoque, "
            "sem implicar que o resultado seja ótimo em sentido matemático."
        ),
        "Figura 40 - Modelo de dimensionamento de estoque para a constante otimizada": (
            "Figura 40 - Modelo de dimensionamento de estoque com constante calibrada"
        ),
        "Para ajustar o modelo de dimensionamento de estoque, utilizamos uma técnica chamada busca em grade": (
            "Para ajustar o modelo de dimensionamento de estoque, utilizou-se uma técnica chamada busca em grade (grid search). Esse método consiste em "
            "testar sistematicamente diversos valores para um parâmetro, no caso a constante c, com o objetivo de observar qual valor reduz o erro no "
            "cenário analisado. Nesta tese, esse procedimento é tratado como calibração de parâmetro."
        ),
        "A busca em grade, portanto, realiza uma varredura entre diferentes valores possíveis da constante": (
            "A busca em grade, portanto, realiza uma varredura entre diferentes valores possíveis da constante e identifica o menor erro dentro do intervalo "
            "testado. Esse resultado depende do intervalo escolhido, dos dados utilizados e da referência operacional adotada."
        ),
        "Figura 12 - Forma intuitiva de representar a busca pela constante otimizada": (
            "Figura 12 - Forma intuitiva de representar a calibração da constante"
        ),
        "De forma intuitiva, pense na Figura 4 acima.": (
            "De forma intuitiva, pense na Figura 4 acima como uma forma de testar caminhos possíveis. No código, é definido um intervalo de valores para a "
            "constante, e a busca em grade avalia cada possibilidade dentro desse intervalo. Por isso, o resultado deve ser tratado como calibração dentro "
            "do cenário analisado."
        ),
        "A otimização da constante visa minimizar o Erro Quadrático Médio": (
            "A calibração da constante visa reduzir o Erro Quadrático Médio (MSE) dentro do cenário analisado. Isso permite avaliar o equilíbrio entre "
            "erro de previsão, estoque de segurança e risco de falta. Ao calcular o estoque necessário com base na demanda prevista e no estoque de segurança, "
            "a proposta apoia a definição de níveis de serviço, sem afirmar a existência de uma solução ótima global."
        ),
        "O artigo \"Aplicação de Machine Learning e Séries Temporais para Previsão de Demanda": (
            "O artigo \"Aplicação de Machine Learning e Séries Temporais para Previsão de Demanda: Um Estudo de Caso em uma Empresa de Bens de Consumo\" "
            "(GOMES et al., 2023) oferece uma base teórica aplicada para a proposta, especialmente no que diz respeito à relação entre previsão de demanda "
            "e gestão de estoques. A redução do erro médio de previsão, conforme relatado no artigo, evidencia o impacto positivo que métodos científicos "
            "podem ter na gestão de estoques, mas a aplicação desta tese mantém a cautela metodológica em razão do tamanho da série disponível."
        ),
        "A indústria frigorífica é particularmente suscetível ao efeito chicote": (
            "A indústria frigorífica é particularmente suscetível ao efeito chicote devido à perecibilidade dos produtos, à sensibilidade à sazonalidade e "
            "à forte dependência de informações acuradas de demanda. Portanto, modelos de previsão avaliados fora da amostra e estoques de segurança "
            "definidos por parâmetros explícitos contribuem para mitigar esse fenômeno."
        ),
        "O modelo proposto neste trabalho, ao incorporar técnicas modernas de previsão": (
            "O modelo proposto neste trabalho, ao incorporar previsão de demanda e cálculo de estoque de segurança, contribui para a análise dos custos "
            "logísticos totais. Ao reduzir o risco de excesso ou falta de produtos, a empresa pode avaliar melhor desperdícios, custos de armazenagem e "
            "perda de receita por indisponibilidade."
        ),
        "Nesse contexto, o artigo de Zhang, Patuwo e Hu (1998)": (
            "Nesse contexto, o artigo de Zhang, Patuwo e Hu (1998) é uma referência clássica sobre o uso de redes neurais artificiais na previsão de séries "
            "temporais. O estudo é relevante para a fundamentação teórica, pois destaca a capacidade das redes neurais de modelar padrões não lineares. "
            "Entretanto, considerando a base mensal disponível nesta tese, modelos desse tipo devem ser tratados como possibilidade futura e não como eixo "
            "principal da aplicação empírica."
        ),
        "O nosso trabalho, além de otimizar o estoque": (
            "O presente trabalho busca integrar previsão de demanda e dimensionamento de estoque, observando métricas de erro e parâmetros operacionais. "
            "Dessa forma, a contribuição está na estrutura de apoio à decisão e na transparência do processo metodológico."
        ),
        "Este trabalho pode se destacar em relação a este artigo": (
            "Este trabalho contribui ao explicitar a integração entre previsão de demanda, erro histórico de previsão, nível de serviço e estoque de segurança. "
            "Além disso, a visualização dos resultados facilita a leitura gerencial e apoia a tomada de decisão."
        ),
        "Para a série temporal dos pesos faturados de 2022-2023": (
            "Para a série temporal mensal analisada, há diferentes métodos de previsão que podem ser aplicados. Entretanto, como a base mensal disponível "
            "é limitada, a avaliação revisada priorizou modelos simples e interpretáveis, comparados por validação temporal e teste final. Essa escolha "
            "permite apresentar resultados mais cautelosos e metodologicamente coerentes com o tamanho da amostra."
        ),
        "Com base na série temporal estudada, iniciaremos a abordagem com a decomposição": (
            "Com base na série temporal estudada, a abordagem revisada parte da análise do comportamento mensal da demanda e da comparação entre modelos "
            "simples. Modelos mais complexos, como SARIMA, Prophet e redes neurais, permanecem relevantes na literatura, mas não são tratados como sustentação "
            "principal dos resultados empíricos desta versão."
        ),
        "A fórmula do Estoque de Segurança (SS) também foi modificada e adaptada": (
            "A fórmula do Estoque de Segurança (SS) também foi adaptada para explicitar o papel da constante de calibração. Essa constante não melhora a "
            "previsão em si; ela ajusta o nível de proteção do estoque diante do erro de previsão e do tempo de reposição assumido:"
        ),
        "Cada modelo demonstrou características distintas": (
            "Os modelos analisados demonstraram características distintas, mas os resultados revisados indicam que a escolha deve ser feita com base no "
            "desempenho fora da amostra e na capacidade de interpretação."
        ),
        "Holt-Winters Aditivo e Multiplicativo proporcionaram previsões confiáveis": (
            "Modelos de suavização exponencial, como Holt e variações de Holt-Winters, são alternativas úteis para séries com tendência e sazonalidade, "
            "mas também apresentam limitações quando há picos, mudanças estruturais ou poucas observações para validação."
        ),
        "Esta tese contribui para a literatura ao comparar múltiplas técnicas": (
            "Esta tese contribui para a literatura ao propor uma estrutura integrada entre previsão de demanda e dimensionamento de estoque. A contribuição "
            "principal está menos na superioridade de um algoritmo específico e mais na organização do processo decisório: tratar a base, validar previsões "
            "fora da amostra, medir o erro e incorporar essa incerteza ao cálculo do estoque de segurança."
        ),
    }
)


def replace_paragraph_text(paragraph, new_text: str) -> None:
    """Substitui o texto mantendo o estilo do paragrafo."""
    paragraph.text = new_text


def request_field_update_on_open(path: Path) -> None:
    """Pede ao Word para atualizar sumario/listas quando o arquivo for aberto."""
    temp_path = path.with_suffix(".tmp.docx")
    with ZipFile(path, "r") as source:
        settings_xml = source.read("word/settings.xml")
        root = etree.fromstring(settings_xml)
        ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
        update_fields = root.find("w:updateFields", namespaces=ns)
        if update_fields is None:
            update_fields = etree.Element(f"{{{ns['w']}}}updateFields")
            root.append(update_fields)
        update_fields.set(f"{{{ns['w']}}}val", "true")
        updated_settings = etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone=True)

        with ZipFile(temp_path, "w", ZIP_DEFLATED) as target:
            written = set()
            for item in source.infolist():
                if item.filename in written:
                    continue
                written.add(item.filename)
                if item.filename == "word/settings.xml":
                    target.writestr(item, updated_settings)
                else:
                    target.writestr(item, source.read(item.filename))

    temp_path.replace(path)


def main() -> None:
    doc = Document(INPUT_DOCX)
    replacements_done = []

    for paragraph in doc.paragraphs:
        current = " ".join(paragraph.text.split())
        if not current:
            continue
        for key, replacement in REPLACEMENTS.items():
            normalized_key = " ".join(key.split())
            if current == normalized_key or current.startswith(normalized_key):
                replace_paragraph_text(paragraph, replacement)
                replacements_done.append(key[:80])
                break

    doc.save(OUTPUT_DOCX)
    request_field_update_on_open(OUTPUT_DOCX)
    print(f"Arquivo gerado: {OUTPUT_DOCX}")
    print(f"Trechos substituidos: {len(replacements_done)}")
    for item in replacements_done:
        print(f"- {item}")


if __name__ == "__main__":
    main()
