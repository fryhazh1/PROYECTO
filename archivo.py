# archivo.py

import streamlit as st
import pandas as pd
import plotly.express as px

# Encabezado de la aplicación
st.header("Explorador de Vehículos US")

# Leer el archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Mostrar una vista previa del dataset
st.write("Vista previa del dataset:")
st.write(car_data.head())

# Botón para generar histograma
if st.button("Generar histograma de odómetro"):
    fig_hist = px.histogram(
        car_data,
        x="odometer",
        nbins=50,
        title="Histograma de Odometer"
    )
    st.plotly_chart(fig_hist)

# Botón para generar gráfico de dispersión
# Botón para generar gráfico de dispersión
if st.button("Generar gráfico de dispersión"):
    fig_scatter = px.scatter(
        car_data,
        x="odometer",
        y="model_year",  # <-- corregido
        color="manufacturer" if "manufacturer" in car_data.columns else None,
        title="Gráfico de dispersión: Odometer vs Model Year"
    )
    st.plotly_chart(fig_scatter)






