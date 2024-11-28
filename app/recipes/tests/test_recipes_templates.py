from django.test import TestCase
from django.urls import reverse
# import pdb


class TemplatesLoadTest(TestCase):
    def test_recipe_home_view_load_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'recipes/home/home.html')
