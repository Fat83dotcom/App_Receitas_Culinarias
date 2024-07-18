from django.shortcuts import render
from django.views import View
from utils.recipe_factory import make_recipe
from recipes.models import Recipe


class Home(View):
    template = 'recipes/home/home.html'
    title = 'Home'

    def get(self, request):
        recipes = Recipe.objects.all().order_by('-id')
        context = {
            'title': self.title,
            'recipes': recipes,
        }
        return render(request, self.template, context)


class RecipeView(View):
    template = 'recipes/recipe_view/recipe_view.html'
    title = 'Receita'

    def get(self, request, cod):
        context = {
            'title': self.title,
            'recipe': make_recipe(),
            'is_detail': True,
        }
        return render(request, self.template, context)
