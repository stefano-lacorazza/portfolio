import dash
from dash import dcc, html
from dash.dependencies import MATCH, ALL
from django_plotly_dash import DjangoDash
from django.core.cache import cache
from django.utils.translation import gettext, gettext_lazy
import plotly.graph_objs as go
import dpd_components as dpd
from django_plotly_dash.consumers import send_to_pipe_channel
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import geopandas as gpd
import urllib.request, json 
app = DjangoDash('Fuel_visualization')   # replaces dash.Dash

app.layout = html.Div(
    [
        html.H4("Gas"),
        html.P(
            "<p> The scatter_geo graph is a type of data visualization that displays individual data points on a geographic map. It helps to visually represent the relationship or distribution of data across different locations, providing insights into spatial patterns and correlations </p> "
            "<p>The density_mapbox is  used for creating density heatmaps on Mapbox maps. It allows you to visualize the density of data points across a geographic area by aggregating data and representing it with color intensity.</p> "
            "<p>The Choropleth Map is a type of data visualization that represents data using different colors or patterns on a geographic map. It is used to display spatial variations of a specific variable across different regions, such as countries, states, or administrative districts.</p>"
        ),
        html.P(
            "Enter the type of graph you want to plot:"
        ),
        dcc.Dropdown(
            id="type",
            options=["Density mapbox", "Scatter_geo", "Choropleth"],
            value="Density mapbox",
            clearable=False,
        ),
        dcc.Graph(id="graph", figure={"layout": {
            "title": "My Dash Graph",
            "height": 700,  # px
        }}),
        
        

        
        
    ]
)


@app.callback(
    Output("graph", "figure"),
    Input("type", "value"),
)






def generate_chart(values):
   
    with urllib.request.urlopen("https://www.datos.gov.co/resource/fbht-2fzd.json") as url:
        df = pd.read_json(url)
        df2 = df[['departamento','volumen_despachado']]
        df3 = df2.groupby(['departamento'])['volumen_despachado'].sum().to_frame()
        df = df[['volumen_despachado', 'latitud', 'longitud', 'departamento_proveedor']]


    if values == "Density mapbox":
        
        fig = px.density_mapbox(df, lat='latitud', lon='longitud', z='volumen_despachado', zoom=5,
                        mapbox_style="stamen-terrain")

        fig.update_layout(mapbox_style="open-street-map")
        fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

    elif values == "Choropleth":
        
        geodf = gpd.read_file('C:/Users/laco-/Documents/Notebooks/MGN_DPTO_POLITICO.shp')
        #geodf["rand"] = np.random.randint(1, 100, len(geodf))
        # shape file is a different CRS,  change to lon/lat GPS co-ordinates
        geodf = geodf.to_crs("WGS84")
        geodf = geodf[['DPTO_CNMBR', 'geometry']]
        geodf= geodf.rename(columns={"DPTO_CNMBR": "departamento"})
        geodf = geodf.merge(df3,on='departamento')
        
        fig = px.choropleth_mapbox(
        geodf.set_index("departamento"),
        geojson=geodf.geometry,
        locations=geodf.index,
        color="volumen_despachado",
        center=dict(lat=4.11, lon=-74.3),
        mapbox_style="open-street-map",
        zoom=5,)
    
    
       
    

    else:
        fig = px.scatter_mapbox(
                    df, lat='latitud', lon='longitud', size='volumen_despachado',
                    zoom=5,)
                
        fig.update_layout(mapbox_style="open-street-map")
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)