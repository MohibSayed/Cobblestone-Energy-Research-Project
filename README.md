# CobbleStone Energy: Efficient Data Stream Anomaly Detection

<br/>
<p align="center">
  <img src="https://cobblestoneenergy.com/wp-content/uploads/2022/10/logo-updated.svg" width="20%" alt="logo"/>
</p>

## Table Of Contents

- [About the Project](#about-the-project)
- [Algorithm Selection](#algorithm-selection)
- [Data Stream Simulation](#data-stream-simulation)
- [Anomaly Detection](#anomaly-detection)
- [Optimization](#optimization)
- [Visualization](#visualization)
- [Installation](#installation)
- [Snapshot](#snapshot)

## About The Project

**Problem Statement**

The task is to develop a Python script capable of detecting anomalies in a continuous data stream. This stream, simulating real-time sequences of floating-point numbers, could represent various metrics such as financial transactions or system metrics. Your focus will be on identifying unusual patterns, such as exceptionally high values or deviations from the norm.

**Requirements**

- The project must be implemented using Python 3.x.
- Your code should be thoroughly documented, with comments to explain key sections.
- Include a concise explanation of your chosen algorithm and its effectiveness.
- Ensure robust error handling and data validation.
- Limit the use of external libraries. If necessary, include a requirements.txt file.

<br />

**Features**

1. Data Generation: The `data_stream` function simulates a time series with fluctuating values, incorporating seasonal patterns, noise, and sudden anomalies, ensuring non-negative output.
2. Anomaly Detection: The `ZScoreAnomalyDetector` class identifies anomalies using a Z-score method, comparing current data against historical data within a sliding window.
3. Real-time Plotting: The `live_plot` function uses Matplotlib to create a real-time plot of the data stream, with visual indicators for detected anomalies and adjustable y-axis limits.
4. CSV Export: Anomalies detected are saved to a CSV file when a button is clicked, including time, value, mean, and deviation.
5. Interactive Features: The plot includes a save button to export data and dynamically updates the plot limits based on data range to ensure readability.


## Algorithm Selection

- **Chosen Algorithm: Z-Score Method** <br/>
  The Z-score method is a simple yet effective statistical approach for anomaly detection, which measures how far a data point deviates from the mean in terms of standard deviations. It's particularly suitable for detecting anomalies when the data distribution follows a normal (Gaussian) distribution.
  <br/>
  The threshold-based approach (Z-score threshold of 3.0) provides a clear cutoff for detecting anomalies. <br/>
  <br/>
  Improvement Pointers:
  Consider using more adaptive methods like Isolation Forest, LOF (Local Outlier Factor), or Autoencoders if data distribution becomes complex or non-Gaussian.

  
## Data Stream Simulation

- **Chosen Method: `seasonal_pattern`, `noise`, `anomaly`** <br/>
  Simulated time-series data with seasonal patterns, noise, and occasional random anomalies (spikes).


## Anomaly Detection

- **Z-Score-Based Detection** <br/>
  A sliding window approach is used with deque to store recent values and calculate rolling statistics (mean and standard deviation).

## Optimization

  - **We achieved optimization in following way:** <br/>
    1. The code efficiently handles real-time data using a deque to maintain a sliding window for anomaly detection.<br/>
    2. Yield-based data generation (yield t, value) ensures that memory is managed efficiently by generating data on the fly rather than storing it all at once.<br/>
    3. Rolling mean and standard deviation calculations are done only within the sliding window, reducing unnecessary recalculations.
   

## Visualization

- **Real-time Plotting** <br/>
  The live plot shows the data stream in real time, with anomalies highlighted using red markers, providing an immediate visual representation of detected outliers.
- **Interactive Features**<br/>
    1. Save to CSV Button: Anomalies can be saved to a CSV file when the "Save as CSV" button is clicked, providing an interactive way to record results for future analysis.
    2. Dynamic Plot Limits: The y-axis range adapts dynamically to the data range to ensure the plot remains readable.
 
  
## Installation

To set up the project locally, follow these steps:

1. **Clone the repository**

```sh
   git clone https://github.com/MohibSayed/Cobblestone-Energy-Research-Project.git
```

2. **Install the required packages**

```sh
 pip install -r requirements.txt
```

3. **Run the application**

```sh
 python main.py
```

## Snapshot

![demonstration_screenshot](https://github.com/user-attachments/assets/80bf35b8-f3b2-447f-a801-045e76fda341)
<br/>
![image](https://github.com/user-attachments/assets/2a08beb0-7a6a-4500-8d3b-9163f4c6b5b2)



## Author

- Mohib Abbas Sayed
  - [LinkedIn](https://www.linkedin.com/in/mohib-abbas-sayed-83837422a/?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)
