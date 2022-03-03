from matplotlib.dates import date2num
import numpy as np
from floodsystem.stationdata import *


def polyfit(dates, levels, p):
    
    dateFloats = date2num(dates)
    offset = dateFloats[0]
    dateFloats = dateFloats - offset
    p_coeff = np.polyfit(dateFloats, levels, p)
    poly = np.poly1d(p_coeff)
    Final = (poly, offset)
    return Final

def relative_risk(station):
    
    number = 0
    relative_level = MonitoringStation.relative_water_level(station)
    if relative_level == None:
        number = None
    else:
        if relative_level > 0.5:
            number += 1
        if relative_level > 1:
            number += 1
        if relative_level > 1.5:
            number+= 1
        if relative_level > 2:
            number +=1

    return number