from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views


class RecipesURLsTest(TestCase):
    def test_home_url_is_correct(self):
        url = reverse('home')
        self.assertEqual(url, '/')

    def test_recipes_url_is_correct(self):
        url = reverse('recipe_view', args=(1,))
        self.assertEqual(url, '/recipes/1/')

    def test_category_url_is_correct(self):
        url = reverse('category', args=(100,))
        self.assertEqual(url, '/categories/100/')


class RecipeViewTest(TestCase):
    def test_recipe_home_is_correct(self):
        view = resolve(reverse('home'))
        self.assertTrue(view.func, views.Home.as_view())

    def test_recipe_recipe_is_correct(self):
        view = resolve(reverse('recipe_view', args=(1,)))
        self.assertTrue(view.func, views.RecipeView.as_view())

    def test_recipe_category_is_correct(self):
        view = resolve(reverse('category', args=(100,)))
        self.assertTrue(view.func, views.CategoryView.as_view())
