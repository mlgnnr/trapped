from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
import logging

logger = logging.getLogger(__name__)


def home(request):
    logger.debug("Opening first/views.home")
    return HttpResponse('<h1>Welcome</h1>')
