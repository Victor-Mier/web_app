# Importar las librerias
import pandas as pd
import plotly.express as px
import streamlit as st

# leer los datos
car_data = pd.read_csv('./datasets/vehicles_us.csv')

# Encabezado de la aplicación
st.header('Análisis anuncios de vehículos')

# Crear casillas de verificación para los primeros histogramas
# crear casilla de verificación
hist_checkbox_1 = st.checkbox('Histrograma de odómetro')

if hist_checkbox_1:  # al hacer clic en la casilla
    # escribir un mensaje
    st.write('Histograma de anuncios de vehículos por cuenta en odómetro')
    st.write('La mediana de los carros anunciados está en:',
             car_data['odometer'].median())

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# crear casilla de verificación
hist_checkbox_2 = st.checkbox('Histrograma de año modelo por condición')

if hist_checkbox_2:  # al hacer clic en la casilla
    # escribir un mensaje
    st.write('Histograma de anuncios de vehículos por año modelo y condición')
    # preparar el dataset
    long_df = car_data.groupby(['model_year', 'condition'])[
        'condition'].count().reset_index(name="count")
    # generar gráfico
    fig = px.bar(long_df, x="model_year", y="count", color="condition",
                 title="Histogram of condition vs model year")
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# crear casilla de verificación para los diagramas de dispersión
# crear casilla de verificación
scatter_checkbox_1 = st.checkbox(
    'Diagrama de dispersión año modelo vs odómetro')

if scatter_checkbox_1:  # al hacer clic en la casilla
    # escribir un mensaje
    st.write('Diagrama de dispersión año modelo vs odómetro')
    # crear gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="model_year")
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# crear casilla de verificación
scatter_checkbox_2 = st.checkbox(
    'Diagrama de dispersión de modelo vs precio')

if scatter_checkbox_2:  # al hacer clic en la casilla
    # escribir un mensaje
    st.write('Diagrama de dispersión de modelo vs precio, identificado por colores de acuerdo al año modelo')
    # crear gráfico de dispersión
    fig = px.scatter(car_data, x="model", y="price", color='model_year')
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Crear un botón para mostrar el dataset de forma interactiva
# Crear un botón
table_button = st.button('Mostrar toda la tabla')

if table_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('A continuación se muestra toda la tabla de anuncios de vehículos')

    # crear un histograma
    st.dataframe(car_data, width=1200, height=400,
                 hide_index=True, selection_mode="multi-column")
