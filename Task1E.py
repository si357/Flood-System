from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number

def run ():
    stations = build_station_list() 
    N = 9
    print(rivers_by_station_number(stations, N))
run()


