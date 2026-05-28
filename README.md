# Reinaldo

Projeto de apoio a revisao metodologica da tese, com foco em previsao de demanda, validacao temporal de modelos e dimensionamento de estoque.

O projeto gera:

- arquivos `.csv` com os dados tratados, metricas, previsoes e dimensionamento de estoque;
- um painel HTML para apresentar os resultados dos testes;
- uma nota tecnica com recomendacoes metodologicas.

## Repositorio

```text
https://github.com/KarenAngelis/Reinaldo
```

## O que instalar antes

Para clonar e executar o projeto localmente, instale estes programas:

1. Visual Studio Code

   Baixe em: https://code.visualstudio.com/

2. Git

   Baixe em: https://git-scm.com/downloads

3. Python

   Baixe em: https://www.python.org/downloads/

   Durante a instalacao no Windows, marque a opcao:

   ```text
   Add python.exe to PATH
   ```

4. Extensao Python no VS Code

   Depois de instalar o VS Code, abra o programa, va em `Extensions` e instale a extensao:

   ```text
   Python
   ```

   A extensao oficial aparece como `Python`, da Microsoft.

## Como conferir se instalou certo

Abra o PowerShell e rode:

```powershell
git --version
python --version
pip --version
```

Se os tres comandos mostrarem versoes instaladas, o ambiente basico esta pronto.

## Como clonar o projeto

Escolha uma pasta no seu computador para guardar o projeto. Exemplo:

```powershell
cd Desktop
```

Clone o repositorio:

```powershell
git clone https://github.com/KarenAngelis/Reinaldo.git
```

Entre na pasta do projeto:

```powershell
cd Reinaldo
```

Abra no VS Code:

```powershell
code .
```

Se o comando `code .` nao funcionar, abra o VS Code manualmente e use:

```text
File > Open Folder
```

Depois selecione a pasta `Reinaldo`.

## Estrutura do projeto

```text
Reinaldo/
├─ data/
│  └─ base de dados resumida140526 .xlsx
├─ docs/
│  ├─ comentarios_tese_reinaldo.pdf
│  ├─ Tese_Reinaldo_T_Ribeiro_19fev (1).docx
│  └─ nota_tecnica_modelagem_reinaldo.md
├─ notebooks/
│  └─ script_modelos_artigo_tese_Reinaldo (1).ipynb
├─ outputs/
│  ├─ dados_mensais_limpos.csv
│  ├─ dimensionamento_estoque.csv
│  ├─ metricas_teste_final.csv
│  ├─ metricas_validacao_interna.csv
│  ├─ previsoes_teste_final.csv
│  ├─ previsoes_validacao_interna.csv
│  ├─ resumo_metodologico.txt
│  └─ painel_resultados.html
├─ src/
│  ├─ modelagem_revisada_reinaldo.py
│  ├─ gerar_painel_resultados.py
│  └─ script_modelos_artigo_tese_Reinaldo (1).py
├─ requirements.txt
└─ README.md
```

## Como instalar as dependencias

Dentro da pasta do projeto, rode:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Para conferir se as bibliotecas principais estao instaladas:

```powershell
python -c "import pandas, numpy, openpyxl; print('Ambiente OK')"
```

Se aparecer `Ambiente OK`, pode executar os scripts.

## Como rodar a modelagem

Na raiz do projeto, execute:

```powershell
python .\src\modelagem_revisada_reinaldo.py
```

Esse script le a base em:

```text
data/base de dados resumida140526 .xlsx
```

E gera os arquivos em:

```text
outputs/
```

Arquivos principais gerados:

- `outputs/dados_mensais_limpos.csv`
- `outputs/metricas_validacao_interna.csv`
- `outputs/metricas_teste_final.csv`
- `outputs/previsoes_teste_final.csv`
- `outputs/previsoes_validacao_interna.csv`
- `outputs/dimensionamento_estoque.csv`
- `outputs/resumo_metodologico.txt`

## Como gerar o painel HTML

Depois de rodar a modelagem, execute:

```powershell
python .\src\gerar_painel_resultados.py
```

O painel sera criado em:

```text
outputs/painel_resultados.html
```

## Como abrir o painel

No VS Code:

1. Abra a pasta `outputs`.
2. Clique com o botao direito em `painel_resultados.html`.
3. Escolha `Reveal in File Explorer`.
4. Dobre clique no arquivo para abrir no navegador.

Tambem e possivel abrir diretamente pelo caminho:

```text
Reinaldo/outputs/painel_resultados.html
```

## Fluxo completo recomendado

Sempre que quiser atualizar os resultados:

```powershell
python .\src\modelagem_revisada_reinaldo.py
python .\src\gerar_painel_resultados.py
```

Depois abra:

```text
outputs/painel_resultados.html
```

## Como reproduzir os testes em ambiente local

Esta secao descreve o ambiente recomendado para reproduzir todos os testes, incluindo o teste exploratorio com Prophet e LSTM.

O ambiente Python 3.12 e recomendado para os testes com TensorFlow/LSTM. Em especial, foi usado Python 3.12.10 com o ambiente virtual `.venv312`. O Python 3.14 pode nao ser compativel com TensorFlow.

### 1. Instalar Python 3.12 no Windows

Baixe e instale o Python 3.12 pelo site oficial:

```text
https://www.python.org/downloads/windows/
```

De preferencia, use Python 3.12.10 ou outra versao 3.12 com instalador disponivel.

Durante a instalacao, marque a opcao:

```text
Add python.exe to PATH
```

### 2. Confirmar as versoes instaladas

No PowerShell, rode:

```powershell
py -0p
```

Esse comando mostra as versoes de Python instaladas e seus caminhos. Confirme se aparece uma versao `3.12`.

### 3. Criar o ambiente virtual com Python 3.12

Na raiz do projeto, rode:

```powershell
py -3.12 -m venv .venv312
```

### 4. Ativar o ambiente no PowerShell

```powershell
.\.venv312\Scripts\Activate.ps1
```

Se o PowerShell bloquear a ativacao, rode:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv312\Scripts\Activate.ps1
```

### 5. Atualizar o pip

Com o ambiente ativado, rode:

```powershell
python -m pip install --upgrade pip
```

### 6. Instalar as dependencias

```powershell
python -m pip install pandas numpy matplotlib scikit-learn statsmodels openpyxl prophet tensorflow
```

No ambiente usado para o teste exploratorio, o TensorFlow instalado foi:

```text
TensorFlow 2.21.0
```

### 7. Testar se o TensorFlow instalou

```powershell
python -c "import tensorflow as tf; print(tf.__version__)"
```

Se aparecer `2.21.0` ou outra versao compativel instalada no Python 3.12, o ambiente esta pronto para rodar a LSTM.

### 8. Rodar a modelagem principal

```powershell
python .\src\modelagem_revisada_reinaldo.py
```

### 9. Rodar o teste complementar de 2025

```powershell
python .\src\teste_final_2025.py
```

### 10. Rodar o teste exploratorio Prophet/LSTM

```powershell
python .\src\teste_prophet_lstm_2025.py
```

Esse teste compara:

- benchmark `media_movel_3m`, com WMAPE de 20,61%;
- Prophet;
- LSTM simples.

Resultados observados no ambiente Python 3.12.10 com TensorFlow 2.21.0 antes da fixacao mais forte de sementes:

- Prophet: WMAPE de 18,60%, superou o benchmark;
- LSTM simples: WMAPE aproximado entre 25,28% e 25,91%, nao superou o benchmark.

Depois dos ajustes de reprodutibilidade, consulte sempre o arquivo `outputs/teste_prophet_lstm_2025/resumo_prophet_lstm_2025.txt` para o valor exato da execucao atual. O script fixa sementes para `random`, `numpy` e `tensorflow`, tenta ativar operacoes deterministicas do TensorFlow, desativa o embaralhamento no treino da LSTM e define `TF_ENABLE_ONEDNN_OPTS=0` para reduzir pequenas diferencas numericas. Mesmo assim, pequenas variacoes ainda podem ocorrer dependendo do sistema operacional, CPU/GPU e versoes das bibliotecas.

### 11. Gerar o painel de resultados

```powershell
python .\src\gerar_painel_resultados.py
```

### 12. Onde ficam os arquivos gerados

Modelagem principal:

```text
outputs/
```

Teste complementar com 2025 como teste final:

```text
outputs/teste_2025/
```

Teste exploratorio Prophet/LSTM:

```text
outputs/teste_prophet_lstm_2025/
```

Arquivos principais do teste Prophet/LSTM:

- `outputs/teste_prophet_lstm_2025/metricas_prophet_lstm_2025.csv`
- `outputs/teste_prophet_lstm_2025/previsoes_prophet_lstm_2025.csv`
- `outputs/teste_prophet_lstm_2025/resumo_prophet_lstm_2025.txt`

### Observacao importante

O teste Prophet/LSTM e exploratorio e nao substitui a modelagem principal. A modelagem principal permanece baseada em modelos simples e interpretaveis, pois a base mensal tem tamanho limitado para sustentar conclusoes fortes com redes neurais.

## O que cada script faz

### `src/modelagem_revisada_reinaldo.py`

Executa a modelagem revisada:

- le a base diaria;
- agrega os dados por mes;
- separa validacao temporal e teste final;
- compara modelos simples e interpretaveis;
- calcula metricas como MAE, RMSE, WMAPE e vies percentual;
- calcula o dimensionamento de estoque com base em previsao, erro validado e nivel de servico.

### `src/gerar_painel_resultados.py`

Cria o painel HTML:

- le os arquivos `.csv` da pasta `outputs`;
- monta cards de resumo;
- gera graficos de demanda, ranking de modelos, previsao vs realizado e estoque necessario;
- salva tudo em `outputs/painel_resultados.html`.

## Observacoes metodologicas

O projeto evita tratar o resultado como uma "otimizacao" matematica, porque nao ha uma funcao objetivo formal com restricoes e algoritmo de otimizacao.

O termo mais adequado para a tese e:

- dimensionamento de estoque;
- calibracao de parametro;
- parametrizacao por nivel de servico;
- apoio a decisao gerencial.

## Problemas comuns

### `python` nao e reconhecido

Reinstale o Python e marque:

```text
Add python.exe to PATH
```

Depois feche e abra o PowerShell novamente.

### `git` nao e reconhecido

Instale o Git em:

```text
https://git-scm.com/downloads
```

Depois feche e abra o PowerShell novamente.

### Erro dizendo que a planilha nao foi encontrada

Confira se o arquivo existe neste caminho:

```text
data/base de dados resumida140526 .xlsx
```

O nome do arquivo tem um espaco antes de `.xlsx`, entao e importante manter o nome exatamente igual.

### O painel abriu, mas os dados parecem antigos

Rode novamente os dois comandos:

```powershell
python .\src\modelagem_revisada_reinaldo.py
python .\src\gerar_painel_resultados.py
```

Depois atualize a pagina no navegador.
