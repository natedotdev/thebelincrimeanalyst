import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
import plotly.express as px
from dash.dependencies import Input, Output, State
import pandas as pd
import pathlib
from app import app

import warnings
warnings.filterwarnings('ignore')

#Reading the data
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()

df = pd.read_csv(DATA_PATH.joinpath("berlin_crime.csv"))

#Modal
modal = html.Div(
    [
        dbc.Button("Add comment", color="primary", id="open"),

        dbc.Modal([
            dbc.ModalHeader("Share your feedback"),
            dbc.ModalBody(
                dbc.Form(
                    [
                        dbc.FormGroup(
                            [
                                dbc.Label("Name", className="mr-2"),
                                dbc.Input(type="text", placeholder="Enter your name"),
                            ],
                            className="mr-3",
                        ),
                        dbc.FormGroup(
                            [
                                dbc.Label("Email", className="mr-2"),
                                dbc.Input(type="email", placeholder="Enter email"),
                            ],
                            className="mr-3",
                        ),
                        dbc.FormGroup(
                            [
                                dbc.Label("Comment", className="mr-2"),
                                dbc.Input(type="text", placeholder="Enter comment"),
                            ],
                            className="mr-3",
                        ),
                        dbc.Button("Submit", color="primary"),
                    ],
                    inline=False,
                )
            ),
            dbc.ModalFooter(
                dbc.Button("Close", id="close", className="ml-auto")
            ),

        ],
            id="modal_arson",
            is_open=False,    # True, False
            size="xl",        # "sm", "lg", "xl"
            backdrop=True,    # True, False or Static for modal to not be closed by clicking on backdrop
            scrollable=True,  # False or True if modal has a lot of text
            centered=True,    # True, False
            fade=True         # True, False
        ),
    ]
)

alert = dbc.Alert("Please choose Districts from dropdown in order to visualize the results!", color="danger",
                  dismissable=True),

#Image Card
image_card = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4("Arson Cases in Berlin", className="card-title", style={"padding":10}),
                dbc.CardImg(src="../assets/arson2.jpg", title="Arson"),
                html.H6("Choose Berlin Districts:", className="card-text", style={"padding":10}),
                html.Div(id="the_alert_arson", children=[]),
                dcc.Dropdown(id='district_chosen', options=[{'label': d, "value": d} for d in df["District"].unique()],
                             value=["Lichtenberg", "Pankow", "Spandau"], multi=True, style={"color": "#000000"}),
                html.Hr(),
                modal
            ]
        ),
    ],
    className="h-100",
    color="light",
)

#Graph Card
graph_card = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4("Arson Cases in Berlin 2012-2019", className="card-title", style={"text-align": "center",
                                                                                       "color": "black"}),
                dbc.Button(
                    "About Web App", id="popover-bottom-target", color="info"
                ),
                dbc.Popover(
                    [
                        dbc.PopoverHeader("About: The Berlin Crime Analyst"),
                        dbc.PopoverBody(
                            "The Data Visualization app is a first-generation application for examining and displaying crime data in Berlin. This app's functions are confined to one city and will be enhanced for subsequent cities and the country as a whole."),
                    ],
                    id="popover_arson",
                    target="popover-bottom-target",  # needs to be the same as dbc.Button id
                    placement="bottom",
                    is_open=False,
                ),
                dcc.Graph(id='line_chart_arson', figure={}),
            ],
        ),
    ],
    className="h-100",
    color="light",
)

#Layout
layout = html.Div([
    dbc.Row([dbc.Col(image_card, width=3), dbc.Col(graph_card, width=8)], align="stretch", justify="around")
])

@app.callback(
    Output("popover_arson", "is_open"),
    [Input("popover-bottom-target", "n_clicks")],
    [State("popover_arson", "is_open")],
)
def toggle_popover(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    [Output("line_chart_arson", "figure"),
     Output("the_alert_arson", "children")],
    [Input("district_chosen", "value")]
)
def update_graph_card(districts):
    if len(districts) == 0:
        return dash.no_update, alert
    else:
        df_filtered = df[df["District"].isin(districts)]
        df_filtered = df_filtered.groupby(["Year", "District"])[['Arson']].median().reset_index()
        fig = px.line(df_filtered, x="Year", y="Arson", color="District",
                      labels={"Arson": "Arson Cases (avg)"}).update_traces(mode='lines+markers')
        return fig, dash.no_update

@app.callback(
    Output("modal_arson", "is_open"),
    [Input("open", "n_clicks"), Input("close", "n_clicks")],
    [State("modal_arson", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    ctx = dash.callback_context
    if ctx.triggered:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        if button_id == "open":
            return not is_open
        else:
            return not is_open
    return is_open



