from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_with_fit
from datetime import timedelta

def main():
    stations = build_station_list()
    update_water_levels(stations)
    for station in stations:
        if station.latest_level is None:
            station.latest_level = -20
    stations.sort(reverse=True, key=lambda x: x.latest_level)
    top = stations[:5]
    for station in top:
        dates, levels = fetch_measure_levels(station.measure_id, dt=timedelta(days=2))
        if len(dates) > 0:
            plot_water_level_with_fit(station, dates, levels, 4)

if __name__ == "__main__":
    main()