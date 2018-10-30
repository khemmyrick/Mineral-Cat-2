import random
import re

from django.shortcuts import get_object_or_404, render
from django.db.models import Q
from django.db import models as orig_g

from .models import Group, Mineral


def index(request):
    return by_alpha(request, 'A')


def mineral_list(request, **kwargs):
    """Generate template list of all minerals."""
    minerals = Mineral.objects.values('name', 'group', 'id')
    if kwargs:
        minerals = [minerals.filter(key=value) for key, value in kwargs]
    group = ''
    term = ''
    categ = ''
    target_color = ''
    return render(request,
                  'minerals/mineral_list.html',
                  {'minerals': minerals,
                   'group': group,
                   'term': term,
                   'categ': categ,
                   'target_color': target_color})


def group_list(request, pk):
    """Generate template list of all minerals in a specific group."""
    minerals = Mineral.objects.filter(
        group__id=pk
    ).values(
        'name', 'group', 'id'
    )
    group = get_object_or_404(Group, pk=pk)
    term = ''
    categ = ''
    target_color = ''
    return render(request,
                  'minerals/mineral_list.html',
                  {'minerals': minerals,
                   'group': group,
                   'term': term,
                   'categ': categ,
                   'target_color': target_color})


def cat_list(request, term):
    """Generate template list of all minerals in a specific category."""
    minerals = Mineral.objects.filter(category__icontains=term).values('name', 'group', 'id')
    categ = term
    group = ''
    term = ''
    target_color = ''
    return render(request,
                  'minerals/mineral_list.html',
                  {'minerals': minerals,
                   'group': group,
                   'term': term,
                   'categ': categ,
                   'target_color': target_color})


def color_search(request, term):
    """Generate list of minerals that sometimes contain a given color."""
    minerals = Mineral.objects.filter(color__icontains=term).values('name', 'group', 'id')
    target_color = term
    categ = ''
    group = ''
    term = ''
    return render(request,
                  'minerals/mineral_list.html',
                  {'minerals': minerals,
                   'group': group,
                   'term': term,
                   'categ': categ,
                   'target_color': target_color})


def mineral_detail(request, pk):
    """Generate template for a specific mineral."""
    mineral = get_object_or_404(Mineral, pk=pk)
    attrlist = list(filter(lambda a: not a.startswith('__'), dir(mineral)))
    mlist = [dflt for dflt in dir(orig_g.Model)]
    attrlist = list(filter(lambda x: x not in mlist, attrlist))
    no_list = ['DoesNotExist', 'MultipleObjectsReturned', '_state', 'id',
               'name', 'imgcap', 'imgfile', 'objects', 'group', 'category',
               'formula', 'group_id']
    attrlist = list(filter(lambda x: x not in no_list, attrlist))
    for thing in attrlist:
        if thing.startswith('_'):
            attrlist.remove(thing)
    vallist = [getattr(mineral, thing) for thing in attrlist]
    result = zip(attrlist, vallist)
    attrlist = list(result)
    group = ''
    term = ''
    categ = ''
    target_color = ''
    return render(request,
                  'minerals/mineral_detail.html',
                  {'mineral': mineral,
                   'attrlist': attrlist,
                   'group': group,
                   'term': term,
                   'categ': categ,
                   'target_color': target_color})


def random_mineral(request):
    pickfrom = len(Mineral.objects.all())
    prikey = random.randint(1, pickfrom)
    return mineral_detail(request, prikey)


def random_group(request):
    pick_group = len(Group.objects.all())
    prikey = random.randint(1, pick_group)
    return group_list(request, prikey)


def by_alpha(request, term):
    minerals = Mineral.objects.filter(
        name__startswith=term
    ).values(
        'name', 'group', 'id'
    )
    term = term
    group = ''
    categ = ''
    target_color = ''
    return render(request,
                  'minerals/mineral_list.html',
                  {'minerals': minerals,
                   'term': term,
                   'group': group,
                   'categ': categ,
                   'target_color': target_color})


# def by_cat(request, term):
#    minerals = Mineral.objects.filter(category=term).values('name', 'group', 'id')
#    term = term
#    group = ''
#    return render(request,
#                  'minerals/mineral_list.html',
#                  {'minerals': minerals,
#                   'term': term,
#                   'group': group})    


def search(request):
    """Allow users to search mineral fields for specific terms."""
    term = request.GET.get('q')
    # Loop through all fields to return matches using 'Q(field__icontains=term)|' notation?
    # Currently works with no looping.
    minerals = Mineral.objects.filter(
        Q(name__icontains=term)|Q(group__name__icontains=term)|
        Q(imgcap__icontains=term)|Q(formula__icontains=term)|
        Q(category__icontains=term)|Q(strunz_classification__icontains=term)|
        Q(color__icontains=term)|Q(crystal_system__icontains=term)|
        Q(unit_cell__icontains=term)|Q(crystal_symmetry__icontains=term)|
        Q(cleavage__icontains=term)|Q(luster__icontains=term)|
        Q(mohs_scale_hardness__icontains=term)|Q(streak__icontains=term)|
        Q(diaphaneity__icontains=term)|Q(optical_properties__icontains=term)|
        Q(refractive_index__icontains=term)|Q(crystal_habit__icontains=term)|
        Q(specific_gravity__icontains=term)
    ).values('name', 'group', 'id')
    # minerals = Mineral.objects.filter(
    #    Q(name|imgcap|category|formula|strunz_classification|color|crystal_system|unit_cell|crystal_symmetry|cleavage__icontains=term)
    # )
    group = ''
    term = ''
    categ = ''
    target_color = ''
    return render(request,
                  'minerals/mineral_list.html',
                  {'minerals': minerals,
                   'group': group,
                   'term': term,
                   'categ': categ,
                   'target_color': target_color})
