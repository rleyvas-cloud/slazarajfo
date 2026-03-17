import streamlit as st

st.title("Simulador de reactor químico")

T = st.slider("Temperatura (K)", 300, 1000, 500)
P = st.slider("Presión (atm)", 1, 10, 1)

conversion = (T / 1000) * (P / 10)

st.write("Conversión estimada:", conversion)
