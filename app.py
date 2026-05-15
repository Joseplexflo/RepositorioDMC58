import streamlit as st
import numpy as np
import libreria_funciones as lf

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

  precio = st.number_input("Ingrese el precio del producto",min_value=0,max_value=50000, value=1200)
  descuento = st.number_input("Ingrese el descuento del producto del 0 al 100%",min_value=0,max_value=100)
  precio_final_producto = precio - (precio * (descuento/100))
  st.write("El precio final del producto es:",precio_final_producto)
  
elif sesion == "Sesión 3":
  st.write("Bienvenido a la Sesión 3")
  
  fin_rango = st.slider("Seleccione un valor",min_value=0,max_value=20,value=7)

  arreglo=np.arange(0,fin_rango)
  st.write(arreglo)

else:
  st.write("Bienvenido a la Sesión 4")
  principal = st.numbres_input("Ingrese el monto del prestamo",value=1000)
  tasa_anual = st.numbres_input("Ingrese la tasa anual en decimal",value=0.1,min_value=0.0,max_value=1.0)
  anios = st.numbres_input("Ingrese el numero de años del prestamo",value=1)
  pagos_anio = st.numbres_input("Ingrese la cantidad de pagos por año",value=12)
  
  cuota = lf.cuota_prestamo(principal,tasa_anual,anios,pagos_anio)
  st.write(cuota)

