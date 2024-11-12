from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views


class RecipeViewTest(TestCase):
    def test_recipe_home_is_correct(self):
        view = resolve(reverse('home'))
        self.assertIs(view.func.view_class, views.Home)

    def test_recipe_recipe_is_correct(self):
        view = resolve(reverse('recipe_view', args=(1,)))
        self.assertIs(view.func.view_class, views.RecipeView)

    def test_recipe_category_is_correct(self):
        view = resolve(reverse('category', args=(100,)))
        self.assertIs(view.func.view_class, views.CategoryView)
