from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def run():
    "Requirements for Task 1B"
    stations = build_station_list()

    close = []
    far=[]

    x = stations_by_distance(stations, (52.2053, 0.1218))

    for i in range(10):
        close.append((x[i][0].name, x[i][0].town,  x[i][1]))

    for i in range(-10, -1):
        far.append((x[i][0].name, x[i][0].town, x[i][1]))


    print(close)
    print(' \n \n ')
    print(far)


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    print(' \n \n ') 
    run()

