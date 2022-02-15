# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from haversine import haversine
from .utils import sorted_by_key  # noqa

def stations_by_distance(stations, p):
    dist_stat = []
    # Calculate distance from point
    for stat in stations:
        dist_stat.append((stat, haversine(stat.coord, p)))

    # Sort result and return
    dist_stat.sort(key=lambda x: x[1])
    return dist_stat

def stations_within_radius(stations, centre, r):
    x = stations_by_distance(stations, centre)
    lt = []
    for stat in x:
        if stat[1] < r:
            lt.append(stat)
    return lt 

def rivers_with_station(stations):
    rivers = set([])
    for station in stations: 
        rivers.add(station.river)
    return rivers

def stations_by_river(stations):
    rivers = rivers_with_station(stations)
    rivers = sorted(rivers)

    riverdict = {}
    for r in rivers:
        riverdict[r] = []
        for s in stations:
            if r == s.river:
                riverdict[r].append(s.name)
    return riverdict

def rivers_by_station_number(stations, N):
    
    unsorted = [(river[0], len(river[1])) for river in stations_by_river(stations).items()]
    rivers_number = sorted_by_key(unsorted, 1, reverse=True)
    nth = rivers_number[N - 1][1]
    rivers_output = []
    for river in rivers_number:
        if river[1] < nth:
            break
        rivers_output.append(river)
    return rivers_output