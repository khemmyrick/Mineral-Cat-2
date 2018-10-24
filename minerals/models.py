from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_min(self):
        return Mineral.objects.filter(group=self)


class Mineral(models.Model):
    name = models.CharField(max_length=250)
    imgfile = models.CharField(default='', max_length=250)
    imgcap = models.CharField(default='', max_length=250)
    category = models.CharField('category', max_length=250)
    formula = models.CharField('formula', max_length=250)
    strunz_classification = models.CharField('strunz classification',
                                             max_length=500)
    color = models.CharField('color', max_length=250)
    crystal_system = models.CharField('crystal system', max_length=250)
    unit_cell = models.CharField('unit cell', max_length=250)
    crystal_symmetry = models.CharField('crystal symmetry', max_length=250)
    cleavage = models.CharField('cleavage', max_length=250)
    mohs_scale_hardness = models.CharField('mohs scale hardness',
                                           max_length=250)
    luster = models.CharField('luster', max_length=250)
    streak = models.CharField('streak', max_length=250)
    diaphaneity = models.CharField('diaphaneity', max_length=250)
    optical_properties = models.CharField('optical properties',
                                          max_length=250)
    refractive_index = models.CharField('refractive index', max_length=250)
    crystal_habit = models.CharField('crystal habit', max_length=250)
    specific_gravity = models.CharField('specific gravity', max_length=250)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
