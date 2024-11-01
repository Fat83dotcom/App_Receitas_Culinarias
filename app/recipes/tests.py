from django.test import TestCase
from django.urls import reverse


class RecipesURLsTest(TestCase):
    def test_home_url_is_correct(self):
        url = reverse('home')
        print(f'Caminho retornado por reverse: {url}')
        self.assertEqual(url, '/')

    def test_recipes_url_is_correct(self):
        url = reverse('recipe_view', args=(1,))
        print(f'Caminho retornado por reverse: {url}')
        self.assertEqual(url, '/recipes/1/')

    def test_category_url_is_correct(self):
        url = reverse('category', args=(100,))
        print(f'Caminho retornado por reverse: {url}')
        self.assertEqual(url, '/categories/100/')
