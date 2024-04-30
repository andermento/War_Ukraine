import streamlit as st
import pandas as pd

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

    st.bar_chart(df1, x="Países", y="Ajuda Financeira")

with st.container():
    st.write(" ")

    st.bar_chart(df1, x="Países", y="Ajuda Humanitária")

with st.container():
    st.write(" ")

    st.bar_chart(df2, x="Country", y="Number of Refugees")
