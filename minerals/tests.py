import random
import unittest

from django.urls import reverse
from django.test import TestCase
from django.template import Context, Template

from .models import Group, Mineral
from minerals.templatetags import mineral_extras


class ModelTests(TestCase):
    def setUp(self):
        self.group = Group.objects.create(
            name="Crystal Gems"
        )
        self.mineral = Mineral.objects.create(
            name="Pearl",
            imgfile="Unusable Garbage",
            imgcap="Various pearls",
            category="Carbonate mineral, protein",
            formula="CaCO<sub>3</sub>",
            strunz_classification="05.AB",
            color="white, pink, silver, cream, etc",
            crystal_system="Orthorhombic",
            unit_cell="",
            crystal_symmetry="",
            cleavage="",
            mohs_scale_hardness="2.5–4.5",
            luster="",
            streak="white",
            diaphaneity="",
            optical_properties="",
            refractive_index="1.52-1.66",
            crystal_habit="",
            specific_gravity="2.60–2.85",
            group=self.group
        )

    def test_group_creation(self):
        self.assertEqual(self.group.name, 'Crystal Gems')

    def test_group_get_min(self):
        m_list = self.group.get_min()
        self.assertIn(self.mineral, m_list)

    def test_mineral_creation(self):
        self.assertIn(self.mineral, self.group.mineral_set.all())


class ViewsTests(TestCase):
    def setUp(self):
        self.cg = Group.objects.create(
            name="Crystal Gems"
        )
        self.hg = Group.objects.create(
            name="Homeworld Gems"
        )
        self.pearl = Mineral.objects.create(
            name="Pearl",
            imgfile="Unusable Garbage",
            imgcap="Various pearls",
            category="Carbonate mineral, protein",
            formula="<sub>pearl</sub>",
            strunz_classification="05.AB",
            color="white, pink, silver, cream, etc",
            crystal_system="Orthorhombic",
            unit_cell="",
            crystal_symmetry="",
            cleavage="",
            mohs_scale_hardness="2.5–4.5",
            luster="",
            streak="white",
            diaphaneity="",
            optical_properties="",
            refractive_index="1.52-1.66",
            crystal_habit="",
            specific_gravity="2.60–2.85",
            group=self.cg
        )
        self.amethyst = Mineral.objects.create(
            name="Amethyst",
            imgfile="Unusable Garbage",
            imgcap="Various amethysts",
            category="Carbonate mineral, protein",
            formula="<sub>amethyst</sub>",
            strunz_classification="05.AB",
            color="white, pink, silver, cream, etc",
            crystal_system="Orthorhombic",
            unit_cell="",
            crystal_symmetry="",
            cleavage="",
            mohs_scale_hardness="2.5–4.5",
            luster="",
            streak="purple",
            diaphaneity="",
            optical_properties="",
            refractive_index="1.52-1.66",
            crystal_habit="",
            specific_gravity="2.60–2.85",
            group=self.cg
        )
        self.rosequartz = Mineral.objects.create(
            name="Rose Quartz",
            imgfile="the leader of the crystal gems",
            imgcap="Rose Quartz faces Pink Diamond through a pane of glass",
            category="Carbonate mineral, protein",
            formula="<sub>pearl</sub>",
            strunz_classification="05.AB",
            color="white, pink, peach",
            crystal_system="Orthorhombic",
            unit_cell="",
            crystal_symmetry="flipped",
            cleavage="",
            mohs_scale_hardness="2.5–4.5",
            luster="",
            streak="justice",
            diaphaneity="",
            optical_properties="",
            refractive_index="1.52-1.66",
            crystal_habit="",
            specific_gravity="2.60–2.85",
            group=self.cg
        )
        self.garnet = Mineral.objects.create(
            name="Garnet",
            imgfile="unique but useless Garbage",
            imgcap="The Garnet",
            category="Carbonate mineral, protein",
            formula="<sub>garnet</sub>",
            strunz_classification="05.AB",
            color="purple, violet, cotten candy",
            crystal_system="Orthorhombic",
            unit_cell="",
            crystal_symmetry="",
            cleavage="",
            mohs_scale_hardness="2.5–4.5",
            luster="",
            streak="purple",
            diaphaneity="",
            optical_properties="",
            refractive_index="1.52-1.66",
            crystal_habit="",
            specific_gravity="2.60–2.85",
            group=self.cg
        )
        
        self.nephrite = Mineral.objects.create(
            name="Nephrite",
            imgfile="Unusable Garbage",
            imgcap="Various nephrites",
            category="Carbonate mineral, protein",
            formula="<sub>nephrite</sub>",
            strunz_classification="05.AB",
            color="white, pink, silver, cream, etc",
            crystal_system="Orthorhombic",
            unit_cell="",
            crystal_symmetry="",
            cleavage="",
            mohs_scale_hardness="2.5–4.5",
            luster="",
            streak="yellow",
            diaphaneity="",
            optical_properties="",
            refractive_index="1.52-1.66",
            crystal_habit="",
            specific_gravity="2.60–2.85",
            group=self.hg
        )
        self.jasper = Mineral.objects.create(
            name="Jasper",
            imgfile="Unusable Garbage",
            imgcap="Various jaspers",
            category="Carbonate mineral, protein",
            formula="<sub>jasper</sub>",
            strunz_classification="05.AB",
            color="white, pink, silver, cream, etc",
            crystal_system="Orthorhombic",
            unit_cell="",
            crystal_symmetry="",
            cleavage="",
            mohs_scale_hardness="2.5–4.5",
            luster="",
            streak="black and yellow",
            diaphaneity="",
            optical_properties="",
            refractive_index="1.52-1.66",
            crystal_habit="",
            specific_gravity="2.60–2.85",
            group=self.hg
        )
        self.dnw = ['DoesNotExist', 'MultipleObjectsReturned', '_state', 'id',
               'name', 'imgcap', 'imgfile', 'objects', 'group', 'category',
               'formula', 'group_id']
        self.dnw_member = random.choice(self.dnw)
        
        self.all_min = Mineral.objects.all()
        
        self.all_groups = Group.objects.all()
        
        self.cg_list = self.cg.get_min()
        
    def test_index_view(self):
        resp = self.client.get(reverse('minerals:index'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'minerals/mineral_list.html')
        self.assertFalse(resp.context['categ'])
        mineral1 = {'name': self.amethyst.name,
                    'group': self.amethyst.group.id,
                    'id': self.amethyst.id}
        mineral2 = {'name': self.rosequartz.name,
                    'group': self.rosequartz.group.id,
                    'id': self.rosequartz.id}
        self.assertIn(mineral1,
                      resp.context['minerals'])
        self.assertNotIn(mineral2,
                         resp.context['minerals'])
        
    def test_mineral_list_view(self):
        resp = self.client.get('/minerals/mineral_list/')
        self.assertEqual(resp.status_code, 200)
        self.assertFalse(resp.context['categ'])
        self.assertFalse(resp.context['group'])
        self.assertFalse(resp.context['target_color'])
        self.assertFalse(resp.context['term'])
        self.assertTemplateUsed(resp, 'minerals/mineral_list.html')
        mineral1 = {'name': self.rosequartz.name,
                    'group': self.rosequartz.group.id,
                    'id': self.rosequartz.id}
        mineral2 = {'name': self.garnet.name,
                    'group': self.garnet.group.id,
                    'id': self.garnet.id}
        mineral3 = {'name': self.nephrite.name,
                    'group': self.nephrite.group.id,
                    'id': self.nephrite.id}
        mineral4 = {'name': self.jasper.name,
                    'group': self.jasper.group.id,
                    'id': self.jasper.id}
        self.assertIn(mineral1,
                      resp.context['minerals'])
        self.assertIn(mineral2,
                      resp.context['minerals'])
        self.assertIn(mineral3,
                      resp.context['minerals'])
        self.assertIn(mineral4,
                      resp.context['minerals'])

    def test_mineral_detail_view(self):
        resp = self.client.get(
            reverse('minerals:mineral_detail',
                    kwargs={'pk': self.pearl.pk})
        )
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.pearl, resp.context['mineral'])
        self.assertNotIn(self.dnw_member, resp.context['attrlist'])
        self.assertTemplateUsed(resp, 'minerals/mineral_detail.html')
        self.assertIn('cleavage', resp.context['attrlist'][0])

    def test_random_mineral_view(self):
        resp = self.client.get(reverse('minerals:random_mineral'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'minerals/mineral_detail.html')
        self.assertTrue(resp.context['mineral'])

    def test_group_list_view(self):
        resp = self.client.get(
            reverse('minerals:group_list',
                    kwargs={'pk': self.hg.pk})
        )
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'minerals/mineral_list.html')
        mineral1 = {'name': self.nephrite.name,
                    'group': self.nephrite.group.id,
                    'id': self.nephrite.id}
        mineral2 = {'name': self.jasper.name,
                    'group': self.jasper.group.id,
                    'id': self.jasper.id}
        mineral3 = {'name': self.rosequartz.name,
                    'group': self.rosequartz.group.id,
                    'id': self.rosequartz.id}
        self.assertIn(mineral1,
                      resp.context['minerals'])
        self.assertIn(mineral2,
                      resp.context['minerals'])
        self.assertNotIn(mineral3,
                         resp.context['minerals'])

    def test_random_group_view(self):
        resp = self.client.get(reverse('minerals:random_group'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'minerals/mineral_list.html')
        self.assertTrue(resp.context['group'])
        self.assertFalse(resp.context['categ'])
        self.assertFalse(resp.context['target_color'])
        self.assertFalse(resp.context['term'])

    def test_by_alpha(self):
        resp = self.client.get(reverse('minerals:by_alpha',
                                       kwargs={'term': 'R'}))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'minerals/mineral_list.html')
        mineral1 = {'name': self.rosequartz.name,
                    'group': self.rosequartz.group.id,
                    'id': self.rosequartz.id}
        mineral2 = {'name': self.nephrite.name,
                    'group': self.nephrite.group.id,
                    'id': self.nephrite.id}
        mineral3 = {'name': self.amethyst.name,
                    'group': self.amethyst.group.id,
                    'id': self.amethyst.id}
        self.assertIn(mineral1,
                      resp.context['minerals'])
        self.assertNotIn(mineral2,
                         resp.context['minerals'])
        self.assertNotIn(mineral3,
                         resp.context['minerals'])

class MineralExtrasTests(TestCase):
    def setUp(self):
        self.cg = Group.objects.create(
            name="Crystal Gems"
        )
        self.hg = Group.objects.create(
            name="HomeWorld Gems"
        )
        self.pearl = Mineral.objects.create(
            name="Pearl",
            imgfile="Unusable Garbage",
            imgcap="Various pearls",
            category="Carbonate mineral, protein",
            formula="<sub>pearl</sub>",
            strunz_classification="05.AB",
            color="white, pink, silver, cream, etc",
            crystal_system="Orthorhombic",
            unit_cell="",
            crystal_symmetry="",
            cleavage="",
            mohs_scale_hardness="2.5–4.5",
            luster="",
            streak="white",
            diaphaneity="",
            optical_properties="",
            refractive_index="1.52-1.66",
            crystal_habit="",
            specific_gravity="2.60–2.85",
            group=self.cg
        )
        self.amethyst = Mineral.objects.create(
            name="Amethyst",
            imgfile="Unusable Garbage",
            imgcap="Various amethysts",
            category="Carbonate mineral, protein",
            formula="<sub>amethyst</sub>",
            strunz_classification="05.AB",
            color="white, pink, silver, cream, etc",
            crystal_system="Orthorhombic",
            unit_cell="",
            crystal_symmetry="",
            cleavage="",
            mohs_scale_hardness="2.5–4.5",
            luster="",
            streak="purple",
            diaphaneity="",
            optical_properties="",
            refractive_index="1.52-1.66",
            crystal_habit="",
            specific_gravity="2.60–2.85",
            group=self.cg
        )

    def test_underspace(self):
        output = mineral_extras.underspace('attr_string')
        self.assertEqual(output, 'attr string')

    def test_jpegger(self):
        self.m_str = mineral_extras.jpegger(self.cg.name)
        self.assertIn('.jpg', self.m_str)
        self.assertIn(self.m_str, ['Amethyst.jpg', 'Pearl.jpg'])

    def test_nav_groups_list(self):
        context = Context({'group': self.cg})
        template_to_render = Template(
            '{% load mineral_extras %}'
            '{% nav_groups_list %}'
        )
        rendered_template = template_to_render.render(context)
        # self.assertInHTML(
        #    '<li class="group__bold">Crystal Gems</li>',
        #    rendered_template
        # )
        self.assertIn(
            '<li class="group__bold">Crystal Gems</li>',
            rendered_template
        )
        self.assertNotIn(
            '<li class="group__bold">HomeWorld Gems</li>',
            rendered_template
        )

    def test_color_list(self):
        context = Context({'target_color': 'Colorless'})
        template_to_render = Template(
            '{% load mineral_extras %}'
            '{% color_list %}'
        )
        rendered_template = template_to_render.render(context)
        # self.assertInHTML(
        #    '<li class="group__bold">Colorless</li>',
        #    rendered_template
        # )
        self.assertIn(
            '<li class="group__bold">Colorless</li>',
            rendered_template
        )
        self.assertNotIn(
            '<li class="group__bold">White</li>',
            rendered_template
        )

    def test_abc_list(self):
        context = Context({'term': 'A'})
        template_to_render = Template(
            '{% load mineral_extras %}'
            '{% abc_list %}'
        )
        rendered_template = template_to_render.render(context)
        # self.assertInHTML(
        #    '<span style="color: white; font-weight: bold;">A</span>',
        #    rendered_template
        # )
        self.assertIn(
            '<span style="color: white; font-weight: bold;">A</span>',
            rendered_template
        )
        self.assertNotIn(
            '<span style="color: white; font-weight: bold;">B</span>',
            rendered_template
        )
