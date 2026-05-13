import streamlit as st

st.title("Mi primera aplicación en Python")

st.sidebar.title("Parámetros")

st.write("Elaborado por: Jhonattan Lezma F.")

sesion = st.selecbox("Seleccione una sessión", ["Sessión 1","Sessión 2","Sessión 3","Sessión 4"])
