# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from .models import Road
from django.shortcuts import render


def home(request):
    road = Road.objects.get(pk=1)
    html = '<h1>' + road.condition + '<h1>'
    html += '<br>'
    html += '<h3>' + road.last_update.strftime("%A, %d. %B %Y %I:%M%p") + '<h3>'
    return HttpResponse(html)
# Create your views here.
