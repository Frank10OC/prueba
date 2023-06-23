import streamlit as st
import gdown
import pandas as pd

def main():
    st.title("Descargar y mostrar DataFrame de Google Drive en Streamlit")

    # URL de descarga del archivo desde Google Drive
    url = "https://drive.google.com/file/d/1ea3baHPePunw8bWNeAzygsfV9YXYI6Mc/view?usp=drive_link"

    try:
        # Descargar el archivo desde Google Drive
        output_file = "data.csv"
        gdown.download(url, output_file, quiet=False)

        # Leer el archivo CSV en un DataFrame
        df = pd.read_csv(output_file)

        # Mostrar los datos en Streamlit
        st.subheader("Contenido del DataFrame")
        st.write(df)
    except Exception as e:
        st.error(f"Error al descargar y mostrar los datos: {e}")

if __name__ == "__main__":
    main()
