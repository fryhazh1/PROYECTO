 # Explorador de Vehículos US

Esta es una **aplicación web interactiva** construida con **Streamlit**, **Pandas** y **Plotly Express**. Permite explorar un conjunto de datos de vehículos en Estados Unidos (`vehicles_us.csv`) de manera visual e interactiva.

## Funcionalidad

- **Vista previa del dataset:** muestra las primeras filas de los datos cargados.
- **Histograma de odómetro:** genera un histograma interactivo de los kilometrajes de los vehículos.
- **Gráfico de dispersión:** permite visualizar la relación entre `odometer` y `model_year` (año del vehículo). Si la columna `manufacturer` está disponible, los puntos se colorean por fabricante.

## Cómo usar la aplicación

1. Instalar dependencias:

```bash
pip install streamlit pandas plotly
