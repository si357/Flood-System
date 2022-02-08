from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations


def run():
    # List of stations where the station has inconsistant typical range values 
    stations = build_station_list()
    inconsistent = inconsistent_typical_range_stations(stations)

    out_range = [] 
    for station in inconsistent: # Inconsistant range 
        out_range.append(station.name) # Add these station to the list

    out_range.sort() # Sort in alphabetical order
    print(out_range) # Print
    print("")



if __name__ == "__main__":
    print("")
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    print("")
    run()