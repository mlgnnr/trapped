from django.core.management.base import BaseCommand
from cond.models import Road as R
from django.utils import timezone
from cond.utility.api import Api
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'gets data from vegagerdin'

    def handle(self, *args, **options):

        Api.addDataToDataBase()
        # Api.getForecast()
        # Api.getRoads()
        # Api.getCurrentWeather()
