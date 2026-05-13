import streamlit as st

st.title("Mi primera aplicación en Python")

st.sidebar.title("Parámetros")

st.write("Elaborado por: Jhonattan Lezma F.")

sesion = st.sidebar.selectbox("Seleccione una sessión", ["Sesión 1","Sesión 2","Sesión 3","Sesión 4"])

if sesion == "Sesión 1":
  st.write("Bienvenido a la Sesión 1")
  
elif sesion == "Sesión 2":
  st.write("Bienvenido a la Sesión 2")
  
elif sesion == "Sesión 3":
  st.write("Bienvenido a la Sesión 3")
  
else:
  st.write("Bienvenido a la Sesión 4")


