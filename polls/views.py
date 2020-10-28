# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

from .models import Person

def test(request):
    return HttpResponse('hello world , first django 1')




def home(request):
    boards = Person.objects.all()
    boards_names = list()

    for board in boards:
        name = board.first_name + '-' + board.last_name
        boards_names.append(name)
    response_html = '<br>'.join(boards_names)

    return HttpResponse(response_html)

def homehtml(request):
    boards = Person.objects.all()
    return render(request, 'home.html', {'boards': boards})