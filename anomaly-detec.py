import matplotlib.pyplot as plt
import numpy as np
import time



"""
# Real-Time anomaly detection in server performance

You are responsible for monitoring a server cluster's performance. The real-time dashboard 
should continuously update with CPU and memory usage, and it should highlight anomalies when usage exceeds predefined 
thresholds (e.g., CPU > 85% or Memory > 90%).
"""


# Initialize simulation of real-time server performance data
cpu_usage = [np.random.uniform(20, 50)]
memory_usage = [np.random.uniform(30, 60)]
times = [0]

plt.ion()  # Interactive mode for real-time plotting
fig, ax = plt.subplots(2, 1, figsize=(10, 6))

# Thresholds for anomaly detection
cpu_threshold = 85
memory_threshold = 90

# Real-time plotting loop
for i in range(100):  # Simulate 100 time points
    cpu_change = np.random.uniform(-5, 5)
    memory_change = np.random.uniform(-3, 3)

    # Simulate occasional anomalies
    if i % 20 == 0:
        cpu_usage.append(np.random.uniform(85, 100))  # Spike in CPU usage
        memory_usage.append(np.random.uniform(90, 100))  # Spike in memory usage
    else:
        cpu_usage.append(cpu_usage[-1] + cpu_change)
        memory_usage.append(memory_usage[-1] + memory_change)

    times.append(i)

    # Clear previous plots
    ax[0].cla()
    ax[1].cla()

    # Plot CPU usage
    ax[0].plot(times, cpu_usage, color='blue', label='CPU Usage')
    ax[0].axhline(cpu_threshold, color='red', linestyle='--', label=f'CPU Threshold: {cpu_threshold}%')
    if cpu_usage[-1] > cpu_threshold:
        ax[0].scatter([i], [cpu_usage[-1]], color='red', s=100, label='Anomaly')

    ax[0].set_title("Real-Time CPU Usage Monitoring with Anomaly Detection")
    ax[0].set_xlabel("Time")
    ax[0].set_ylabel("CPU Usage (%)")
    ax[0].legend()

    # Plot Memory usage
    ax[1].plot(times, memory_usage, color='green', label='Memory Usage')
    ax[1].axhline(memory_threshold, color='red', linestyle='--', label=f'Memory Threshold: {memory_threshold}%')
    if memory_usage[-1] > memory_threshold:
        ax[1].scatter([i], [memory_usage[-1]], color='red', s=100, label='Anomaly')

    ax[1].set_title("Real-Time Memory Usage Monitoring with Anomaly Detection")
    ax[1].set_xlabel("Time")
    ax[1].set_ylabel("Memory Usage (%)")
    ax[1].legend()

    plt.draw()
    plt.pause(0.5)  # Simulate data arrival every half second


"""
Why anomaly detection?

Anomaly detection is crucial in performance monitoring to quickly identify potential problems 
before they impact operations. Real-time monitoring with thresholds allows system administrators to take proactive measures.
"""
