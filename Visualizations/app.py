#LINPACK and Power Usage Visualization

import dash
from dash import dcc, html

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(
        id='comparison-chart',
        figure={
            'data': [
                {'x': ['Frontera (TACC)', 'Cheyenne (NCAR)'],
                 'y': [23.5, 1.26],
                 'type': 'bar',
                 'name': 'LINPACK Performance (petaflops)'},
                {'x': ['Frontera (TACC)', 'Cheyenne (NCAR)'],
                 'y': [3.5, 2],
                 'type': 'bar',
                 'name': 'Power Usage (megawatts)'},
            ],
            'layout': {
                'title': 'Comparison of LINPACK Performance and Power Usage for Frontera (TACC) and Cheyenne (NCAR)',
                'xaxis': {'title': 'Supercomputers'},
                'yaxis': {'title': 'Value'},
                'legend': {'title': 'Metrics'},
                'barmode': 'group'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
