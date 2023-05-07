# Funding Visualizations

import dash
from dash import dcc, html
import plotly.graph_objects as go

app = dash.Dash(__name__)


funding_sources = ["NSF", "DOE", "NIH", "Industry Partners", "Others"]
tacc_funding = [45, 25, 10, 15, 5]
ncar_funding = [70, 0, 0, 10, 20]

fig = go.Figure()

fig.add_trace(go.Bar(name="TACC", x=funding_sources, y=tacc_funding))
fig.add_trace(go.Bar(name="NCAR", x=funding_sources, y=ncar_funding))

fig.update_layout(
    title="Funding and Support Sources for TACC and NCAR (Estimate)",
    xaxis_title="Funding Sources",
    yaxis_title="Percentage of Total Funding",
    barmode="group",
    legend_title="Institutions"
)

app.layout = html.Div([
    dcc.Graph(id="funding-chart", figure=fig)
])

if __name__ == "__main__":
    app.run_server(debug=True)
