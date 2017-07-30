import requests
import csv
import codecs
from datetime import datetime
import xml.etree.ElementTree as etree
from cond.models import Road, Weather, WeatherStation
from cond.models import WeatherForecast, Condition, Image
from django.utils import timezone
from cond.utility.date import DateUtility
from enum import Enum
import logging

logger = logging.getLogger(__name__)
forecast_hours = 12


class Api():

    # road_id_dir = {'hellisheidi_id': 902020003, 'threngslin_id': 902340003}
    road_id_dir = {'Hellisheiði': 902020003,
                   'Þrengsli': 902340003, 'Sandskeið': 903260003}

    station_id_dir = {'sandskeid_id': 17, 'hellisheidi_id': 1,
                      'threngslin_id': 31}

    webcam_id_dir = {'sandskeid_id': 7080, 'hellisheidi_id': 7001,
                     'threngslin_id': 31}
    forecast_id_dir = {'hellisheidi_id': 31392,
                     'threngslin_id': 31387}



    hellisheidi_img = "http://www.vegagerdin.is/vgdata/vefmyndavelar/hellisheidi_3.jpg"
    threngslin_img = "http://www.vegagerdin.is/vgdata/vefmyndavelar/threngsli_1.jpg"
    sandskeid_img = "http://www.vegagerdin.is/vgdata/vefmyndavelar/sandskeid_1.jpg"

    def addImages():
        road = Road.objects.get(name="Hellisheiði")

        if(road.image_set.count() == 0):
            print("Not in database: " + "Images")
            Api.addImagesThrengsli()
            Api.addImagesHellisheidi()
            Api.addImagesSandskeid()



    def addDataToDataBase():
        for road_name, road_id in Api.road_id_dir.items():
            road = (road_name, road_id)
            Api.databaseContainsRoad(road)
            # Api.databaseContainsRoad(road_id)

        Api.addImages()
        Api.getRoadCondition()
        Api.getCurrentWeather()
        Api.getForecast()
        # Api.getWebCams()

    def databaseContainsRoad(road):
        try:
            check_road = Road.objects.get(id_butur=road[1])
        except Road.DoesNotExist:
            print("Not in database: " + road[0])
            new_road = Road(name=road[0],id_butur=road[1],last_updated=timezone.now())
            new_road.save()
            new_weather = Weather(road=new_road)
            new_weather.save()
            return



    def makeRequest(type):
        if(type == "condition"):
            r = requests.get('http://gagnaveita.vegagerdin.is/api/faerd2014_1')
        elif(type == "weather"):
            r = requests.get('http://gagnaveita.vegagerdin.is/api/vedur2014_1')
        elif(type == "forecast"):
            r = requests.get('http://xmlweather.vedur.is/?op_w=xml&type=forec&lang=is&view=csv&ids=31392')
        return r

    def getRoadCondition():
        r = Api.makeRequest("condition")
        if(r.status_code == 200):
            Api.parseRoadCondition(r.json())
        else:
            print("Error retrieving Condition from website")

    def getCurrentWeather():
        r = Api.makeRequest("weather")
        if(r.status_code == 200):
            Api.parseWeatherStation(r.json())
        else:
            print("Error retrieving Weather from website")

    def getForecast():
        r = Api.makeRequest("forecast")

        if(r.status_code == 200):
            Api.parseForecast(r)
        else:
            print("Errror retrieving Forecast")
##TODOOO
    def parseForecast(response):
        csvfile = response.iter_lines()
        response_dict = csv.DictReader(codecs.iterdecode(csvfile, 'utf-8'))
        Api.searchForecast(response_dict, forecast_hours)

    def searchForecast(forecasts, number_of_hours):

        number_of_forecasts_added = 0
        found_currentHour = False
        road = Road.objects.get(name="Hellisheiði")
        forecasts_database = road.weather.weatherforecast_set.all()
        midnight_list = []

        if not forecasts_database:
            print("Database empty")
        else:
            print("Deleted Forecasts in database")
            road.weather.weatherforecast_set.all().delete()


        index = 0
        for forecast in forecasts:
            datetime_object = DateUtility.makeDateObject(forecast['Spátími'])

            #IF current hour is not found - use first items in dict
            if index < number_of_hours:
                    midnight_list.append(forecast)
                    index += 1

            if not(found_currentHour):
                # print(DateUtility.sameDay(datetime_object))
                # print(DateUtility.sameHour(datetime_object))
                if(DateUtility.sameDay(datetime_object) and DateUtility.sameHour(datetime_object)):
                    print('correct hour and day', forecast['Spátími'])
                    found_currentHour = True
                    number_of_forecasts_added += 1
                    Api.saveForecastObject(forecast, datetime_object)
            elif (found_currentHour and number_of_forecasts_added <= number_of_hours):
                number_of_forecasts_added += 1
                Api.saveForecastObject(forecast, datetime_object)

            if number_of_forecasts_added > number_of_hours:
                break

        #IF current hour is not in forecast
        if not found_currentHour:
            for forecast in midnight_list:
                datetime_object = DateUtility.makeDateObject(forecast['Spátími'])
                Api.saveForecastObject(forecast, datetime_object)



    def saveForecastObject(forecast, datetime_object):
        road = Road.objects.get(name="Hellisheiði")
        forecastObject = WeatherForecast()
        forecastObject.weather = road.weather
        forecastObject.name = "Hellisheiði"
        forecastObject.hour = DateUtility.getHour(datetime_object)
        forecastObject.wind = forecast['Vindhraði (m/s)']
        forecastObject.wind_max = 0
        forecastObject.wind_direction = forecast['Vindátt']
        forecastObject.temp = forecast['Hiti (°C)']
        forecastObject.sky = forecast['Veður']
        forecastObject.save()

    def getWebcams():
        r = Api.makeRequest("webcam")
        if(r.status_code == 200):
            Api.parseWebcam(r.json())
        else:
            print("Error retrieving Webcam from website")

    def parseWebcam(response):
        for station in response:
            for station_id in Api.webcam_id_dir.values():
                Api.searchWebcamStation(station, station_id)

    def parseWeatherStation(response):
        for station in response:
            for station_id in Api.station_id_dir.values():
                Api.searchWeatherStation(station, station_id)

    def parseRoadCondition(response):
        for road in response:
            for road_id in Api.road_id_dir.values():
                Api.search_road(road, road_id)

    def search_road(response_road, road_id):
        if response_road['IdButur'] == road_id and response_road['IdLeid'] is not None:
            Api.updateRoadConditionObject(response_road)

    def searchWeatherStation(station, station_id):
        if station['Nr'] == station_id:
            Api.updateWeatherStationObject(station)

    def searchWebcamStation(station, station_id):
        if station['Maelist_nr'] == station_id:
            print(station['Maelist_nr'])


    def updateRoadConditionObject(new_road):

        road = Road.objects.get(id_butur=new_road['IdButur'])
        try:
            condition = road.condition
            condition.status = new_road['StuttAstand']
            condition.sign = new_road['Skilti']
            condition.save()
            print("New condition: " + condition.status)
        except Condition.DoesNotExist:
            new_condition = Condition(road=road,
                                      status=new_road['StuttAstand'],
                                      sign=new_road['Skilti'])
            new_condition.save()
            print("New Condition object added: " + new_condition.status)



    def updateWeatherStationObject(new_station):
        road = Road.objects.get(name=new_station['Nafn'])
        try:
            weatherstation = road.weather.weatherstation
            Api.saveWeatherStationObject(weatherstation,new_station)
        except WeatherStation.DoesNotExist:
            new_weatherstation = WeatherStation(
                                 road=road.weather,
                                 name=new_station['Nafn'],
                                 wind = new_station['Vindhradi'],
                                 wind_direction = new_station['VindattAsc'],
                                 wind_max = new_station['Vindhvida'],
                                 temp = new_station['Hiti'],
                                 temp_road = new_station['Veghiti'],
                                 humidity = new_station['Raki'])
            new_weatherstation.save()
            print("New WeatherStation object added: " + new_weatherstation.name)

    def saveRoadConditionObject(new_road):
            road = Road.objects.get(pk=pk)
            print(road)
            print("Old condition: " + road.condition)
            # Add notications if CHANGES
            road.condition = new_road['StuttAstand']
            road.last_update = timezone.now()
            road.save()
            print("New condition: " + road.condition)

    def saveWeatherStationObject(station, new_station):
            # Add notications if CHANGES
            station.wind = new_station['Vindhradi']
            station.wind_direction = new_station['VindattAsc']
            station.wind_max = new_station['Vindhvida']
            station.temp = new_station['Hiti']
            station.temp_road = new_station['Veghiti']
            station.humidity = new_station['Raki']
            station.last_updated = new_station['Dags']
            station.save()
            print("New weather: " + station.name)

    def addImagesThrengsli():
        road = Road.objects.get(name="Þrengsli")
        for i in range(1,4):
            new_img = Image(road=road,
                            url="http://www.vegagerdin.is/vgdata/vefmyndavelar/threngsli_" + str(i) + ".jpg",
                            image_id = i)
            new_img.save()

    def addImagesHellisheidi():
        road = Road.objects.get(name="Hellisheiði")
        for i in range(1,4):
            new_img = Image(road=road,
                            url="http://www.vegagerdin.is/vgdata/vefmyndavelar/hellisheidi_" + str(i) + ".jpg",
                            image_id = i)
            new_img.save()

    def addImagesSandskeid():
        road = Road.objects.get(name="Sandskeið")
        for i in range(1,3):
            new_img = Image(road=road,
                            url="http://www.vegagerdin.is/vgdata/vefmyndavelar/sandskeid_" + str(i) + ".jpg",
                            image_id = i)
            new_img.save()
