import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import numpy as np
from dash.dependencies import Input, Output

# Initialize the app
app = dash.Dash(__name__)

# Simulated real-time data
countries = ['USA', 'Brazil', 'India', 'Russia', 'South Africa']
data = {
    'Country': np.random.choice(countries, 100),
    'Active Cases': np.random.randint(1000, 100000, 100),
    'Recoveries': np.random.randint(1000, 80000, 100),
    'Deaths': np.random.randint(100, 10000, 100)
}
df = pd.DataFrame(data)

# App layout
app.layout = html.Div([
    dcc.Dropdown(id='country-dropdown', options=[{'label': c, 'value': c} for c in countries], value='USA'),
    dcc.Graph(id='covid-map'),
    dcc.Graph(id='covid-trend')
])

# Update the map based on selected country
@app.callback(
    Output('covid-map', 'figure'),
    [Input('country-dropdown', 'value')]
)
def update_map(selected_country):
    filtered_df = df[df['Country'] == selected_country]
    fig = px.scatter_mapbox(filtered_df, lat=np.random.uniform(-90, 90, len(filtered_df)),
                            lon=np.random.uniform(-180, 180, len(filtered_df)),
                            size='Active Cases', color='Active Cases',
                            mapbox_style="open-street-map",
                            title=f'COVID-19 Active Cases in {selected_country}')
    return fig

# Update the trend chart based on selected country
@app.callback(
    Output('covid-trend', 'figure'),
    [Input('country-dropdown', 'value')]
)
def update_trend(selected_country):
    filtered_df = df[df['Country'] == selected_country]
    fig = px.line(filtered_df, x=np.arange(len(filtered_df)), y='Active Cases', title=f'COVID-19 Trend in {selected_country}')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
