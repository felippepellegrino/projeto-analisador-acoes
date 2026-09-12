# Analisador de Ações

Projeto desenvolvido em Python para análise de dados
de ações da bolsa de valores.

## Objetivo

O objetivo do projeto é desenvolver um sistema capaz de:

- receber o código de uma ação;
- buscar dados reais do mercado;
- calcular indicadores técnicos;
- analisar os dados;
- gerar uma pontuação;
- classificar o cenário da ação;
- armazenar histórico das análises;
- disponibilizar os dados através de uma API.

## Indicadores utilizados

Atualmente o projeto utiliza:

- Variação percentual;
- Média Móvel de 20 períodos (MM20);
- RSI;
- MACD;
- Volume negociado.

## Sistema de pontuação

O sistema possui atualmente 5 critérios:

1. Preço acima da MM20;
2. Variação positiva;
3. RSI abaixo de 70;
4. MACD acima da linha de sinal;
5. Volume atual acima da média.

Cada critério atendido adiciona 1 ponto.

A pontuação pode variar de 0 a 5.

## Classificação

- 5 pontos: MUITO FAVORÁVEL
- 3 ou 4 pontos: FAVORÁVEL
- 2 pontos: ATENÇÃO
- 0 ou 1 ponto: DESFAVORÁVEL

## Tecnologias

- Python
- Pandas
- yfinance
- TA
- Pytest
- PostgreSQL
- FastAPI
- Git
- GitHub

## Estrutura

```text
projeto_analisador_acoes/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── dados_mercado.py
│   └── indicadores.py
│
├── tests/
│   └── test_indicadores.py
│
├── README.md
├── pytest.ini
└── venv/