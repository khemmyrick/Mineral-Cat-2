import random
import string

from django import template

from django.shortcuts import get_object_or_404

from minerals.models import Group


register = template.Library()


@register.filter('underspace')
def underspace(attr_string):
    """Replace spaces with underscores."""
    return attr_string.replace('_', ' ')


@register.filter('jpegger')
def jpegger(group_name):
    """Return a mineral image from a group name."""
    group = get_object_or_404(Group, name=group_name)
    g_list = group.get_min()
    mineral = random.choice(g_list)
    return '{}.jpg'.format(mineral.name)


@register.inclusion_tag('minerals/group_nav.html')
def nav_groups_list():
    """Returns a dictionary of mineral groups to display in layout."""
    groups = Group.objects.all().order_by('name')
    return {'groups': groups}


@register.inclusion_tag('minerals/letters.html')
def abc_list():
    """Return a list of letters for first letter search."""
    alpha_search = []
    for char in string.ascii_uppercase:
        alpha_search.append(char)
    return {'alpha_search': alpha_search}
