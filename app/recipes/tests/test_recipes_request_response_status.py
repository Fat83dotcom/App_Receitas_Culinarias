from django.test import TestCase
from django.urls import reverse
from recipes import views
from recipes.models import Category, Recipe, User
# import pdb


class RecipeRequestResponse(TestCase):
    def test_recipes_home_request_response_200(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_recipes_home_shows_no_recipe_found_if_no_recipes_response_404(
        self
    ):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 404)

    def test_recipes_recipeview_request_response_200(self):
        response = self.client.get(reverse('recipe_view', args=(1555,)))
        self.assertEqual(response.status_code, 200)

    def test_recipes_recipeview_shows_not_found_if_no_recipes_response_404(
        self
    ):
        response = self.client.get(reverse('recipe_view', args=(1,)))
        self.assertEqual(response.status_code, 404)

    def test_recipes_categoryview_request_response_200(self):
        response = self.client.get(reverse('category', args=(1333,)))
        self.assertEqual(response.status_code, 200)

    def test_recipes_category_shows_not_found_if_no_recipes_response_404(
        self
    ):
        response = self.client.get(reverse('category', args=(1444,)))
        self.assertEqual(response.status_code, 404)
