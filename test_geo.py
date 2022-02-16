from tokenize import String
from typing import List, Set, Tuple
from floodsystem.geo import *
from floodsystem.stationdata import build_station_list
import random


# TASK 1B: Check that the outputs are of the correct type and value
def test_stations_by_distance():
    stations = build_station_list()
    p = (52.2053, 0.1218)
    s = stations_by_distance(stations, p)

    # The output must be list
    if not type(s) == list:
        raise TypeError("Output is not a list")

    # Every entry must be tuple
    for entry in s:
        if type(entry) != tuple:
            raise TypeError("At least one entry in the list is not a tuple")
            
    # Ordered by distance
    for n in range(0, len(s) - 1):
        assert s[n + 1][1] >= s[n][1]
# TASK 1C: Check that the outputs are of the correct type and are ordered properly
def test_stations_within_radius():
    stations = build_station_list()
    p = (52.2053, 0.1218)

    # No stations within a radius of 0
    assert stations_within_radius(stations, p, 0) == []
    # Choose a random radius
    R = random.randint(5, 10000)
    # Output list
    X = stations_within_radius(stations, p, R)
    # Type of the output
    assert type(X) == list
   

# TASK 1D: Check that the outputs are of the correct type and are ordered properly
def test_rivers_with_station():
    stations = build_station_list()
    # Obtain output
    X = rivers_with_station(stations)
    # Output is of correct type
    assert type(X) == set
    # Type of every entry in the set is correct
    for n in X:
        assert type(n) == str

def test_stations_by_river():
    stations = build_station_list()
    # Obtain output
    X = stations_by_river(stations)
    # Output type
    assert type(X) == dict
    # River Cam is in Cambridge
    assert "Cambridge" in X["River Cam"]

# TASK 1E: Check that the outputs are of the correct type and are ordered properly
def test_rivers_by_station_number():
    stations = build_station_list()
    # Obtain output
    N = random.randint(1, 1000)
    X = rivers_by_station_number(stations, N)
    # Type of the output
    assert type(X) == list
    # Alphabetical order
    for n in range(0, len(X) - 1):
        assert X[n + 1][1] <= X[n][1]
    # List is of length N or greater
    assert len(X) >= N
    