from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

def run():
    stations = build_station_list()
    rivers = rivers_with_station(stations)
    rivers = sorted(rivers)

    print("Number of stations with a river:{}".format(len(rivers)))
    print("First 10 rivers: {}".format(rivers[:10]))
    print(' \n \n ')
    StationsRivers = stations_by_river(stations)
    Aire =[]
    for stations in StationsRivers["River Aire"]:
        Aire.append(stations)
    Aire.sort()
    print("Stations on River Aire:{}".format(Aire))
    print(' \n \n ')
    Cam =[]
    for stations in StationsRivers["River Cam"]:
        Cam.append(stations)
    Cam.sort()
    print("Stations on River Cam:{}".format(Cam))
    print(' \n \n ')
    Thames =[]
    for stations in StationsRivers["River Thames"]:
        Thames.append(stations)
    Thames.sort()
    print("Stations on River Thames:{}".format(Thames))
    print(' \n \n ')

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    print(' \n \n ') 
    run()