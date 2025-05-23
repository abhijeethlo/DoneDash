import dash
from dash import html, dcc
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import random

app = dash.Dash(__name__)
app.title = "Asset Scan Dashboard"

app.layout = html.Div([
    html.H1("🏗️ Smart Asset Scan Dashboard", style={'textAlign': 'center'}),
    
    html.Div([
        dcc.Graph(id='speedometer'),
        dcc.Graph(id='accuracy-meter'),
        dcc.Graph(id='health-gauge')
    ], style={'display': 'flex', 'justifyContent': 'space-around'}),

    dcc.Interval(
        id='interval-component',
        interval=2000,  # Update every 2 seconds
        n_intervals=0
    )
])

@app.callback(
    Output('speedometer', 'figure'),
    Output('accuracy-meter', 'figure'),
    Output('health-gauge', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_gauges(n):
    scan_rate = random.randint(20, 100)
    accuracy = random.uniform(85, 99)
    health = random.randint(50, 100)

    fig1 = go.Figure(go.Indicator(
        mode="gauge+number",
        value=scan_rate,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Scan Speed (Labels/min)"},
        gauge={
            'axis': {'range': [0, 120]},
            'bar': {'color': "lightblue"},
            'steps': [
                {'range': [0, 60], 'color': "lightgray"},
                {'range': [60, 120], 'color': "steelblue"}
            ]
        }
    ))

    fig2 = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=accuracy,
        delta={'reference': 90},
        title={'text': "AI Classification Accuracy (%)"},
        gauge={
            'axis': {'range': [80, 100]},
            'bar': {'color': "limegreen"},
            'steps': [
                {'range': [80, 90], 'color': "lightgray"},
                {'range': [90, 100], 'color': "lightgreen"}
            ]
        }
    ))

    fig3 = go.Figure(go.Indicator(
        mode="gauge+number",
        value=health,
        title={'text': "System Health (%)"},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "tomato"},
            'steps': [
                {'range': [0, 60], 'color': "mistyrose"},
                {'range': [60, 100], 'color': "salmon"}
            ]
        }
    ))

    return fig1, fig2, fig3

if __name__ == '__main__':
    app.run(debug=True)

