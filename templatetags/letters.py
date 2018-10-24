import string

from django import template

from django.shortcuts import get_object_or_404

from minerals.models import Group


register = template.Library()


@register.inclusion_tag('letters.html')
def by_alpha():
    alpha_search = []
    for char in string.ascii_uppercase:
        alpha_search.append(char)
    return {'alpha_search': alpha_search}
