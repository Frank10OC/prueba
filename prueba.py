import streamlit as st
import requests

def main():
    st.title("Obtener datos de una página web en Streamlit")

    # URL de la página web
    url = "https://www.datosabiertos.gob.pe/dataset/casos-positivos-por-covid-19-ministerio-de-salud-minsa/resource/690e57a6-a465-47d8-86fd"

    # Realizar la solicitud HTTP a la página
    response = requests.get(url)

    if response.status_code == 200:
        # Procesar la respuesta
        data = response.text

        # Mostrar los datos en Streamlit
        st.subheader("Contenido de la página web")
        st.text(data)
    else:
        st.error(f"Error al obtener los datos. Código de estado: {response.status_code}")

if __name__ == "__main__":
    main()



