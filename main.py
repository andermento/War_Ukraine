import streamlit as st

st.set_page_config(page_title="Guerra na Ucrânia")

with st.container():
    st.subheader("Dados sobre a Guerra na Ucrânia")
    st.title("Guerra na Ucrânia")
    st.write("Fonte: [InformationIsBeautiful](https://informationisbeautiful.net/visualizations/ukraine-russian-war-infographics-data-visuals/#OilReserves)")

with st.container():
    st.write("---")

with st.container():
    st.image('mortosferidos.png', caption='Mortos e Feridos na Guerra da Ucrânia')

with st.container():
    st.image('forca_militar.png', caption='Força Militar russa e ucraniana')

