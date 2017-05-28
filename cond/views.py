# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from .models import Road
from django.shortcuts import render


def home(request):
    road = Road.objects.get(pk=1)
    html = '<h1>' + road.condition + '<h1>'
    html += '<br>'
    html += '<h4> Uppfært: ' + road.last_update.strftime('%H:%M - %d/%m/%y') + '</h4>'
    html += '<br>'
    html += '<p><i>Byggt á gögnum frá Vegagerðinni.</i></p>'
    return HttpResponse(html)
# Create your views here.
