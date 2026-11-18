import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_excel("H:\prova python\PROVA B\prova_python(35)\saeb_aprendizado_territorios-7-2023-EM.xlsx",
sheet_name="estados", engine="openpyxl")

df_filtrado = df[
    (df["uf"].isin(["MG", "BA", "CE", "PR"]))
].copy()

df_tabela = df_filtrado[["uf", "lingua portuguesa insuficiente", "matematica insuficiente"]]


st.title("Painel Streamlit — Portugues e matetica insuficientes")

st.sidebar.header("Controles")
opcao = st.sidebar.radio("Selecione a visualização:", ["Tabela", "Gráficos"])

if opcao == "Tabela":
    st.header("Tabela escolaridade")
    st.dataframe(df_tabela, use_container_width=True, hide_index=True)

elif opcao == "Gráficos":
    st.header("Gráficos escolaridades")

    st.subheader("3. Gráfico de Barras Agrupadas matematica insuficiente")
    fig_barras = px.bar(
        df_tabela,
        x="uf",
        y="matematica insuficiente",
        color="uf",
        barmode="group",
        title="matematica insuficiente",
        color_discrete_map={"MG": "#d3d3d3", "BA": "#d3d3d3", "CE": "d3d3d3", "PR": "d3d3d3"},
        template="plotly_dark"
    )
    fig_barras.update_xaxes(type="category")
    st.plotly_chart(fig_barras, use_container_width=True)

    st.subheader("3. Gráfico de Barras Agrupadas portugues insuficiente")
    fig_barras = px.bar(
        df_tabela,
        x="uf",
        y="lingua portuguesa insuficiente",
        color="uf",
        barmode="group",
        title="portugues insuficiente",
        color_discrete_map={"MG": "#d3d3d3", "BA": "#d3d3d3", "CE": "d3d3d3", "PR": "d3d3d3"},
        template="plotly_dark"
    )
    fig_barras.update_xaxes(type="category")
    st.plotly_chart(fig_barras, use_container_width=True)


st.markdown("---")
st.caption("A fonte dos dados visivel no painel: INEP, https://www.gov.br/inep")
