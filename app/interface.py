
import streamlit as st

from dados_mercado import buscar_dados

from analise import analisar_acao

from indicadores import (
    calcular_variacao,
    calcular_mm20,
    calcular_rsi,
    calcular_macd,
    calcular_volume,
    calcular_pontuacao,
    classificar_acao,
    analisar_criterios
)


st.set_page_config(
    page_title="Analisador de Ações",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Analisador de Ações")

st.write("Analise indicadores técnicos de ações da bolsa brasileira.")

acao = st.text_input("Digite o código da ação:", placeholder="Exemplo: PETR4")


if st.button("Analisar ação"):

    codigo = acao.strip().upper()

    if not codigo:
        st.warning("Digite o código de uma ação.")

    else:
        try:
            with st.spinner("Buscando dados e analisando a ação..."):

                dados = buscar_dados(codigo)

                if dados.empty:
                    st.error("Não foram encontrados dados para essa ação.")

                else:
                    resultado = analisar_acao(
                        codigo,
                        dados,
                        calcular_variacao,
                        calcular_mm20,
                        calcular_rsi,
                        calcular_macd,
                        calcular_volume,
                        calcular_pontuacao,
                        classificar_acao,
                        analisar_criterios
                    )

                    st.subheader(f"Resultado: {codigo}")

                    col1, col2, col3, col4 = st.columns(4)

                    col1.metric(
                        "Preço atual",
                        f"R$ {resultado['preco']:.2f}"
                    )

                    col2.metric(
                        "Variação",
                        f"{resultado['variacao']:.2f}%"
                    )

                    col3.metric(
                        "Pontuação",
                        f"{resultado['pontuacao']}/5"
                    )

                    col4.metric(
                        "Classificação",
                        resultado["classificacao"]
                    )

                    st.subheader("Indicadores técnicos")

                    col1, col2, col3, col4 = st.columns(4)

                    col1.metric(
                        "Média móvel 20",
                        f"R$ {resultado['media_movel']:.2f}"
                    )

                    col2.metric(
                        "RSI",
                        f"{resultado['rsi']:.2f}"
                    )

                    col3.metric(
                        "MACD",
                        f"{resultado['macd']:.2f}"
                    )

                    col4.metric(
                        "Volume atual",
                        f"{resultado['volume_atual']:,.0f}"
                    )

                    # Criando os dados do gráfico
                    grafico = dados[["Close", "Volume"]].copy()

                    # Calculando a média móvel de 20 dias
                    grafico["MM20"] = grafico["Close"].rolling(window=20).mean()

                    #Gráfico de preço e média móvel
                    st.subheader("Evolução do preço e média móvel")
                    st.line_chart(
                        grafico[["Close", "MM20"]]
                    )

                    #Gráfico de volume
                    st.subheader("Volume negociado")
                    st.bar_chart(
                        grafico[["Volume"]]
                    )

                    #Critérios de análise
                    st.subheader("Critérios da análise")

                    for criterio, atendido in resultado["criterios"].items():

                        if atendido:
                            st.success(f"{criterio}: ATENDIDO")
                        else:
                            st.warning(f"{criterio}: NÃO ATENDIDO")

        except Exception as erro:
            st.error(f"Erro durante a análise: {erro}")


st.caption("Análise experimental baseada em indicadores técnicos. Não constitui recomendação de investimento.")
