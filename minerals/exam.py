import random

from django.urls import reverse
from django.test import TestCase
from django.test import Client

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
        # Check that by_alpha runs.
        # self.assertIn(self.cg, resp.context['groups'])
        # self.assertIn(self.hg, resp.context['groups'])
        
    def test_mineral_list_view(self):
        resp = self.client.get(reverse('minerals:mineral_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn('', resp.context['categ'])
        self.assertIn('', resp.context['group'])
        self.assertIn('', resp.context['target_color'])
        self.assertIn('', resp.context['term'])
        self.assertTemplateUsed(resp.context['term'], 'minerals/mineral_list.html')
        # assert isinstance(resp.context['minerals'], self.QuerySet)
        # self.assertIn(dict, resp.context['minerals'])
        # self.assertIn(self.amethyst, resp.context['minerals'])
        # self.assertIn(self.nephrite, resp.context['minerals'])
        # self.assertIn(self.jasper, resp.context['minerals'])

#    def test_mineral_list_view(self):
#        resp = self.client.get(reverse('minerals:mineral_list',
#                                       kwargs={'streak': 'justice'}))
#        self.assertEqual(resp.status_code, 200)
#    
    def test_mineral_detail_view(self):
        resp = self.client.get(reverse('minerals:mineral_detail',
                                       kwargs={'pk': self.pearl.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.pearl, resp.context['mineral'])
        self.assertNotIn(self.dnw_member, resp.context['attrlist'])
        self.assertIn('cleavage', resp.context['attrlist'][0])
        
    def test_random_mineral_view(self):
        resp = self.client.get(reverse('minerals:random_mineral'))
        self.assertEqual(resp.status_code, 200)
        # self.assertIn(resp.context['mineral'], self.all_min)

    def test_group_list_view(self):
        resp = self.client.get(reverse('minerals:group_list',
                                       kwargs={'pk': self.hg.pk}))
        self.assertEqual(resp.status_code, 200)
        # self.assertIn(self.nephrite, resp.context['minerals'])
        # self.assertIn(self.jasper, resp.context['minerals'])
        # self.assertEqual(self.hg, resp.context['group'])

    def test_random_group_view(self):
        resp = self.client.get(reverse('minerals:random_group'))
        self.assertEqual(resp.status_code, 200)
        # self.assertIn(resp.context['group'], self.all_groups)

class MineralExtrasTests(TestCase):
    def test_underspace(self):
        output = mineral_extras.underspace('attr_string')
        self.assertEqual(output, 'attr string')

    def test_jpegger(self):
        self.cg = Group.objects.create(
            name="Crystal Gems"
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
        self.m_str = mineral_extras.jpegger(self.cg.name)
        self.assertIn('.jpg', self.m_str)
        self.assertIn(self.m_str, ['Amethyst.jpg', 'Pearl.jpg'])

    def test_nav_groups_list(self):
        pass

    def test_color_list(self):
        pass

    def test_abc_list(self):
        pass
