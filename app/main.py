# Importamos a função responsável por buscar
# os dados da ação.
from dados_mercado import buscar_dados

# Importamos a função responsável por realizar
# a análise completa da ação.
from analise import analisar_acao


# Importamos as funções responsáveis pelos indicadores.
from indicadores import (
    calcular_variacao,
    calcular_mm20,
    calcular_rsi,
    calcular_pontuacao,
    classificar_acao,
    calcular_macd,
    calcular_volume
)


def receber_acao():
    """
    Solicita ao usuário o código da ação.
    """

    # O while mantém o programa perguntando
    # até receber alguma informação.
    while True:

        # input() recebe o código digitado.
        #
        # strip() remove espaços extras.
        #
        # upper() transforma letras minúsculas em maiúsculas.
        #
        # Exemplo:
        # " petr4 " -> "PETR4"
        acao = input(
            "Digite o código da ação: "
        ).strip().upper()

        # Verificamos se o usuário digitou alguma coisa.
        if acao:
            return acao

        # Caso tenha deixado vazio.
        print("Digite uma ação válida.")


# ---------------------------------------------------------
# PROGRAMA PRINCIPAL
# ---------------------------------------------------------

# Primeiro recebemos o código da ação.
acao = receber_acao()


# Tentamos buscar os dados.
#
# try/except evita que o programa simplesmente
# quebre caso aconteça algum problema.
try:

    # Busca os dados através do arquivo dados_mercado.py.
    dados = buscar_dados(acao)

    # Se o DataFrame estiver vazio, significa que
    # não recebemos dados válidos.
    if dados.empty:

        print(
            "Não foi possível encontrar dados "
            "para essa ação."
        )

        # Encerra o programa.
        exit()


except Exception as erro:

    # Caso aconteça algum erro durante a busca.
    print(
        "Ocorreu um erro ao buscar os dados."
    )

    # Mostramos o detalhe do erro para ajudar
    # durante o desenvolvimento.
    print(f"Detalhes: {erro}")

    exit()


# ---------------------------------------------------------
# CÁLCULO DOS DADOS
# ---------------------------------------------------------

# Enviamos os dados da ação para a função
# responsável por realizar toda a análise.
resultado = analisar_acao(
    acao,
    dados,
    calcular_variacao,
    calcular_mm20,
    calcular_rsi,
    calcular_macd,
    calcular_volume,
    calcular_pontuacao,
    classificar_acao
)


# Pegamos cada informação do resultado.
#
# resultado é um dicionário criado dentro
# da função analisar_acao().
preco = resultado["preco"]
variacao = resultado["variacao"]
media_movel = resultado["media_movel"]
rsi = resultado["rsi"]
macd = resultado["macd"]
sinal_macd = resultado["sinal_macd"]
volume_atual = resultado["volume_atual"]
volume_medio = resultado["volume_medio"]
pontuacao = resultado["pontuacao"]
classificacao = resultado["classificacao"]


# ---------------------------------------------------------
# APRESENTAÇÃO DOS RESULTADOS
# ---------------------------------------------------------

print()
print("======================================")
print("       ANÁLISE DA AÇÃO")
print("======================================")

print(f"Código: {acao}")

print(f"Preço atual: R$ {preco:.2f}")

print(
    f"Variação no período: "
    f"{variacao:.2f}%"
)

print(
    f"Média móvel de 20 períodos: "
    f"R$ {media_movel:.2f}"
)

print(f"RSI: {rsi:.2f}")

print(f"MACD: {macd:.2f}")

print(
    f"Linha de sinal: "
    f"{sinal_macd:.2f}"
)

print(
    f"Volume atual: "
    f"{volume_atual:,.0f}"
)

print(
    f"Volume médio: "
    f"{volume_medio:,.0f}"
)

print()
print(
    f"Pontuação: {pontuacao}/5"
)

print(
    f"Classificação: {classificacao}"
)

print("======================================")
