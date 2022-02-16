from tokenize import String
from typing import List, Set, Tuple
from floodsystem.flood import *
from floodsystem.stationdata import build_station_list
import random

def test_stations_level_over_threshold():
    stations = build_station_list()
    s = stations_level_over_threshold(stations, 10)

    # The output must be list
    if not type(s) == list:
        raise TypeError("Output is not a list")

    # Every entry must be tuple
    for entry in s:
        if type(entry) != tuple:
            raise TypeError("At least one entry in the list is not a tuple")

def test_stations_highest_rel_level():
    stations = build_station_list()
    s = stations_highest_rel_level(stations, 10)

    # The output must be list
    if not type(s) == list:
        raise TypeError("Output is not a list")


            