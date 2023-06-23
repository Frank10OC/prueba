import streamlit as st
import pandas as pd

dfa = pd.read_csv("https://raw.githubusercontent.com/Frank10OC/prueba/main/Reporte_Proyecto_APROBADO%20(4).csv")
# Mostrar el DataFrame en la aplicación de Streamlit
st.write(dfa)
import streamlit as st
import pandas as pd
import folium

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

    # Crear el mapa
    map = folium.Map()

    # Agregar marcadores al mapa
    for index, row in df.iterrows():
        lat = row[lat_column]
        lon = row[lon_column]
        folium.Marker(location=[lat, lon], popup=f"Ubicación {index}").add_to(map)

    # Mostrar el mapa
    folium_static(map)

if __name__ == "__main__":
    main()
