# Data storage (Dash Python)
import dash
from dash import dcc, html, dash_table
import plotly.graph_objects as go

app = dash.Dash(__name__)


storage_systems = ["Ranch (TACC)", "Corral (TACC)", "Stockyard (TACC)", "HPSS (NCAR)", "Globus (NCAR)"]
capacities = [100, 10, 50, 70, 1.5]  


bar_chart = go.Figure(data=[
    go.Bar(name='Capacity (PB)', x=storage_systems, y=capacities)
])

bar_chart.update_layout(
    title='Comparison of Data Storage Capacities at TACC and NCAR',
    xaxis_title='Storage Systems',
    yaxis_title='Capacity (Petabytes)',
    legend_title='Metrics',
)


data = [
    ["Ranch (TACC)", "100 PB", "Encryption, Redundancy", "Globus, Web Access"],
    ["Corral (TACC)", "10 PB", "Encryption, Redundancy", "Globus, Web Access"],
    ["Stockyard (TACC)", "50 PB", "Encryption, Redundancy", "Globus, Web Access"],
    ["HPSS (NCAR)", "70 PB", "Encryption, Redundancy", "Globus, Web Access"],
    ["Globus (NCAR)", "1.5 PB", "Encryption, Redundancy", "Web Access"],
]

header = ["Storage System", "Capacity", "Security Features", "Accessibility Features"]

table = go.Figure(data=[go.Table(
    header=dict(values=header, line_color='darkslategray', fill_color='lightskyblue', font=dict(color='white', size=14)),
    cells=dict(values=list(map(list, zip(*data))), line_color='darkslategray', fill_color='lightcyan', font=dict(color='darkslategray', size=12))
)])

table.update_layout(width=800, height=300, title="Comparison of Data Storage and Management Solutions at TACC and NCAR")

app.layout = html.Div([
    dcc.Graph(id='comparison-chart', figure=bar_chart),
    dcc.Graph(id='comparison-table', figure=table)
])

if __name__ == '__main__':
    app.run_server(debug=True)
