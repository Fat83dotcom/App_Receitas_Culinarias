from django.urls import path
from recipes import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('recipes/<int:cod>/', views.RecipeView.as_view(), name='recipe_view'),
    path(
        'categories/<int:cod_category>/',
        views.CategoryView.as_view(),
        name='category'
    ),
]
