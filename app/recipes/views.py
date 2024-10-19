from django.shortcuts import render
from django.views import View
# from utils.recipe_factory import make_recipe
from django.http import Http404
from recipes.models import Recipe


class Home(View):
    template = 'recipes/home/home.html'
    title = 'Home'

    def get(self, request):
        recipes = Recipe.objects.all().filter(
            is_published=True,
        ).order_by('-id')
        context = {
            'title': self.title,
            'recipes': recipes,
        }
        return render(request, self.template, context)


class RecipeView(View):
    template = 'recipes/recipe_view/recipe_view.html'
    title = 'Receita'

    def get(self, request, cod):
        recipe = Recipe.objects.filter(
            id=cod,
            is_published=True,
        )
        context = {
            'title': self.title,
            'recipe': recipe,
            'is_detail': True,
        }
        return render(request, self.template, context)


class CategoryView(View):
    template = 'recipes/category/category.html'
    title = 'Categorias'

    def get(self, request, cod_category):
        recipes = Recipe.objects.filter(
            category__id=cod_category,
            is_published=True,
        ).order_by('-id')

        if not recipes:
            raise Http404('Não Encontrado!')

        category_name = recipes.first().category.name

        context = {
            'title': f'{self.title} | {category_name}',
            'recipes': recipes,
        }
        return render(request, self.template, context)
