# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import time, date

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def test(request):
    return HttpResponse('hello world , first django 1'. time.time() )