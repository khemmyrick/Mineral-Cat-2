from django.shortcuts import render

from minerals.models import Group
from minerals import views


def index(request):
    return views.by_alpha(request, 'A')
