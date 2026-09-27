from app.analise import analisar_acao
import pytest

# Importamos o pandas para criar um DataFrame
# semelhante ao utilizado pelo programa real.
import pandas as pd


def test_analisar_acao():
    """
    Testa se a função analisar_acao()
    consegue reunir os resultados corretamente.
    """

    # -----------------------------------------------------
    # DADOS FALSOS PARA O TESTE
    # -----------------------------------------------------

    # Criamos um pequeno conjunto de dados
    # parecido com os dados que viriam do mercado.
    dados = pd.DataFrame({
        "Close": [10, 11, 12, 13, 14]
    })


    # -----------------------------------------------------
    # FUNÇÕES FALSAS PARA O TESTE
    # -----------------------------------------------------

    # Estas funções simulam os indicadores.
    #
    # Estamos dizendo:
    # "Quando alguém chamar calcular_variacao(),
    # devolva 10."
    def calcular_variacao(dados):
        return 10


    # Simula a média móvel.
    def calcular_mm20(dados):
        return 12


    # Simula o RSI.
    def calcular_rsi(dados):
        return 50


    # Simula o MACD.
    def calcular_macd(dados):
        return 2, 1


    # Simula o volume.
    def calcular_volume(dados):
        return 1000, 900


    # Simula a pontuação.
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
        assert preco == 14
        assert media_movel == 12
        assert rsi == 50
        assert variacao == 10
        assert macd == 2
        assert sinal_macd == 1
        assert volume_atual == 1000
        assert volume_medio == 900

        return 4


    # Simula a classificação.
    def classificar_acao(pontuacao):
        assert pontuacao == 4
        return "FAVORÁVEL"


    # -----------------------------------------------------
    # EXECUTAMOS A FUNÇÃO QUE ESTAMOS TESTANDO
    # -----------------------------------------------------

    resultado = analisar_acao(
        dados,
        calcular_variacao,
        calcular_mm20,
        calcular_rsi,
        calcular_macd,
        calcular_volume,
        calcular_pontuacao,
        classificar_acao
    )


    # -----------------------------------------------------
    # VERIFICAMOS OS RESULTADOS
    # -----------------------------------------------------

    # O último preço deve ser 14.
    assert resultado["preco"] == 14

    # A variação simulada deve ser 10.
    assert resultado["variacao"] == 10

    # A média móvel simulada deve ser 12.
    assert resultado["media_movel"] == 12

    # O RSI simulado deve ser 50.
    assert resultado["rsi"] == 50

    # O MACD simulado deve ser 2.
    assert resultado["macd"] == 2

    # A linha de sinal deve ser 1.
    assert resultado["sinal_macd"] == 1

    # O volume atual deve ser 1000.
    assert resultado["volume_atual"] == 1000

    # O volume médio deve ser 900.
    assert resultado["volume_medio"] == 900

    # A pontuação simulada deve ser 4.
    assert resultado["pontuacao"] == 4

    # A classificação simulada deve ser FAVORÁVEL.
    assert resultado["classificacao"] == "FAVORÁVEL"


def test_analisar_acao_sem_dados():
    """
    Testa se analisar_acao() gera ValueError
    quando recebe um DataFrame sem dados.
    """

    dados = pd.DataFrame({
        "Close": []
    })

    with pytest.raises(ValueError):
        analisar_acao(
            dados,
            None,
            None,
            None,
            None,
            None,
            None,
            None
        )

