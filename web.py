import dash
from dash import dcc, html
import plotly.graph_objects as go


app = dash.Dash(__name__)



#Comparison chart code
comparison_chart = {
    'data': [
        {'x': ['Frontera (TACC)', 'Cheyenne (NCAR)'],
         'y': [23.5, 13.2],
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

#Storage capacity chart code
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

#Storage comparison table code
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

#Research domains and projects table code
data = [
    ["TACC", "Molecular Dynamics", "Simulation of protein folding and drug interactions"],
    ["TACC", "Fluid Dynamics", "Modeling of ocean currents and turbulence in aircraft engines"],
    ["TACC", "Astrophysics Simulations", "Simulation of galaxy formation and evolution"],
    ["NCAR", "Atmospheric Science", "Investigation of atmospheric chemistry and air quality"],
    ["NCAR", "Climate Science", "Study of climate change and its impacts on global ecosystems"],
    ["NCAR", "Earth System Science", "Analysis of interactions between the atmosphere, oceans, and terrestrial systems"],
]

header = ["Facility", "Research Domain", "Example Project"]

research_table = go.Figure(data=[go.Table(
header=dict(values=header, line_color='darkslategray', fill_color='lightskyblue', font=dict(color='white', size=14)),
cells=dict(values=list(map(list, zip(*data))), line_color='darkslategray', fill_color='lightcyan', font=dict(color='darkslategray', size=12))
)])

research_table.update_layout(width=1000, height=300, title="Comparison of Research Domains and Projects at TACC and NCAR")

#Pie Chart code

tacc_domains = ['Molecular Dynamics', 'Fluid Dynamics', 'Astrophysics Simulations', 'Other']
tacc_counts = [120, 110, 90, 250]

ncar_domains = ['Atmospheric Science', 'Climate Science', 'Earth System Science', 'Other']
ncar_counts = [180, 160, 140, 220]

research_domains_fig = go.Figure()

research_domains_fig.add_trace(go.Pie(labels=tacc_domains, values=tacc_counts, name="TACC", domain=dict(x=[0, 0.5], y=[0, 1])))
research_domains_fig.add_trace(go.Pie(labels=ncar_domains, values=ncar_counts, name="NCAR", domain=dict(x=[0.5, 1], y=[0, 1])))

research_domains_fig.update_layout(
    title='Research Domains at TACC and NCAR',
    legend_title='Domains',
    annotations=[
        dict(text='TACC', x=0.25, y=0.5, font_size=20, showarrow=False),
        dict(text='NCAR', x=0.75, y=0.5, font_size=20, showarrow=False)
    ]
)

#funding Chart
funding_sources = ["NSF", "DOE", "NIH", "Industry Partners", "Others"]
tacc_funding = [45, 25, 10, 15, 5]
ncar_funding = [70, 0, 0, 10, 20]

funding_chart = go.Figure()

funding_chart.add_trace(go.Bar(name="TACC", x=funding_sources, y=tacc_funding))
funding_chart.add_trace(go.Bar(name="NCAR", x=funding_sources, y=ncar_funding))

funding_chart.update_layout(
  title="Funding and Support Sources for TACC and NCAR (Estimate)",
  xaxis_title="Funding Sources",
  yaxis_title="Percentage of Total Funding",
  barmode="group",
  legend_title="Institutions"
)

#software ecosystem comparison


software_categories = ['Compilers', 'Debuggers', 'Performance Analysis Tools', 'Domain-specific Applications']
tacc_software_counts = [4, 2, 6, 60]  # Approximate counts for TACC
ncar_software_counts = [4, 3, 5, 50]  # Approximate counts for NCAR

software_fig = go.Figure()

software_fig.add_trace(go.Bar(name='TACC', x=software_categories, y=tacc_software_counts))
software_fig.add_trace(go.Bar(name='NCAR', x=software_categories, y=ncar_software_counts))

software_fig.update_layout(
    title='Comparison of Software Ecosystems at TACC and NCAR',
    xaxis_title='Software Categories',
    yaxis_title='Number of Tools and Libraries',
    barmode='group',
    legend_title='Institutions'
)


app.layout = html.Div([
    html.H1("Comparative Analysis of High-Performance Computing Facilities (TACC & NCAR)", style={'text-align': 'center'}),
    html.H2("A visualization website", style={'text-align': 'center'}),
    dcc.Graph(id='linpack-power-usage-chart', figure=comparison_chart),
    dcc.Graph(id='storage-capacity-chart', figure=bar_chart),
    dcc.Graph(id='storage-comparison-table', figure=table),
    dcc.Graph(id='research-domains-projects-table', figure=research_table),
    dcc.Graph(id='research-domains-pie-chart', figure=research_domains_fig),
    dcc.Graph(id='funding-chart', figure=funding_chart),
    dcc.Graph(id='software-ecosystem-chart', figure=software_fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)