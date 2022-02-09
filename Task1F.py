from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations


def run():
    
    stations = build_station_list()
    inconsistent = inconsistent_typical_range_stations(stations)

    out_range = [] 
    for station in inconsistent: 
        out_range.append(station.name)
    out_range.sort() 
    print(out_range) 
run()