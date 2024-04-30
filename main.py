import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Guerra na Ucrânia", layout="wide")

df1 = pd.read_excel("War_UK_RU.xlsx")
df2 = pd.read_excel("War_UK_RU.xlsx", sheet_name="Refugiados por país")

with st.container():
    st.title("Guerra na Ucrânia")
    st.subheader("Dados sobre a Guerra na Ucrânia")
    st.write("Fonte: [InformationIsBeautiful](https://informationisbeautiful.net/visualizations/ukraine-russian-war-infographics-data-visuals/#OilReserves)")

with st.container():
    st.write("---")

with st.container():
    st.image('mortosferidos.png', caption='Mortos e Feridos na Guerra da Ucrânia')

with st.container():
    st.write(" ")

with st.container():
    st.image('forca_militar.png', caption='Força Militar russa e ucraniana')

with st.container():
    st.write(" ")

col1, col2, col3 = st.columns(3)

fig_refug = px.pie(df2, values="Number of Refugees", names="Country", title="Países que mais receberam refugiados")
col1.plotly_chart(fig_refug)

fig_fin = px.bar(df1, x="Países", y="Ajuda Financeira", title="Ajuda financeira à Ucrânia (por país)")
col2.plotly_chart(fig_fin)

fig_hum = px.bar(df1, x="Países", y="Ajuda Humanitária", title="Ajuda humanitária à Ucrânia (por país)", orientation="h")
col3.plotly_chart(fig_hum)
