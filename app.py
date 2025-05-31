import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# Cargar los datos CSV
importaciones = pd.read_csv('01_Importaciones.csv')
segmentacion = pd.read_csv('02_Segmentacion_Cocina.csv')
edades = pd.read_csv('03_Edades_Duenos.csv')
importadores = pd.read_csv('04_Importadores.csv')
tamano_restaurantes = pd.read_csv('05_Tamano_Restaurantes.csv')
frecuencia_compra = pd.read_csv('06_Frecuencia_Compra.csv')
captacion_perfiles = pd.read_csv('07_Captacion_Perfiles.csv')
penetracion_mensaje = pd.read_csv('08_Penetracion_Mensaje.csv')

# Iniciar la app Dash
app = dash.Dash(__name__)
app.title = "Dashboard - Alimentos Asiáticos en Centroamérica"

app.layout = html.Div([
    html.H1("Dashboard Estratégico - Exportaciones de Alimentos Asiáticos", style={"textAlign": "center"}),

    dcc.Graph(
        id='importaciones',
        figure=px.line(importaciones, x="Año", y="Importaciones (USD)", color="País", title="Evolución de importaciones (2020-2025)")
    ),

    dcc.Graph(
        id='segmentacion-cocina',
        figure=px.bar(segmentacion, x="País", y="Cantidad", color="Tipo de Cocina", title="Segmentación por tipo de cocina")
    ),

    dcc.Graph(
        id='edades-duenos',
        figure=px.box(edades, x="País", y="Edad", title="Distribución de edades de dueños de restaurantes")
    ),

    dcc.Graph(
        id='importadores',
        figure=px.bar(importadores, x="País", y="Cantidad de Importadores", color="Volumen de Compra", title="Empresas importadoras por volumen")
    ),

    dcc.Graph(
        id='tamano-restaurantes',
        figure=px.bar(tamano_restaurantes, x="País", y="Cantidad", color="Tamaño", title="Cantidad de restaurantes por tamaño")
    ),

    dcc.Graph(
        id='frecuencia-compra',
        figure=px.bar(frecuencia_compra, x="País", y="Frecuencia Promedio", color="Tipo de Restaurante", title="Frecuencia de compra por tipo de restaurante")
    ),

    dcc.Graph(
        id='captacion-perfiles',
        figure=px.bar(captacion_perfiles, x="País", y="Nivel de Captación (%)", color="Tipo de Restaurante", title="Captación de perfiles clave")
    ),

    dcc.Graph(
        id='penetracion-mensaje',
        figure=px.bar(penetracion_mensaje, x="Segmento", y="Penetración (%)", color="País", barmode="group", title="Penetración del mensaje por segmento")
    ),
])

if __name__ == '__main__':
    app.run_server(debug=True)
