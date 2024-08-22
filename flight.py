import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression


"""
You work for an airline, and your task is to build a real-time dashboard that predicts whether flights will 
be delayed based on incoming weather, traffic, and airport data. The dashboard should visualize the predicted delay 
probability for each flight and highlight high-risk flights.

"""


# Simulate pre-trained machine learning model
model = LogisticRegression()
model.coef_ = np.array([[0.5, -0.5, 0.3]])  # Simulated coefficients
model.intercept_ = np.array([-1.0])
model.classes_ = np.array([0, 1])  # 0 = No Delay, 1 = Delay

# Initialize real-time flight data simulation
flight_ids = ['Flight_1', 'Flight_2', 'Flight_3']
delays = []
times = []

plt.ion()  # Interactive mode for real-time plotting
fig, ax = plt.subplots(figsize=(10, 6))

# Real-time prediction loop
for i in range(30):  # Simulate 30 flights
    # Simulate incoming flight data (weather, traffic, etc.)
    flight_data = np.random.normal(0, 1, (3, 3))

    # Predict delay probabilities using the model
    delay_probs = model.predict_proba(flight_data)[:, 1]  # Probability of delay

    delays.append(delay_probs)
    times.append(i)

    # Clear previous plots
    ax.cla()

    # Plot delay probabilities for each flight
    for j in range(len(flight_ids)):
        ax.plot(times, [d[j] for d in delays], label=flight_ids[j], marker='o')

    ax.axhline(0.5, color='red', linestyle='--', label='Delay Threshold')
    ax.set_title("Real-Time Flight Delay Prediction")
    ax.set_xlabel("Time")
    ax.set_ylabel("Probability of Delay")
    ax.legend()

    plt.draw()
    plt.pause(1)  # Simulate data arrival every second


"""
Why predictive modeling in Real-Time?

Predictive modeling enables real-time decision-making. By continuously predicting the likelihood of flight delays, 
airlines can proactively manage schedules, rebook passengers, and minimize the impact of delays on operations.
"""
