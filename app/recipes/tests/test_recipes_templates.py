from django.test import TestCase
from django.urls import reverse
# import pdb


class TemplatesLoadTest(TestCase):
    def test_recipe_home_view_load_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'recipes/home/home.html')

    def test_recipe_ecipe_view_view_load_correct_template(self):
        response = self.client.get(reverse('recipe_view', args=(1,)))
        self.assertTemplateUsed(
            response, 'recipes/recipe_view/recipe_view.html'
        )

    def test_recipe_category_view_load_correct_template(self):
        response = self.client.get(reverse('category', args=(30,)))
        self.assertTemplateUsed(
            response, 'recipes/category/category.html'
        )
