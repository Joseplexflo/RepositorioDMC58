import streamlit as st

st.title("Mi primera aplicación en Python")

st.sidebar.title("Parámetros")

st.write("Elaborado por: Jhonattan Lezma F.")

st.sidebar.image("Image20260512194106.png")

sesion = st.sidebar.selectbox("Seleccione una sessión", ["Sesión 1","Sesión 2","Sesión 3","Sesión 4"])

if sesion == "Sesión 1":
  st.write("Bienvenido a la Sesión 1")
  st.image("Image20260512194057.png") #imagen python
  
elif sesion == "Sesión 2":
  st.write("Bienvenido a la Sesión 2")

  precio = st.number_input("Ingrese el precio del producto")
  descuento = st.number_input("Ingrese el descuento del producto")
  precio_final_producto = precio - (precio * descuento)
  st.write("El precio final del producto es:",precio_final_producto)
  
elif sesion == "Sesión 3":
  st.write("Bienvenido a la Sesión 3")
  
else:
  st.write("Bienvenido a la Sesión 4")


