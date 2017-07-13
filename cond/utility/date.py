from datetime import datetime


class DateUtility():

    def getCurrentHour():
        return datetime.now().strftime('%H')

    def getCurrentDay():
        return datetime.now().strftime('%d')

    def getHour(forecast_datetime_object):
        return forecast_datetime_object.strftime('%H')

    def getDay(forecast_datetime_object):
        return forecast_datetime_object.strftime('%d')

    def makeDateObject(forecast_time):
        return datetime.strptime(forecast_time, '%Y-%m-%d %H:%M:%S')
