import streamlit as st
import pandas as pd

dfa = pd.read_csv("https://raw.githubusercontent.com/Frank10OC/prueba/main/Reporte_Proyecto_APROBADO%20(4).csv")
# Mostrar el DataFrame en la aplicación de Streamlit
st.write(dfa)
