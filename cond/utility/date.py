from datetime import datetime


class DateUtility():

    # def getNextHours(number_of_hours, current_hour):
    #     if current_hour < (23 - number_of_hours):
    #         return getNextHoursNoMidnightOverlap(number_of_hours, current_hour)
    #     else:
    #         return getNextHoursMidnightOverlap(number_of_hours,current_hour)
    #
    # def getNextHoursNoMidnightOverlap(number_of_hours, current_hour):
    #     hours = []
    #     lastHour = current_hour + number_of_hours
    #     for i in range(current_hour, lastHour + 1):
    #         hours.append(i)
    #     return hours
    #
    # def getNextHoursMidnightOverlap(number_of_hours, current_hour):
    #     hours = []
    #     for i in range(1, nu)

    def sameDay(forecast_datetime_object):
        return (DateUtility.getDay(forecast_datetime_object) == DateUtility.getCurrentDay())

    def sameHour(forecast_datetime_object):
        return (DateUtility.getHour(forecast_datetime_object) == DateUtility.getCurrentHour())

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
