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
st.subheader("Cantidad de empresas importadoras por volumen de compra")
fig4 = px.bar(importadores, x="País", y="Cantidad de Importadores", color="Volumen de Compra", barmode="stack")
st.plotly_chart(fig4, use_container_width=True)

# Gráfico 5 - Tamaño de restaurantes
st.subheader("Cantidad de restaurantes por país y tamaño")
fig5 = px.bar(tamano_restaurantes, x="País", y="Cantidad", color="Tamaño", barmode="group")
st.plotly_chart(fig5, use_container_width=True)

# Gráfico 6 - Frecuencia de compra
st.subheader("Frecuencia de compra por tipo de restaurante")
fig6 = px.bar(frecuencia_compra, x="País", y="Frecuencia Promedio", color="Tipo de Restaurante", barmode="group")
st.plotly_chart(fig6, use_container_width=True)

# Gráfico 7 - Captación de perfiles clave
st.subheader("Nivel de captación de perfiles clave por país y tipo de restaurante")
fig7 = px.bar(captacion_perfiles, x="País", y="Nivel de Captación (%)", color="Tipo de Restaurante", barmode="group")
st.plotly_chart(fig7, use_container_width=True)

# Gráfico 8 - Penetración del mensaje
st.subheader("Nivel de penetración del mensaje por segmento y país")
fig8 = px.bar(penetracion_mensaje, x="Segmento", y="Penetración (%)", color="País", barmode="group")
st.plotly_chart(fig8, use_container_width=True)
