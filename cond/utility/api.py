import requests
from cond.models import Road
from django.utils import timezone
import logging

logger = logging.getLogger(__name__)


class Api():

    # road_id_dir = {'hellisheidi_id': 902020003, 'threngslin_id': 902340003}
    road_id_dir = {'sandskeid_id': 903260003, 'hellisheidi_id': 902020003,
                   'threngslin_id': 902340003}

    def makeRequest(type):
        if(type == "roads"):
            r = requests.get('http://gagnaveita.vegagerdin.is/api/faerd2014_1')
        return r

    def getRoads():
        r = Api.makeRequest("roads")
        if(r.status_code == 200):
            Api.parse(r.json())
        else:
            print("Error retrieving Condition from website")

    def parse(response):
        for road in response:
            for road_id in Api.road_id_dir.values():
                Api.search_road(road, road_id)

    def search_road(road, road_id):
        if road['IdButur'] == road_id and road['IdLeid'] is not None:
            print(road['IdLeid'])
            Api.updateRoadObject(road, road_id)

    def updateRoadObject(new_road, road_id):
        if road_id == Api.road_id_dir['hellisheidi_id']:
            Api.saveRoadObject(1, new_road)
        elif road_id == Api.road_id_dir['threngslin_id']:
            Api.saveRoadObject(2, new_road)
        elif road_id == Api.road_id_dir['sandskeid_id']:
            Api.saveRoadObject(3, new_road)

    def saveRoadObject(pk, new_road):
            road = Road.objects.get(pk=pk)
            print(road)
            print("Old condition: " + road.condition)
            # Add notications if CHANGES
            road.condition = new_road['StuttAstand']
            road.last_update = timezone.now()
            road.save()
            print("New condition: " + road.condition)
