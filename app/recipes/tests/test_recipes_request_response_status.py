from django.test import TestCase
from django.urls import reverse
# import pdb


class RecipeRequestResponse(TestCase):
    def test_recipes_request_response_200_OK(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
