### The Berlin Crime Analyst (A Web App) is an Interactive Multipage Dashboard created Using Dash <br>

Dash is a Python framework developed by Plotly to craft interactive web applications. Leveraging Flask, Plotly.js, and React.js, 
it provides a robust foundation. Dash empowers data scientists and engineers to seamlessly deliver intricate Python analytics to 
business decision-makers and operators through user-friendly applications. <br>

The Berlin Crime Analyst is a web software that allows you to analyze data on various sorts of crimes in Berlin over time and transform it into actionable information.
<br>
Why Create a Crime Data Visualization App in Berlin?<br>
To answer these questions, <br>

1) Where in Berlin is the most dangerous? <br>
2) What is the rate of crime growth? <br>
3) What kinds of crimes are committed? <br>
<br><br>
##Must step
<br>
install all dependencies in the requirement.txt file

#Installing Dash( contains plotly for graph) using the terminal <br>
pip install dash <br>
<br>
#Installing Dash( contains plotly for graph) <br>
pip install pandas<br>
<br>
from dash import Dash, html, dcc <br>
import plotly.express as px <br>
import pandas as pd <br>
<br>
#Reading the data <br>
PATH = pathlib.Path(__file__).parent<br>
DATA_PATH = PATH.joinpath("../datasets").resolve()<br>
df = pd.read_csv(DATA_PATH.joinpath("berlin_crime.csv"))<br>
<br><br>

app = Dash(__name__)<br>
<br>
#Reading the data<br>
PATH = pathlib.Path(__file__).parent<br>
DATA_PATH = PATH.joinpath("../datasets").resolve()<br>
<br>
#Converting the berlin data from csv to a pandas dataframedf = pd.read_csv(DATA_PATH.joinpath("berlin_crime.csv"))<br>
<br>
#To run app, type the following and click the link in the terminal<br>
python index.py or python app.py<br>
#click on the local deployed link<br>
<br>
