# -*- coding: utf-8 -*-

import json

from django.db import migrations, models


def loadmin(apps, schema_editor):
    """Load JSON file into Django Database."""
    Group = apps.get_model('minerals', 'Group')
    Mineral = apps.get_model('minerals', 'Mineral')
    g_list = []
    minelist = []
    with open('minerals/fixtures/minerals.json', 'r', encoding="utf8") as mindb:
        data = json.load(mindb)
        for mineral in data:
            g_list.append(mineral.get('group', ''))
        g_set = set(g_list)
        g_list = []
        for gname in g_set:
            gobj = Group(name=gname)
            g_list.append(gobj)
        Group.objects.bulk_create(g_list)
        for mineral in data:
            obj = Mineral(name=mineral.get('name', ''),
                          imgfile=mineral.get('image filename', ''),
                          imgcap=mineral.get('image caption', ''),
                          category=mineral.get('category', ''),
                          formula=mineral.get('formula', ''),
                          strunz_classification=mineral.get(
                            'strunz classification', ''),
                          color=mineral.get('color', ''),
                          crystal_system=mineral.get('crystal system', ''),
                          unit_cell=mineral.get('unit cell', ''),
                          crystal_symmetry=mineral.get(
                            'crystal symmetry', ''),
                          cleavage=mineral.get('cleavage', ''),
                          mohs_scale_hardness=mineral.get(
                            'mohs scale hardness', ''),
                          luster=mineral.get('luster', ''),
                          streak=mineral.get('streak', ''),
                          diaphaneity=mineral.get('diaphaneity', ''),
                          optical_properties=mineral.get(
                            'optical properties', ''),
                          refractive_index=mineral.get(
                            'refractive index', ''),
                          crystal_habit=mineral.get('crystal habit', ''),
                          specific_gravity=mineral.get(
                            'specific gravity', ''),
                          group=Group.objects.get(name=mineral.get('group', ''))
                         )
            minelist.append(obj)

    Mineral.objects.bulk_create(minelist)


class Migration(migrations.Migration):
    dependencies = [
        ('minerals', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(loadmin)
    ]

