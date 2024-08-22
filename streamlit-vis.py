import streamlit as st
import numpy as np
import pandas as pd
import time

# Set up the title
st.title("Real-Time Sensor Data Monitoring")

# Initialize empty lists to hold sensor data
temperature = []
humidity = []

# Simulate real-time sensor data
with st.empty():
    for i in range(100):
        # Generate random sensor data
        new_temperature = np.random.normal(25, 2)
        new_humidity = np.random.uniform(30, 50)

        # Append to lists
        temperature.append(new_temperature)
        humidity.append(new_humidity)

        # Create a dataframe for plotting
        sensor_data = pd.DataFrame({'Temperature (°C)': temperature, 'Humidity (%)': humidity})

        # Plot the data using Streamlit's built-in charting functions
        st.line_chart(sensor_data,use_container_width=True)

        # Pause for a short interval to simulate real-time updates
        time.sleep(0.5)
