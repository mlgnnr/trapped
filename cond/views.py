# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Road


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
    road = get_object_or_404(Road, pk=1)
    update_time = road.last_update.strftime('%H:%M - %d/%m/%y')
    context = {'update_time': update_time, 'road': road}
    return render(request, 'cond/index.html', context)


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     context = {'question': question}
#     return render(request, 'polls/results.html', context)
