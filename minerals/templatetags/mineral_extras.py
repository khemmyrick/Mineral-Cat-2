import random

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
