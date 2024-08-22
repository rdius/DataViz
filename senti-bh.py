import matplotlib.pyplot as plt
import numpy as np
import time

# Set up sentiment categories and initial counts
sentiments = ['Positive', 'Negative', 'Neutral']
sentiment_counts = [0, 0, 0]

# Initialize the plot
fig, ax = plt.subplots()

# Simulate real-time data updates
for i in range(50):  # Simulate 50 time points
    new_sentiment = np.random.choice(sentiments, p=[0.5, 0.3, 0.2])

    # Update sentiment counts
    if new_sentiment == 'Positive':
        sentiment_counts[0] += 1
    elif new_sentiment == 'Negative':
        sentiment_counts[1] += 1
    else:
        sentiment_counts[2] += 1

    # Clear the plot
    ax.cla()

    # Create horizontal bar chart
    ax.barh(sentiments, sentiment_counts, color=['green', 'red', 'gray'])

    # Add labels and title
    ax.set_xlabel('Number of Mentions')
    ax.set_title('Real-Time Sentiment Analysis')

    # Redraw the plot
    plt.pause(1)  # Pause for 1 second to simulate real-time updates

# Keep the plot open after the loop ends
plt.show()
