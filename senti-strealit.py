import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

# Set up the title
st.title("Real-Time Sentiment Visualization")

# Initialize real-time sentiment data
sentiments = ['Positive', 'Negative', 'Neutral']
sentiment_counts = [0, 0, 0]

# Plot settings
fig, ax = plt.subplots()

# Simulate real-time sentiment data
with st.empty():
    for i in range(50):  # Simulate 50 time points
        new_sentiment = np.random.choice(sentiments, p=[0.5, 0.3, 0.2])

        # Update sentiment counts
        if new_sentiment == 'Positive':
            sentiment_counts[0] += 1
        elif new_sentiment == 'Negative':
            sentiment_counts[1] += 1
        else:
            sentiment_counts[2] += 1

        # Clear previous plot
        ax.cla()

        # Create a horizontal bar chart
        ax.barh(sentiments, sentiment_counts, color=['green', 'red', 'gray'])

        # Add labels and title
        ax.set_xlabel('Number of Mentions')
        ax.set_title('Real-Time Sentiment Analysis')

        # Display the plot
        st.pyplot(fig)

        # Simulate real-time data arrival every second
        time.sleep(1)
