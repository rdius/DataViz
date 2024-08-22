import matplotlib.pyplot as plt
import numpy as np
import time

# Simulate real-time sentiment data
sentiments = ['Positive', 'Negative', 'Neutral']
sentiment_counts = [0, 0, 0]

plt.ion()  # Interactive mode for real-time plotting

# Real-time sentiment pie chart
for i in range(50):  # Simulate 50 time points
    new_sentiment = np.random.choice(sentiments, p=[0.5, 0.3, 0.2])

    # Update sentiment counts
    if new_sentiment == 'Positive':
        sentiment_counts[0] += 1
    elif new_sentiment == 'Negative':
        sentiment_counts[1] += 1
    else:
        sentiment_counts[2] += 1

    # Update pie chart
    plt.cla()
    plt.pie(sentiment_counts, labels=sentiments, autopct='%1.1f%%', colors=['green', 'red', 'gray'])
    plt.title("Real-Time Sentiment Analysis")

    plt.draw()
    plt.pause(1)  # Simulate data arrival every second
