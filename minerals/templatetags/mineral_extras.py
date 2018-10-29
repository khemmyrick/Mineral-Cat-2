import random
import string

from django import template

from django.shortcuts import get_object_or_404

from minerals.models import Group, Mineral


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


@register.inclusion_tag('minerals/group_nav.html', takes_context=True)
def nav_groups_list(context):
    """Returns a dictionary of mineral groups to display in layout."""
    group_list = Group.objects.all().order_by('name')
    return {'group_list': group_list, 'group': context['group']}
    

@register.inclusion_tag('minerals/cat_list.html', takes_context=True)
def min_cat_list(context):
    """Returns a dictionary of mineral categories to display in layout."""
    minerals = Mineral.objects.all()
    categories = []
    for mineral in minerals:
        categories.append(mineral.category)
    categories = set(categories)
    categories = list(categories)
    return {'categories': categories, 'categ': context['categ']}


@register.inclusion_tag('minerals/color_nav.html', takes_context=True)
def color_list(context):
    """Returns a dictionary of possible mineral colors to display in layout."""
    colors = ['Black',
              'Blue',
              'Brown',
              'Colorless',
              'Gray',
              'Green',
              'Indigo',
              'Orange',
              'Purple',
              'Red',
              'Violet',
              'White',
              'Yellow']
    return {'colors': colors, 'target_color': context['target_color']}


@register.inclusion_tag('minerals/letters.html', takes_context=True)
def abc_list(context):
    """Return a list of letters for first letter search."""
    alpha_search = []
    for char in string.ascii_uppercase:
        alpha_search.append(char)
    return {'alpha_search': alpha_search, 'term': context['term']}
