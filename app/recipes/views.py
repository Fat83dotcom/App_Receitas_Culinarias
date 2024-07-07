from django.shortcuts import render
from django.views import View


class Home(View):
    template = 'recipes/home.html'

    def get(self, request):
        return render(request, self.template)
