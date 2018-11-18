# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request,'basic_app/index.html')


def other(request):
    return render(request, 'basic_app/other.html')


def rel(request):
    return render(request, 'basic_app/rel_templates.html')


