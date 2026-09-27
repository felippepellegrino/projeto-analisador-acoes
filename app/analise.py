# ---------------------------------------------------------
# FUNÇÃO PRINCIPAL DE ANÁLISE
# ---------------------------------------------------------

def analisar_acao(
    dados,
    calcular_variacao,
    calcular_mm20,
    calcular_rsi,
    calcular_macd,
    calcular_volume,
    calcular_pontuacao,
    classificar_acao
):
    """
    Recebe os dados de uma ação e calcula todos
    os indicadores necessários para a análise.

    No final, retorna todos os resultados
    organizados em um dicionário.
    """

    # -----------------------------------------------------
    # PREÇO ATUAL
    # -----------------------------------------------------

    # Pega o último preço de fechamento disponível.
    #
    # iloc[-1] significa:
    # "pegue o último valor da coluna".
    #
    # Exemplo:
    # [45.10, 46.20, 47.30, 48.07]
    #
    # iloc[-1] -> 48.07
    preco = dados["Close"].iloc[-1]


    # -----------------------------------------------------
    # INDICADORES
    # -----------------------------------------------------

    # Calcula a variação percentual da ação.
    variacao = calcular_variacao(dados)

    # Calcula a média móvel de 20 períodos.
    media_movel = calcular_mm20(dados)

    # Calcula o RSI.
    rsi = calcular_rsi(dados)

    # Calcula o MACD e a linha de sinal.
    #
    # Como a função retorna dois valores,
    # precisamos guardar os dois.
    macd, sinal_macd = calcular_macd(dados)

    # Calcula o volume atual e o volume médio.
    volume_atual, volume_medio = calcular_volume(dados)


    # -----------------------------------------------------
    # PONTUAÇÃO
    # -----------------------------------------------------

    # Envia todos os indicadores para a função
    # responsável por calcular a pontuação da ação.
    #
    # O resultado será uma pontuação de 0 a 5.
    pontuacao = calcular_pontuacao(
        preco,
        media_movel,
        rsi,
        variacao,
        macd,
        sinal_macd,
        volume_atual,
        volume_medio
    )


    # -----------------------------------------------------
    # CLASSIFICAÇÃO
    # -----------------------------------------------------

    # Transforma a pontuação em uma classificação.
    #
    # Exemplo:
    # 3 pontos -> FAVORÁVEL
    classificacao = classificar_acao(pontuacao)


    # -----------------------------------------------------
    # RESULTADO FINAL
    # -----------------------------------------------------

    # Organizamos todos os resultados em um dicionário.
    #
    # Pense no dicionário como uma caixa com várias
    # informações identificadas por nomes.
    resultado = {
        "preco": preco,
        "variacao": variacao,
        "media_movel": media_movel,
        "rsi": rsi,
        "macd": macd,
        "sinal_macd": sinal_macd,
        "volume_atual": volume_atual,
        "volume_medio": volume_medio,
        "pontuacao": pontuacao,
        "classificacao": classificacao
    }


    # Devolve o resultado para quem chamou
    # a função analisar_acao().
    return resultado