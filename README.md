### The Berlin Crime Analyst (A Web App) is an Interactive Multipage Dashboard created Using Dash <br>

Dash is a Python framework developed by Plotly to craft interactive web applications. Leveraging Flask, Plotly.js, and React.js, it provides a robust foundation. Dash empowers data scientists and engineers to seamlessly deliver intricate Python analytics to business decision-makers and operators through user-friendly applications. <br>

The Berlin Crime Analyst is a web software that allows you to analyze data on various sorts of crimes in Berlin over time and transform it into actionable information.

Why Create a Crime Data Visualization App in Berlin?
To answer these questions, 

1) Where in Berlin is the most dangerous? <br>
2) What is the rate of crime growth? <br>
3) What kinds of crimes are committed? <br>

#Must step- install all dependencies in the requirement.txt file

#Installing Dash( contains plotly for graph) using the terminal
pip install dash

#Installing Dash( contains plotly for graph)
pip install pandas

from dash import Dash, html, dcc 
import plotly.express as px 
import pandas as pd 

#Reading the data
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()
df = pd.read_csv(DATA_PATH.joinpath("berlin_crime.csv"))


app = Dash(__name__)

#Reading the data
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()

#Converting the berlin data from csv to a pandas dataframedf = pd.read_csv(DATA_PATH.joinpath("berlin_crime.csv"))

#To run app, type the following and click the link in the terminal
python index.py or python app.py
#click on the local deployed link
<img width="709" alt="image" src="https://github.com/natedotdev/thebelincrimeanalyst/assets/153172449/62e4d7d7-7bed-46c8-9509-487c4b41ddb1">
