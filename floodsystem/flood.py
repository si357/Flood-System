
from .station import MonitoringStation

def stations_level_over_threshold(stations, tol):
    fl=[]
    for station in stations:
        if type(station.relative_water_level()) == float:
            if station.relative_water_level() > tol:
                fl.append((station.name, station.relative_water_level()))
    fl.sort(key=lambda x: x[1], reverse=True)
    return fl
    
def stations_highest_rel_level(stations, N):
    hl = []
    for station in stations:
        if type(station.relative_water_level()) == float:
            hl.append(station)
    hl.sort(key=lambda x: x.relative_water_level(), reverse = True)
    return hl[:N]
