import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from .analysis import polyfit
import matplotlib.dates as date
from matplotlib.dates import date2num
from datetime import datetime, timedelta



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

def plot_water_level_with_fit(station, dates, levels, p):
    #create polynomial object and plot it using 30 data points spaced along the requested period (denoted by dates)
    #print(dates)
    poly, offset = polyfit(dates, levels, p)
    dateFloat = date2num(dates)
    plt.plot(dateFloat, poly(dateFloat-offset))

    #Plot exact data 
    plt.plot(dates,levels, '.')

    #Format graphs
    plt.xlabel('Date')
    plt.ylabel('Water Level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.tight_layout()

    plt.show()