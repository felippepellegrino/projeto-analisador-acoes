# Analisador de Ações

Projeto desenvolvido em Python para análise de dados de ações da bolsa de valores.

O projeto busca aplicar conceitos de **Python, análise de dados, indicadores técnicos, testes automatizados e organização de software**.

## Objetivo

O objetivo do projeto é desenvolver um sistema capaz de:

* receber o código de uma ação;
* buscar dados reais do mercado;
* calcular indicadores técnicos;
* analisar os dados;
* gerar uma pontuação;
* classificar o cenário da ação;
* armazenar histórico das análises;
* disponibilizar os dados através de uma API.

## Indicadores utilizados

Atualmente o projeto utiliza:

* Variação percentual;
* Média Móvel de 20 períodos (MM20);
* RSI;
* MACD;
* Volume negociado.

## Sistema de pontuação

O sistema possui atualmente 5 critérios:

1. Preço acima da MM20;
2. Variação positiva;
3. RSI abaixo de 70;
4. MACD acima da linha de sinal;
5. Volume atual acima da média.

Cada critério atendido adiciona 1 ponto.

A pontuação pode variar de **0 a 5**.

## Classificação

* **5 pontos:** MUITO FAVORÁVEL
* **3 ou 4 pontos:** FAVORÁVEL
* **2 pontos:** ATENÇÃO
* **0 ou 1 ponto:** DESFAVORÁVEL

> A classificação é uma regra definida pelo projeto para fins de análise técnica e não constitui recomendação de investimento.

## Tecnologias utilizadas

### Atualmente implementadas

* Python
* Pandas
* yfinance
* TA
* Pytest
* Git
* GitHub

### Planejadas

* PostgreSQL
* FastAPI
* Dashboard
* Armazenamento do histórico das análises
* Integração com recursos de Inteligência Artificial

## Testes

O projeto utiliza **Pytest** para testar as funções responsáveis pelos indicadores e pela análise das ações.

Atualmente existem **24 testes automatizados**.

Para executar os testes:

```bash
pytest
```

## Como executar

### 1. Clonar o projeto

```bash
git clone https://github.com/felippepellegrino/projeto-analisador-acoes.git
```

### 2. Entrar na pasta

```bash
cd projeto-analisador-acoes
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
pytest
```

## Estrutura do projeto

```text
projeto_analisador_acoes/
│
├── app/
│   ├── __init__.py
│   ├── main.py
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

* [x] Buscar dados reais do mercado
* [x] Calcular indicadores técnicos
* [x] Criar sistema de pontuação
* [x] Criar classificação da ação
* [x] Criar função central de análise
* [x] Criar testes automatizados
* [x] Criar validação para dados vazios
* [x] Criar `requirements.txt`
* [ ] Implementar armazenamento do histórico
* [ ] Integrar PostgreSQL
* [ ] Criar API com FastAPI
* [ ] Criar dashboard
* [ ] Adicionar recursos de Inteligência Artificial

## Observação

Este projeto possui finalidade **educacional e de portfólio**, sendo desenvolvido para praticar programação, análise de dados, testes automatizados e desenvolvimento de software.

As análises e classificações geradas pelo sistema não constituem recomendação de investimento.
