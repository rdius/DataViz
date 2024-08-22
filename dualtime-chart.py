import matplotlib.pyplot as plt
import numpy as np
import time


"""
# Continuously stream data

You are responsible for monitoring temperature and humidity data from a set of IoT sensors in a smart building. 
Your goal is to create a real-time dashboard that updates every few seconds with the latest readings from the sensors.
"""

# Initialize real-time data simulation
np.random.seed(42)
temperature = [20 + np.random.normal(0, 1)]
humidity = [50 + np.random.normal(0, 2)]
times = [0]

plt.ion()  # Interactive mode for real-time plotting
fig, ax = plt.subplots(2, 1, figsize=(10, 6))

# Real-time plotting loop
for i in range(50):  # Simulate 50 time points
    temp_change = np.random.normal(0, 0.5)
    humidity_change = np.random.normal(0, 0.5)

    temperature.append(temperature[-1] + temp_change)
    humidity.append(humidity[-1] + humidity_change)
    times.append(i)

    # Update temperature plot
    ax[0].cla()
    ax[0].plot(times, temperature, color='r')
    ax[0].set_title("Real-Time Temperature Monitoring")
    ax[0].set_xlabel("Time")
    ax[0].set_ylabel("Temperature (°C)")

    # Update humidity plot
    ax[1].cla()
    ax[1].plot(times, humidity, color='b')
    ax[1].set_title("Real-Time Humidity Monitoring")
    ax[1].set_xlabel("Time")
    ax[1].set_ylabel("Humidity (%)")

    plt.draw()
    plt.pause(0.5)  # Simulate data arrival every half second



"""
Why dual-Line charts for real-Time sensor data?

Dual-line charts allow us to monitor multiple variables (temperature and humidity) simultaneously. 
Each variable is plotted on its own axis to avoid confusion and clutter, making it easy to spot trends in both metrics in real time.
"""
