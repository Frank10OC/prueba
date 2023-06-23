import streamlit as st
import pandas as pd
import gdown

def main():
    st.title("Cargar CSV desde Google Drive en Streamlit")

    # Enlace compartido del archivo CSV en Google Drive
    csv_url = "https://drive.google.com/file/d/1ea3baHPePunw8bWNeAzygsfV9YXYI6Mc/view?usp=drive_link"

    # Descargar el archivo CSV desde Google Drive
    output_csv = "data.csv"
    gdown.download(csv_url, output_csv, quiet=False)

    # Cargar el archivo CSV en un DataFrame
    df = pd.read_csv(output_csv)

    # Mostrar el DataFrame
    st.subheader("Contenido del archivo CSV")
    st.write(df)

if __name__ == "__main__":
    main()
import streamlit as st
import pandas as pd
import gdown

def main():
    st.title("Mostrar datos de Google Drive en Streamlit")

    # Enlace compartido del archivo en Google Drive
    file_url = "https://drive.google.com/file/d/1ea3baHPePunw8bWNeAzygsfV9YXYI6Mc/view?usp=drive_link"

    # Descargar el archivo desde Google Drive
    output_file = "data.csv"
    gdown.download(file_url, output_file, quiet=False)

    # Cargar el archivo en un DataFrame
    df = pd.read_csv(output_file)

    # Mostrar el DataFrame
    st.subheader("Contenido del archivo")
    st.write(df)

if __name__ == "__main__":
    main()

