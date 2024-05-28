# Importar las librerias
import pandas as pd
import plotly.express as px
import streamlit as st

# leer los datos
car_data = pd.read_csv('./datasets/vehicles_us.csv')

# Encabezado de la aplicación
st.header('Análisis anuncios de vehículos')

# Crear un botón para el primer histograma
hist_button = st.button('Construir histograma')  # crear un botón

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Histograma de anuncios de vehículos por cuenta en odómetro')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
