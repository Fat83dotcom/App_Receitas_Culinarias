from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.views import View
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
        recipe = get_object_or_404(
            Recipe,
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
        recipes = get_list_or_404(Recipe.objects.filter(
            category__id=cod_category,
            is_published=True,
        ).order_by('-id'))

        context = {
            'title': f'{self.title} | {recipes[0].category.name}',
            'recipes': recipes,
        }
        return render(request, self.template, context)
