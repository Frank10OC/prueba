import streamlit as st
import pandas as pd

dfa = pd.read_csv("https://datosabiertos.senace.gob.pe/home/VistaDatos/carteraproyectos?dataset=ESTUDIOS%20AMBIENTALES%20(APROBADO)&id=1&q=APROBADO#data")
# Mostrar el DataFrame en la aplicación de Streamlit
st.write(dfa)
