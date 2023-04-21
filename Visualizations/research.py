# This has not been added to web.py

import dash
from dash import dcc, html
import plotly.graph_objects as go

app = dash.Dash(__name__)

data = [
    ["TACC", "Molecular Dynamics", "Simulation of protein folding and drug interactions"],
    ["TACC", "Fluid Dynamics", "Modeling of ocean currents and turbulence in aircraft engines"],
    ["TACC", "Astrophysics Simulations", "Simulation of galaxy formation and evolution"],
    ["NCAR", "Atmospheric Science", "Investigation of atmospheric chemistry and air quality"],
    ["NCAR", "Climate Science", "Study of climate change and its impacts on global ecosystems"],
    ["NCAR", "Earth System Science", "Analysis of interactions between the atmosphere, oceans, and terrestrial systems"],
]

header = ["Facility", "Research Domain", "Example Project"]

table = go.Figure(data=[go.Table(
    header=dict(values=header, line_color='darkslategray', fill_color='lightskyblue', font=dict(color='white', size=14)),
    cells=dict(values=list(map(list, zip(*data))), line_color='darkslategray', fill_color='lightcyan', font=dict(color='darkslategray', size=12))
)])

table.update_layout(width=1000, height=300, title="Comparison of Research Domains and Projects at TACC and NCAR")

app.layout = html.Div([
    dcc.Graph(id='research-domains-projects-table', figure=table)
])

if __name__ == '__main__':
    app.run_server(debug=True)
