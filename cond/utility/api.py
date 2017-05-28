import requests
from cond.models import Road
from django.utils import timezone


class Api():

    sandskeid_id = 903260003
    hellisheidi_id = 902020003
    threngslin_id = 902340003

    def makeRequest(type):
        if(type == "roads"):
            r = requests.get('http://gagnaveita.vegagerdin.is/api/faerd2014_1')
        return r

    def getRoads():
        r = Api.makeRequest("roads")
        if(r.status_code == 200):
            Api.parse(r.json(), Api.hellisheidi_id)
        else:
            print("Error retrieving Condition from website")

    def parse(response, road_id):
        for road in response:
            if road['IdButur'] == road_id and road['IdLeid'] is not None:
                print(road['IdLeid'])
                Api.updateRoadObject(road)

    def updateRoadObject(new_road_status):
        road = Road.objects.get(pk=1)
        print(road.condition)
        # Add notications if CHANGE
        road.condition = new_road_status['StuttAstand']
        road.last_update = timezone.now()
        print(road.condition)
        road.save()
