import streamlit as st
import pandas as pd

def main():
    st.title("Convertir JSON a CSV")

    # Cargar el archivo JSON
    file = st.file_uploader("Cargar archivo JSON", type=["json"])
    if file is not None:
        content = file.read()
        try:
            # Convertir JSON a DataFrame
            df = pd.read_json(content)

            # Convertir DataFrame a CSV
            csv_data = df.to_csv(index=False)

            # Descargar el archivo CSV resultante
            st.download_button("Descargar CSV", data=csv_data, file_name='archivo.csv')

        except pd.errors.JSONDecodeError:
            st.error("Error al decodificar el archivo JSON.")

if __name__ == "__main__":
    main()

