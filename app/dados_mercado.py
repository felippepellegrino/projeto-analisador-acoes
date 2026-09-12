# Importamos a biblioteca yfinance.
# Ela permite buscar dados financeiros através do Yahoo Finance.
import yfinance as yf


def buscar_dados(acao):
    """
    Busca os dados históricos de uma ação.

    Parâmetro:
        acao: código da ação, por exemplo PETR4

    Retorno:
        DataFrame contendo os dados históricos da ação.
    """

    # O Yahoo Finance utiliza ".SA" para ações brasileiras.
    # PETR4 -> PETR4.SA
    codigo = acao + ".SA"

    # Criamos um objeto que representa a ação.
    ticker = yf.Ticker(codigo)

    # Buscamos os dados dos últimos 3 meses.
    #
    # Precisamos de vários períodos porque vamos calcular
    # indicadores como a média móvel de 20 períodos.
    dados = ticker.history(period="3mo")

    # Retornamos os dados para quem chamou a função.
    return dados