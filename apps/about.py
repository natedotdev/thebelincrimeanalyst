import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
import plotly.express as px
from dash.dependencies import Input, Output, State
from app import app

card_main = dbc.Card(
    [
        dbc.CardImg(src="/assets/analyst.png", top=True, bottom=False, style={ 'width':'50%', "text-align": "center"},
                    title="The Berlin Crime Analyst"),
        dbc.CardBody(
            [
                html.H4("Data Visualization for Crime In Berlin", className="card-title"),
                html.P(
                    "The Berlin Crime Analyst is an application designed to analyse data collected over time and make connections and meaning of it. " + " " +
                    "The reason for this application is to allow flexibity and scaling when you have to deploy a bigger and a more complicated version." + " " +
                    "You don't need to understand HTML, CSS, or Javascript to develop interactive dashboards with Plotly Dash; all you need is Python.",
                    className="card-text",
                ),
                html.Br(),
                html.H4("Developed By Nathaniel Alabi-Ga Annang", className="card-title"),
                html.P("References: https://dash.plotly.com/ | https://github.com/Coding-with-Adam/Dash-by-Plotly/" + " " +
                     "Email for more information and project inquiry: nate.annang@gmail.com",
                     className="card-text",
                ),
            ]
        ),
    ],
    color="dark",
    inverse=True,   
    outline=False,  
)

layout = html.Div([
    dbc.Row([dbc.Col(card_main, width=6,)], justify="center"),
])

