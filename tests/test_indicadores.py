# Importamos a função que queremos testar.
from app.indicadores import calcular_pontuacao


def test_pontuacao_maxima():
    """
    Testa se a função consegue retornar 5 pontos
    quando todos os critérios são atendidos.
    """

    resultado = calcular_pontuacao(
        # Preço acima da média.
        preco=110,

        # Média móvel.
        media_movel=100,

        # RSI abaixo de 70.
        rsi=50,

        # Variação positiva.
        variacao=10,

        # MACD acima do sinal.
        macd=5,

        # Linha de sinal.
        sinal_macd=2,

        # Volume atual acima da média.
        volume_atual=200000,

        # Volume médio.
        volume_medio=100000
    )

    # Esperamos que os 5 critérios sejam atendidos.
    assert resultado == 5


def test_pontuacao_zero():
    """
    Testa se a função retorna 0 quando nenhum
    dos critérios é atendido.
    """

    resultado = calcular_pontuacao(
        # Preço abaixo da média.
        preco=90,

        # Média móvel.
        media_movel=100,

        # RSI acima de 70.
        rsi=80,

        # Variação negativa.
        variacao=-10,

        # MACD abaixo do sinal.
        macd=1,

        # Linha de sinal.
        sinal_macd=5,

        # Volume atual abaixo da média.
        volume_atual=50000,

        # Volume médio.
        volume_medio=100000
    )

    # Nesse cenário esperamos zero pontos.
    assert resultado == 0