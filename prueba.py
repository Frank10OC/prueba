import streamlit as st
import pandas as pd

dfa = pd.read_csv("https://raw.githubusercontent.com/Frank10OC/prueba/main/Reporte_Proyecto_APROBADO%20(4).csv")
# Mostrar el DataFrame en la aplicación de Streamlit
st.write(dfa)
import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    st.title("Visualizador de Coordenadas en Mapa")

    # Cargar el DataFrame
    df = cargar_dataframe()  # Función para cargar el DataFrame, puedes adaptarla según tus necesidades

    # Mostrar el DataFrame
    st.subheader("DataFrame")
    st.dataframe(df)

    # Obtener las columnas de coordenadas
    lat_column = st.selectbox("Columna de latitud", df.columns)
    lon_column = st.selectbox("Columna de longitud", df.columns)

    # Crear la figura del mapa
    fig = px.scatter_mapbox(df, lat=lat_column, lon=lon_column, hover_data=df.columns)

    # Configurar el diseño del mapa
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    # Mostrar el mapa
    st.plotly_chart(fig)

if __name__ == "__main__":
    main()
