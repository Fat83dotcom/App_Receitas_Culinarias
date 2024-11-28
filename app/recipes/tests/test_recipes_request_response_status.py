from django.test import TestCase
from django.urls import reverse
import pdb


class RecipeRequestResponse(TestCase):
    def test_recipes_home_request_response_200_OK(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_recipes_home_template_shows_no_recipe_found_if_no_recipes(self):
        response = self.client.get(reverse('home'))
        #pdb.set_trace()
        self.assertEqual(response.status_code, 404)

    def test_recipes_recipeview_request_response_200_OK(self):
        response = self.client.get(reverse('recipe_view', args=(1,)))
        self.assertEqual(response.status_code, 200)

    def test_recipes_categoryview_request_response_200_OK(self):
        response = self.client.get(reverse('category', args=(1,)))
        self.assertEqual(response.status_code, 200)
