import pandas as pd

from app.indicadores import (
    calcular_pontuacao,
    classificar_acao,
    calcular_variacao,
    calcular_mm20,
    calcular_rsi,
    calcular_macd,
    calcular_volume
)


# ============================================================
# TESTES DA PONTUAÇÃO
# ============================================================

def test_pontuacao_maxima():
    resultado = calcular_pontuacao(
        preco=110,
        media_movel=100,
        rsi=50,
        variacao=10,
        macd=2,
        sinal_macd=1,
        volume_atual=2000,
        volume_medio=1000
    )

    assert resultado == 5


def test_pontuacao_zero():
    resultado = calcular_pontuacao(
        preco=90,
        media_movel=100,
        rsi=70,
        variacao=0,
        macd=1,
        sinal_macd=2,
        volume_atual=900,
        volume_medio=1000
    )

    assert resultado == 0


def test_classificacao():
    assert classificar_acao(5) == "MUITO FAVORÁVEL"
    assert classificar_acao(3) == "FAVORÁVEL"
    assert classificar_acao(2) == "ATENÇÃO"
    assert classificar_acao(1) == "DESFAVORÁVEL"
    assert classificar_acao(0) == "DESFAVORÁVEL"


def test_pontuacao_nos_limites():
    resultado = calcular_pontuacao(
        preco=100,
        media_movel=100,
        rsi=70,
        variacao=0,
        macd=2,
        sinal_macd=2,
        volume_atual=1000,
        volume_medio=1000
    )

    assert resultado == 0


def test_criterio_preco_acima_media():
    resultado = calcular_pontuacao(
        preco=110,
        media_movel=100,
        rsi=70,
        variacao=0,
        macd=1,
        sinal_macd=1,
        volume_atual=1000,
        volume_medio=1000
    )

    assert resultado == 1


def test_criterio_variacao_positiva():
    resultado = calcular_pontuacao(
        preco=100,
        media_movel=100,
        rsi=70,
        variacao=5,
        macd=1,
        sinal_macd=1,
        volume_atual=1000,
        volume_medio=1000
    )

    assert resultado == 1


def test_criterio_rsi_abaixo_70():
    resultado = calcular_pontuacao(
        preco=100,
        media_movel=100,
        rsi=60,
        variacao=0,
        macd=1,
        sinal_macd=1,
        volume_atual=1000,
        volume_medio=1000
    )

    assert resultado == 1


def test_criterio_macd_acima_sinal():
    resultado = calcular_pontuacao(
        preco=100,
        media_movel=100,
        rsi=70,
        variacao=0,
        macd=2,
        sinal_macd=1,
        volume_atual=1000,
        volume_medio=1000
    )

    assert resultado == 1


def test_criterio_volume_acima_media():
    resultado = calcular_pontuacao(
        preco=100,
        media_movel=100,
        rsi=70,
        variacao=0,
        macd=1,
        sinal_macd=1,
        volume_atual=1500,
        volume_medio=1000
    )

    assert resultado == 1


# ============================================================
# TESTES DA VARIAÇÃO
# ============================================================

def test_calcular_variacao():
    dados = pd.DataFrame({
        "Close": [100, 105, 110]
    })

    resultado = calcular_variacao(dados)

    assert resultado == 10


# ============================================================
# TESTES DA MÉDIA MÓVEL
# ============================================================

def test_calcular_mm20():
    dados = pd.DataFrame({
        "Close": [100] * 20
    })

    resultado = calcular_mm20(dados)

    assert resultado == 100


def test_calcular_mm20_com_valores_diferentes():
    dados = pd.DataFrame({
        "Close": list(range(1, 21))
    })

    resultado = calcular_mm20(dados)

    assert resultado == 10.5


# ============================================================
# TESTES DO RSI
# ============================================================

def test_calcular_rsi_com_alta_continua():
    """
    Testa o RSI usando preços que sobem continuamente.
    """

    dados = pd.DataFrame({
        "Close": list(range(1, 31))
    })

    resultado = calcular_rsi(dados)

    assert resultado > 70


def test_calcular_rsi_com_queda_continua():
    """
    Testa o RSI usando preços que caem continuamente.
    """

    dados = pd.DataFrame({
        "Close": list(range(30, 0, -1))
    })

    resultado = calcular_rsi(dados)

    assert resultado < 30


# ============================================================
# TESTES DO MACD
# ============================================================

def test_calcular_macd_com_dados_suficientes():
    """
    Testa se o MACD retorna valores válidos.
    """

    dados = pd.DataFrame({
        "Close": list(range(1, 61))
    })

    macd, sinal = calcular_macd(dados)

    assert pd.notna(macd)
    assert pd.notna(sinal)


def test_calcular_macd_com_queda_continua():
    """
    Testa o MACD usando preços em queda contínua.
    """

    dados = pd.DataFrame({
        "Close": list(range(60, 0, -1))
    })

    macd, sinal = calcular_macd(dados)

    assert pd.notna(macd)
    assert pd.notna(sinal)


def test_macd_retorna_dois_valores():
    """
    Verifica se calcular_macd retorna MACD e linha de sinal.
    """

    dados = pd.DataFrame({
        "Close": list(range(1, 61))
    })

    resultado = calcular_macd(dados)

    assert len(resultado) == 2


# ============================================================
# TESTES DO VOLUME
# ============================================================

def test_calcular_volume():
    """
    Testa o cálculo do volume atual e da média.
    """

    dados = pd.DataFrame({
        "Volume": [100] * 19 + [200]
    })

    volume_atual, volume_medio = calcular_volume(dados)

    assert volume_atual == 200
    assert volume_medio == 105


def test_calcular_volume_com_volume_constante():
    """
    Quando todos os volumes são iguais,
    a média deve ser igual ao volume atual.
    """

    dados = pd.DataFrame({
        "Volume": [1000] * 20
    })

    volume_atual, volume_medio = calcular_volume(dados)

    assert volume_atual == 1000
    assert volume_medio == 1000


# ============================================================
# TESTES EXTRAS
# ============================================================

def test_pontuacao_parcial():
    """
    Verifica uma situação intermediária de pontuação.
    """

    resultado = calcular_pontuacao(
        preco=110,
        media_movel=100,
        rsi=80,
        variacao=5,
        macd=1,
        sinal_macd=2,
        volume_atual=1500,
        volume_medio=1000
    )

    assert resultado == 3


def test_classificacao_pontuacao_4():
    """
    Uma pontuação de 4 deve ser classificada como favorável.
    """

    resultado = classificar_acao(4)

    assert resultado == "FAVORÁVEL"
    
def test_classificacao_pontuacao_negativa():
    """
    Verifica se uma pontuação negativa também
    recebe a classificação DESFAVORÁVEL.
    """

    resultado = classificar_acao(-1)

    assert resultado == "DESFAVORÁVEL"
