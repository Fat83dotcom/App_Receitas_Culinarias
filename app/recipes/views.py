from django.shortcuts import render
from django.views import View


class Home(View):
    template = 'recipes/home/home.html'
    title = 'Home'

    def get(self, request):
        context = {
            'title': self.title
        }
        return render(request, self.template, context)


class RecipeView(View):
    template = 'recipes/recipe_view/recipe_view.html'
    title = 'Receita'

    def get(self, request, cod):
        context = {
            'title': self.title
        }
        return render(request, self.template, context)
