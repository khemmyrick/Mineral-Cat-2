from django.shortcuts import render

from minerals.models import Group


def index(request):
    groups = Group.objects.all()
    return render(request,
                  'minerals/index.html',
                  {'groups': groups})
