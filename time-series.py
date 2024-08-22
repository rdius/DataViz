import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set up the title
st.title("Time Series Data Visualization")

# Generate a date range and random stock price data
dates = pd.date_range(start="2023-01-01", periods=365)
prices = np.cumsum(np.random.randn(365)) + 100  # Simulated stock prices

# Create a DataFrame
df = pd.DataFrame({'Date': dates, 'Price': prices})

# Display a line chart using Streamlit
st.line_chart(df.set_index('Date'))

# Allow user to adjust moving average window
window = st.slider('Moving Average Window', 1, 30, 5)

# Calculate and plot moving average
df['Moving_Avg'] = df['Price'].rolling(window=window).mean()

# Plotting with Matplotlib
st.write("Stock Prices with Moving Average")
fig, ax = plt.subplots()
ax.plot(df['Date'], df['Price'], label='Price', color='blue')
ax.plot(df['Date'], df['Moving_Avg'], label=f'{window}-Day Moving Average', color='red')
ax.legend()
st.pyplot(fig)
