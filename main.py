# This project is developed with the aim of completing an assignment.
# Project Title:
# Efficient Data Stream Anomaly Detection

# Project Description:
# Your task is to develop a Python script capable of detecting anomalies in a continuous data stream. This stream, simulating real-time sequences of floating-point numbers, could represent various metrics such as financial transactions or system metrics. Your focus will be on identifying unusual patterns, such as exceptionally high values or deviations from the norm.

# Dependencies are subjected to minimal usage and are only utilised for the purpose of plotting and visualizing the operations.
# Dependencies include numpy, matplotlib, scipy.

# Summary
# 1. Data Generation: The data_stream function simulates a time series with fluctuating values, incorporating seasonal patterns, noise, and sudden anomalies, ensuring non-negative output.
# 2. Anomaly Detection: The ZScoreAnomalyDetector class identifies anomalies using a Z-score method, comparing current data against historical data within a sliding window.
# 3. Real-time Plotting: The live_plot function uses Matplotlib to create a real-time plot of the data stream, with visual indicators for detected anomalies and adjustable y-axis limits.
# 4. CSV Export: Anomalies detected are saved to a CSV file when a button is clicked, including time, value, mean, and deviation.
# 5. Interactive Features: The plot includes a save button to export data and dynamically updates the plot limits based on data range to ensure readability.

# Algorithmic method and its effectiveness - Z score method
# Statistical point of difference: By measuring how many standard deviations a data point is from the mean, the Z-score helps identify outliers that deviate significantly from typical data patterns. 
# Effectiveness:  
# Z-score is calculated in real-time as new data arrives.
# Z-score can effectively identify anomalies in environments where the data distribution might change over time.

#Limitation: the Z-score method works best when the data is spread out in a roughly bell-shaped (normal) curve. It might not be as effective if the data is heavily skewed or has extreme outliers, as it relies on the assumption that most data points are close to the average and only a few are far away.


# Code 
import numpy as np
import random
from collections import deque
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button
import csv

# Data Stream Generator
def data_stream():
    t = 0
    while True:
        # Seasonal patter generate values that fluctuate 
        seasonal_pattern = 50000 * np.sin(t / 100)  # Fluctuates between -50,000 and 50,000
        noise = np.random.normal(0, 2000)  # Noise with a smaller standard deviation is calculated
        anomaly = 0 #initialised to zero initially

        # Randomly inject an anomaly
        if random.random() < 0.05:
            anomaly = random.uniform(50000, 150000)  # Large spike anomaly in the range of 50,000 to 150,000
        # Ensure the generated value is non-negative
        value = max(0, seasonal_pattern + noise + anomaly)
        yield t, value #yield is used for memory efficiency as the values are generated on the fly as needed
        t += 1

# Anomaly Detection using Z-Score
class ZScoreAnomalyDetector:
    # This function processes the data stream and detects anomalies based on the Z-score. 
    # A Z-score measures how many standard deviations, a data point is from the mean of the data in a sliding window.
    # sliding window is implemented using deque
    def __init__(self, window_size=50, z_score_threshold=3.0):
        self.window = deque(maxlen=window_size)
        self.z_score_threshold = z_score_threshold

    def detect(self, data):
        self.window.append(data)
        if len(self.window) >= self.window.maxlen:
            #  The mean and standard deviation of the data points in the window are calculated that help determine how far a new data point deviates from the normal range of values.
            mean = np.mean(self.window)
            std_dev = np.std(self.window)
            if std_dev == 0:
                return False, mean, 0  # No deviation if std_dev is zero
            
            z_score = (data - mean) / std_dev
            # A Z-score greater than a certain threshold (e.g., 3) is flagged as an anomaly. 
            # threshold =3 as defined in init function above
            return abs(z_score) > self.z_score_threshold, mean, z_score
        return False, 0, 0

# Function to save anomalies to a CSV file with additional details
def save_anomalies_to_csv(anomalies, filename='anomalies_track.csv'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Time", "Value", "Mean", "Deviation"])
        writer.writerows(anomalies)
    print(f"Anomalies saved to {filename}")

# Real-time Visualization using Matplotlib
def live_plot(data_gen, window_size=50, detector_window_size=50, z_score_threshold=3.0):
    fig, ax = plt.subplots(figsize=(12, 6))
    plt.subplots_adjust(bottom=0.2)  # Adjust the bottom to make space for the button
    xdata, ydata = [], []
    anomaly_x, anomaly_y, anomaly_mean, anomaly_deviation = [], [], [], []
    detected_anomalies = []  # To store detected anomalies (time, value, mean, deviation) with mentioned parameters
    line, = ax.plot([], [], lw=2, color='blue', label='Data Stream')
    anomaly_line, = ax.plot([], [], 'ro', markersize=8, label='Anomalies')
    
    # Set initial y-axis limits to accommodate realistic metrics
    ax.set_ylim(0, 200000)
    ax.set_xlim(0, window_size)
    ax.set_title('CobbleStone Energy: Real-time Anomaly Detection (Z-Score) by Mohib Abbas Sayed')
    ax.set_xlabel('Time')
    ax.set_ylabel('Value')
    ax.legend(loc='upper left')

    detector = ZScoreAnomalyDetector(window_size=detector_window_size, z_score_threshold=z_score_threshold)
    is_running = [True]  # A flag to indicate whether the stream is running

    def init():
        return line, anomaly_line

    def update(frame):
        if not is_running[0]:  # Stop the stream if the 'save as csv' button is clicked
            return line, anomaly_line

        t, data = frame
        xdata.append(t)
        ydata.append(data)

        is_anomaly, mean, z_score = detector.detect(data)
        if is_anomaly:
            anomaly_x.append(t)
            anomaly_y.append(data)
            anomaly_mean.append(mean)
            anomaly_deviation.append(z_score)
            detected_anomalies.append((t, data, mean, z_score))  # Save anomaly data
            print(f"Anomaly detected: Time={t}, Value={data}, Mean={mean}, Deviation={z_score}")

        line.set_data(xdata, ydata)
        anomaly_line.set_data(anomaly_x, anomaly_y)

        # Keep y-axis minimum at 0
        current_max_y = max(max(ydata, default=0), 200000)  # Ensure positive y-axis limit
        ax.set_ylim(0, current_max_y + 5000)  # Adding a small margin above the max value

        ax.relim()
        ax.autoscale_view()

        # Keep only the last 'window_size' points
        if len(xdata) > window_size:
            del xdata[0]
            del ydata[0]
            ax.set_xlim(xdata[0], xdata[-1])

        return line, anomaly_line

    # Button click event handler
    def on_save_clicked(event):
        # Stop the data stream
        is_running[0] = False
        # Save anomalies to CSV
        save_anomalies_to_csv(detected_anomalies)
        # Close the plot window
        plt.close(fig)

    # Create a button
    ax_button = plt.axes([0.8, 0.05, 0.1, 0.075])  # Position [left, bottom, width, height]
    btn_save = Button(ax_button, 'Save as CSV')

    # Register the button click event
    btn_save.on_clicked(on_save_clicked)

    ani = FuncAnimation(fig, update, frames=data_gen, init_func=init, blit=True, interval=100)
    plt.show()

# Execute the real-time plot with anomaly detection
if __name__ == "__main__":
    window_size = 100
    detector_window_size = 50
    z_score_threshold = 3.0  # Z-score threshold for anomalies
    live_plot(data_stream(), window_size, detector_window_size, z_score_threshold)
