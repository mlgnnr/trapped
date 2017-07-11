# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Road
import logging

logger = logging.getLogger(__name__)


def home(request):
    road = Road.objects.get(pk=1)
    html = '<h1>' + road.condition + '<h1>'
    html += '<br>'
    html += '<h4> Uppfært: ' + road.last_update.strftime('%H:%M - %d/%m/%y') + '</h4>'
    html += '<br>'
    html += '<p><i>Byggt á gögnum frá Vegagerðinni.</i></p>'
    return HttpResponse(html)
# Create your views here.


def index(request):
    road_list = []
    road_list.append(get_object_or_404(Road, name="Hellisheiði"))

    context = {'road_list': road_list,}
    return render(request, 'cond/index.html', context)


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     context = {'question': question}
#     return render(request, 'polls/results.html', context)
