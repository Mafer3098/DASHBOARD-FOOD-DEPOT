import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide", page_title="Dashboard - Alimentos Asiáticos")

st.title("📊 Dashboard Estratégico - Alimentos Asiáticos en Centroamérica")

# Cargar archivos CSV
importaciones = pd.read_csv("01_Importaciones.csv")
segmentacion = pd.read_csv("02_Segmentacion_Cocina.csv")
edades = pd.read_csv("03_Edades_Duenos.csv")
importadores = pd.read_csv("04_Importadores.csv")
tamano_restaurantes = pd.read_csv("05_Tamano_Restaurantes.csv")
frecuencia_compra = pd.read_csv("06_Frecuencia_Compra.csv")
captacion_perfiles = pd.read_csv("07_Captacion_Perfiles.csv")
penetracion_mensaje = pd.read_csv("08_Penetracion_Mensaje.csv")

# Gráfico 1 - Importaciones
st.subheader("Evolución de importaciones de productos asiáticos (2020-2025)")
fig1 = px.line(importaciones, x="Ano", y="Importaciones (USD)", color="Pais", markers=True)
st.plotly_chart(fig1, use_container_width=True)

# Gráfico 2 - Segmentación por tipo de cocina
st.subheader("Segmentación de restaurantes por especialización de cocina")
fig2 = px.bar(segmentacion, x="País", y="Cantidad de Restaurantes", color="Cocina", barmode="group")
st.plotly_chart(fig2, use_container_width=True)

# Gráfico 3 - Edades de dueños
st.subheader("Distribución de edades de dueños de restaurantes por país")
fig3 = px.box(edades, x="País", y="Edad Dueño", points="all")
st.plotly_chart(fig3, use_container_width=True)

# Gráfico 4 - Importadores por volumen
importadores_count = importadores.groupby("País").size().reset_index(name="Cantidad de Importadores")
st.subheader("Cantidad de empresas importadoras por país")
fig4 = px.bar(importadores_count, x="País", y="Cantidad de Importadores", barmode="stack")
st.plotly_chart(fig4, use_container_width=True)

# Gráfico 5 - Tamaño de restaurantes
fig5 = px.bar(
    tamano_restaurantes,
    x="País",
    y="Cantidad de Restaurantes",
    color="Tamaño",
    barmode="group"
)
st.plotly_chart(fig5, use_container_width=True)

# Gráfico 6 - Frecuencia de compra
fig6 = px.bar(
    frecuencia_compra,
    x="País",
    y="Porcentaje",
    color="Tipo de Restaurante",
    barmode="group"
)
st.plotly_chart(fig6, use_container_width=True)

# Gráfico 7 - Captación de perfiles clave
fig7 = px.bar(
    captacion_perfiles,
    x="País",
    y="Nivel de Captación (%)",
    color="Perfil Clave",
    barmode="group"
)

# Gráfico 8 - Penetración del mensaje
fig8 = px.bar(
    penetracion_mensaje,
    x="Segmento",
    y="Penetración del Mensaje (%)",
    color="País",
    barmode="group"
)
