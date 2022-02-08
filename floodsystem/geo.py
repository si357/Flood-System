# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from haversine import haversine
from .utils import sorted_by_key  # noqa

def stations_by_distance(stations, p):
    "Given a list of stations and coordinates p returns a list of (station, distance) tuples, sorted in order of distance"
    list = []
    for station in stations:
        distance = haversine(p,station.coord)
        tuple = (station, distance)
        list.append(tuple)
    list = sorted_by_key(list,1)
    return list

def stations_within_radius(stations, centre, r):
    x = stations_by_distance(stations, centre)
    lt = []
    i = 0
    while x[i][1] <= r:
        lt.append(x[i][0])
        i += 1
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
                    