import matplotlib.pyplot as plt
import matplotlib
from datetime import datetime, timedelta
import numpy as np


def plot_water_levels(station, dates, levels):

    data_length = len(dates)

    min = [station.typical_range[0]] * data_length
    max = [station.typical_range[1]] * data_length

    plt.subplots(figsize=(10,10))

    plt.plot(dates, levels)

    plt.plot(dates, min, color="orange")
    plt.plot(dates, max, color="orange")

    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title("Station: {}".format(station.name))

    # Display the plot, ensuring no labels are cut off
    plt.tight_layout()
    plt.show()