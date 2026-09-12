# Importamos o RSI.
from ta.momentum import RSIIndicator

# Importamos o MACD.
from ta.trend import MACD


def calcular_variacao(dados):
    """
    Calcula a variação percentual da ação no período analisado.
    """

    # Pega o primeiro preço de fechamento disponível.
    preco_inicial = dados["Close"].iloc[0]

    # Pega o último preço de fechamento disponível.
    preco_final = dados["Close"].iloc[-1]

    # Fórmula da variação percentual:
    #
    # (preço final - preço inicial) / preço inicial * 100
    variacao = (
        (preco_final - preco_inicial)
        / preco_inicial
    ) * 100

    return variacao


def calcular_mm20(dados):
    """
    Calcula a Média Móvel de 20 períodos.
    """

    # Pegamos a coluna de preços de fechamento.
    fechamento = dados["Close"]

    # rolling(window=20) cria uma janela de 20 períodos.
    # mean() calcula a média desses 20 períodos.
    #
    # iloc[-1] pega somente o último resultado.
    media_movel = (
        fechamento
        .rolling(window=20)
        .mean()
        .iloc[-1]
    )

    return media_movel


def calcular_rsi(dados):
    """
    Calcula o RSI de 14 períodos.
    """

    # Criamos o indicador RSI utilizando
    # os preços de fechamento.
    indicador = RSIIndicator(
        close=dados["Close"],
        window=14
    )

    # Calculamos o RSI e pegamos o último valor.
    rsi = indicador.rsi().iloc[-1]

    return rsi


def calcular_macd(dados):
    """
    Calcula o MACD e a linha de sinal.
    """

    # Criamos o indicador MACD.
    indicador = MACD(
        close=dados["Close"],
        window_slow=26,
        window_fast=12,
        window_sign=9
    )

    # Valor atual do MACD.
    macd = indicador.macd().iloc[-1]

    # Valor atual da linha de sinal.
    sinal = indicador.macd_signal().iloc[-1]

    return macd, sinal


def calcular_volume(dados):
    """
    Compara o volume atual com a média de volume
    dos últimos 20 períodos.
    """

    # Volume do último período.
    volume_atual = dados["Volume"].iloc[-1]

    # Média do volume dos últimos 20 períodos.
    volume_medio = (
        dados["Volume"]
        .rolling(window=20)
        .mean()
        .iloc[-1]
    )

    return volume_atual, volume_medio


def calcular_pontuacao(
    preco,
    media_movel,
    rsi,
    variacao,
    macd,
    sinal_macd,
    volume_atual,
    volume_medio
):
    """
    Calcula uma pontuação de 0 a 5.

    Cada condição atendida adiciona 1 ponto.

    IMPORTANTE:
    Esta é uma regra experimental do nosso projeto.
    Não representa recomendação de investimento.
    """

    # Começamos com zero pontos.
    pontos = 0

    # 1º critério:
    # preço acima da média móvel de 20 períodos.
    if preco > media_movel:
        pontos += 1

    # 2º critério:
    # variação positiva no período analisado.
    if variacao > 0:
        pontos += 1

    # 3º critério:
    # RSI abaixo de 70.
    if rsi < 70:
        pontos += 1

    # 4º critério:
    # MACD acima da linha de sinal.
    if macd > sinal_macd:
        pontos += 1

    # 5º critério:
    # volume atual acima da média de volume.
    if volume_atual > volume_medio:
        pontos += 1

    # Retornamos a pontuação final.
    return pontos


def classificar_acao(pontuacao):
    """
    Transforma a pontuação em uma classificação.
    """

    if pontuacao == 5:
        return "MUITO FAVORÁVEL"

    elif pontuacao >= 3:
        return "FAVORÁVEL"

    elif pontuacao == 2:
        return "ATENÇÃO"

    else:
        return "DESFAVORÁVEL"