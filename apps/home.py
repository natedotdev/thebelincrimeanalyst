from turtle import width
import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
import plotly.express as px
from dash.dependencies import Input, Output, State
import pandas as pd
from app import app

#Image Card for the home page
image_card = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4("The Berlin Crime Analyst", className="card-title", style={"padding":20, "text-align": "center"}),
                dbc.CardImg(src="../assets/analyst.png")
            ]
        ),
    ],
    className="h-100",
    color="warning",
)

#Text body for the home page
graph_card = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4("Data Exploratory and Visualization of Berlin Crime", className="card-title", style={"text-align": "center",
                                                                                         "color": "black", "padding":20}),
                
                html.P("The display of data in a pictorial or graphical form is known as data visualisation. This form aids top management and goverment leaders in visualising data, communicating messages about complex subjects, and spotting new trends. The way data is handled is determined by how each individual interprets it. Diagrams or graphs are more effective than tables or statements for displaying large amounts of complex data."),
                html.P("In this assignment, we use the Python programming language and the Plotly Dash module to process and visualise crime report data from 2012 to 2019 in Berlin."),
                html.P("The following steps were taken in the approach: data gathering, data exploration, variable identification, data preprocessing, preparing Python dependencies, charting the data, and creating a web app for the data for easy interaction.Plotly has a characteristic that no other visualisation library does: it is interactive. This allows viewers to interact with graphs on the screen, making it easier to follow and comprehend the tale."),
                dbc.CardImg(src="../assets/berlin.jpg", style={ 'width':'50%', "text-align": "center"})
            ],
        ),
    ],
    className="h-100",
    color="light",
)

#Layout of home page
layout = html.Div([
                dbc.Row([dbc.Col(image_card, width=3, style={"height": "100%"}),
                         dbc.Col(graph_card, width=8, style={"height": "50%"})],
                        align="stretch", justify="around", style={"height": "100vh"})
                ])
