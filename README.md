# Analisador de Ações

Projeto desenvolvido em Python para análise de dados de ações da bolsa de valores.

O projeto busca aplicar conceitos de **Python, análise de dados, indicadores técnicos, testes automatizados, interfaces gráficas e organização de software**.

## Objetivo

Desenvolver um sistema capaz de:

- Receber o código de uma ação;
- Buscar dados reais do mercado financeiro;
- Calcular indicadores técnicos;
- Analisar os dados;
- Gerar uma pontuação;
- Classificar o cenário da ação;
- Disponibilizar uma interface gráfica para visualização dos resultados.

## Indicadores utilizados

Atualmente o projeto utiliza:

- Variação percentual;
- Média Móvel de 20 períodos (MM20);
- RSI;
- MACD;
- Volume negociado.

## Sistema de pontuação

O sistema possui 5 critérios:

1. Preço acima da MM20;
2. Variação positiva;
3. RSI abaixo de 70;
4. MACD acima da linha de sinal;
5. Volume atual acima da média.

Cada critério atendido adiciona 1 ponto.

A pontuação pode variar de **0 a 5**.

## Classificação

- **5 pontos:** MUITO FAVORÁVEL
- **3 ou 4 pontos:** FAVORÁVEL
- **2 pontos:** ATENÇÃO
- **0 ou 1 ponto:** DESFAVORÁVEL

> A classificação é uma regra definida pelo projeto para fins de análise técnica e não constitui recomendação de investimento.

## Interface gráfica

O projeto possui uma interface gráfica desenvolvida com **Streamlit**, permitindo:

- Informar o código de uma ação;
- Visualizar o preço atual;
- Consultar os indicadores técnicos;
- Visualizar a pontuação e classificação;
- Verificar individualmente os critérios atendidos;
- Visualizar gráficos de preço, média móvel e volume negociado.

## Tecnologias utilizadas

### Implementadas

- Python
- Pandas
- yfinance
- TA
- Pytest
- Streamlit
- Git
- GitHub

### Planejadas

- PostgreSQL
- FastAPI
- Armazenamento do histórico das análises
- Integração com recursos de Inteligência Artificial

## Testes

O projeto utiliza **Pytest** para testar as funções responsáveis pelos indicadores e pela análise das ações.

Para executar os testes:

```bash
python -m pytest -v
```

## Como executar

### 1. Clonar o projeto

```bash
git clone https://github.com/felippepellegrino/projeto_analisador_acoes.git
```

### 2. Entrar na pasta

```bash
cd projeto_analisador_acoes
```

### 3. Criar o ambiente virtual

```bash
python -m venv venv
```

### 4. Ativar o ambiente virtual no Windows

```bash
venv\Scripts\activate
```

### 5. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 6. Executar os testes

```bash
python -m pytest -v
```

### 7. Executar a interface gráfica

```bash
python -m streamlit run app/interface.py
```

## Estrutura do projeto

```text
projeto_analisador_acoes/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── interface.py
│   ├── dados_mercado.py
│   ├── indicadores.py
│   └── analise.py
│
├── tests/
│   ├── test_indicadores.py
│   └── test_analise.py
│
├── .gitignore
├── README.md
├── pytest.ini
└── requirements.txt
```

## Próximos passos

O projeto está sendo desenvolvido de forma incremental.

Próximas etapas planejadas:

- Implementar armazenamento do histórico das análises;
- Integrar PostgreSQL;
- Criar API com FastAPI;
- Integrar recursos de Inteligência Artificial;
- Melhorar a interface gráfica;
- Ampliar a cobertura de testes automatizados.

## Observação

Este projeto possui finalidade **educacional e de portfólio**, sendo desenvolvido para praticar programação, análise de dados, testes automatizados e desenvolvimento de software.

As análises e classificações geradas pelo sistema não constituem recomendação de investimento.