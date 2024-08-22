import psutil  # System performance monitoring (use for real data)
import matplotlib.pyplot as plt
import time


"""
You are in charge of monitoring server performance, specifically CPU usage and memory utilization. 
Your goal is to create a real-time dashboard that displays live updates of CPU and memory usage.

"""

# Initialize real-time data simulation
cpu_usage = [psutil.cpu_percent(interval=1)]
memory_usage = [psutil.virtual_memory().percent]
times = [0]

plt.ion()  # Interactive mode for real-time plotting
fig, ax = plt.subplots(2, 1, figsize=(10, 6))

# Real-time plotting loop
for i in range(50):  # Simulate 50 time points
    cpu_usage.append(psutil.cpu_percent(interval=1))
    memory_usage.append(psutil.virtual_memory().percent)
    times.append(i)

    # Update CPU usage plot
    ax[0].cla()
    ax[0].plot(times, cpu_usage, color='g')
    ax[0].set_title("Real-Time CPU Usage Monitoring")
    ax[0].set_xlabel("Time")
    ax[0].set_ylabel("CPU Usage (%)")

    # Update memory usage plot
    ax[1].cla()
    ax[1].plot(times, memory_usage, color='c')
    ax[1].set_title("Real-Time Memory Usage Monitoring")
    ax[1].set_xlabel("Time")
    ax[1].set_ylabel("Memory Usage (%)")

    plt.draw()
    plt.pause(1)  # Simulate data arrival every second



"""
Why line charts for Real-Time performance monitoring?

Line charts are ideal for tracking metrics that change over time, such as CPU and memory usage. 
These visualizations allow for easy identification of trends, anomalies, and spikes in resource usage, which are critical for monitoring server health in real tim

"""
