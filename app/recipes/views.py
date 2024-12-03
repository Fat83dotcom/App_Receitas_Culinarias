from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.views import View
from recipes.models import Recipe

# import pdb


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
        if not recipes:
            return render(request, self.template, context, status=404)
        return render(request, self.template, context)


class RecipeView(View):
    template = 'recipes/recipe_view/recipe_view.html'
    title = 'Receita'

    def get(self, request, cod):
        recipe = Recipe.objects.all().filter(id=cod, is_published=True).first()
        if not recipe:
            return render(request, self.template, status=404)
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
        recipe = Recipe.objects.all().filter(
            category__id=cod_category,
            is_published=True,
        ).order_by('-id').first()

        if not recipe:
            return render(request, self.template, status=404)
        context = {
            'title': f'{self.title} | {recipe.category.name}',
            'recipe': recipe,
        }
        return render(request, self.template, context)
