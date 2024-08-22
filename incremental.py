import pandas as pd
import numpy as np

"""
# 
You are working with streaming data from multiple weather stations that record temperature data every minute. 
Your goal is to visualize the temperature data over time, updating the graph incrementally.
"""

# Simulated temperature data from weather stations
weather_data = {'Station': ['A', 'B', 'C'],
                'Temperature': [np.random.randint(15, 35) for _ in range(3)]}
df = pd.DataFrame(weather_data)


import plotly.graph_objects as go
import pandas as pd
import numpy as np
import time

# Initialize the plot
fig = go.FigureWidget()

# Simulate streaming data
for _ in range(5):  # Simulate 5 time points.
    temp_data = {'Station': ['A', 'B', 'C'],
                 'Temperature': [np.random.randint(15, 35) for _ in range(3)]}
    df = pd.DataFrame(temp_data)

    fig.add_trace(go.Scatter(x=df['Station'], y=df['Temperature'], mode='lines+markers'))
    fig.show()

    time.sleep(1)  # Simulate data streaming every second

"""
Why Incremental Line Graphs ? --> Note that this is not suitable for a large range.

When dealing with streaming data, incremental updates using line graphs are effective for visualizing how 
variables change over time. This method keeps the visualization up-to-date as new data points come in, making it ideal for real-time monitoring.
"""
