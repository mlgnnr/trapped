import requests
from cond.models import Road, WeatherStation
from django.utils import timezone
import logging

logger = logging.getLogger(__name__)


class Api():

    # road_id_dir = {'hellisheidi_id': 902020003, 'threngslin_id': 902340003}
    road_id_dir = {'sandskeid_id': 903260003, 'hellisheidi_id': 902020003,
                   'threngslin_id': 902340003}
    station_id_dir = {'sandskeid_id': 17, 'hellisheidi_id': 1,
                      'threngslin_id': 31}

    def makeRequest(type):
        if(type == "roads"):
            r = requests.get('http://gagnaveita.vegagerdin.is/api/faerd2014_1')
        elif(type == "weather"):
            r = requests.get('http://gagnaveita.vegagerdin.is/api/vedur2014_1')
        return r

    def getRoads():
        r = Api.makeRequest("roads")
        if(r.status_code == 200):
            Api.parseRoad(r.json())
        else:
            print("Error retrieving Condition from website")

    def getCurrentWeather():
        r = Api.makeRequest("weather")
        if(r.status_code == 200):
            Api.parseWeatherStation(r.json())
        else:
            print("Error retrieving Weather from website")

    def parseWeatherStation(response):
        for station in response:
            for station_id in Api.station_id_dir.values():
                Api.searchWeatherStation(station, station_id)

    def parseRoad(response):
        for road in response:
            for road_id in Api.road_id_dir.values():
                Api.search_road(road, road_id)

    def search_road(road, road_id):
        if road['IdButur'] == road_id and road['IdLeid'] is not None:
            print(road['IdLeid'])
            Api.updateRoadObject(road, road_id)

    def searchWeatherStation(station, station_id):
        if station['Nr'] == station_id:
            print(station['Nafn'])
            Api.updateWeatherStationObject(station, station_id)

    def updateRoadObject(new_road, road_id):
        if road_id == Api.road_id_dir['hellisheidi_id']:
            Api.saveRoadObject(1, new_road)
        elif road_id == Api.road_id_dir['threngslin_id']:
            Api.saveRoadObject(2, new_road)
        elif road_id == Api.road_id_dir['sandskeid_id']:
            Api.saveRoadObject(3, new_road)

    def updateWeatherStationObject(new_station, station_id):
        if station_id == Api.station_id_dir['hellisheidi_id']:
            Api.saveWeatherStationObject(1, new_station)
        elif station_id == Api.station_id_dir['threngslin_id']:
            Api.saveWeatherStationObject(2, new_station)
        elif station_id == Api.station_id_dir['sandskeid_id']:
            Api.saveWeatherStationObject(3, new_station)

    def saveRoadObject(pk, new_road):
            road = Road.objects.get(pk=pk)
            print(road)
            print("Old condition: " + road.condition)
            # Add notications if CHANGES
            road.condition = new_road['StuttAstand']
            road.last_update = timezone.now()
            road.save()
            print("New condition: " + road.condition)

    def saveWeatherStationObject(pk, new_station):
            station = WeatherStation.objects.get(pk=pk)
            print(station.wind_direction)
            # Add notications if CHANGES
            station.wind = new_station['Vindhradi']
            station.wind_direction = new_station['VindattAsc']
            station.wind_max = new_station['Vindhvida']
            station.temp = new_station['Hiti']
            station.temp_road = new_station['Veghiti']
            station.humidity = new_station['Raki']
            station.save()
            print("Saved: Weather: " + station.name)
