import random
import re
import string

from django.shortcuts import get_object_or_404, render
from django.db.models import Q
from django.db import models as orig_g

from .models import Group, Mineral


def letter_gen():
    alpha_search = []
    for char in string.ascii_uppercase:
        alpha_search.append(char)
    return alpha_search

    
def index(request):
    groups = Group.objects.all()
    return render(request,
                  'minerals/index.html',
                  {'groups': groups})


def mineral_list(request, **kwargs):
    """Generate template list of all minerals."""
    alpha_search = letter_gen()
    minerals = Mineral.objects.all()
    if kwargs:
        minerals = [minerals.filter(key=value) for key, value in kwargs]
    return render(request,
                  'minerals/mineral_list.html',
                  {'minerals': minerals,
                   'alpha_search': alpha_search})


def group_list(request, pk):
    """Generate template list of all minerals in a specific group."""
    group = get_object_or_404(Group, pk=pk)
    minerals = group.get_min()
    return render(request,
                  'minerals/group_list.html',
                  {'minerals': minerals,
                   'group': group})


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
    return render(request,
                  'minerals/mineral_detail.html',
                  {'mineral': mineral,
                   'attrlist': attrlist})


def random_mineral(request):
    pickfrom = len(Mineral.objects.all())
    prikey = random.randint(1, pickfrom)
    return mineral_detail(request, prikey)


def random_ingroup(request, pk):
    group = get_object_or_404(Group, pk=pk)
    minerals = group.get_min()
    m_choice = [mineral.pk for mineral in minerals]
    prikey = random.choice(m_choice)
    return mineral_detail(request, prikey)


def random_group(request):
    pick_group = len(Group.objects.all())
    prikey = random.randint(1, pick_group)
    return group_list(request, prikey)


def by_alpha(request, term):
    alpha_search = letter_gen()
    minerals = Mineral.objects.filter(name__startswith=term)
    return render(request,
                  'minerals/mineral_list.html',
                  {'minerals': minerals, 'alpha_search': alpha_search})


def search(request):
    """Allow users to search mineral fields for specific terms."""
    alpha_search = letter_gen()
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
    )
    # minerals = Mineral.objects.filter(
    #    Q(name|imgcap|category|formula|strunz_classification|color|crystal_system|unit_cell|crystal_symmetry|cleavage__icontains=term)
    # )
    return render(request,
                  'minerals/mineral_list.html',
                  {'minerals': minerals, 'alpha_search': alpha_search})
