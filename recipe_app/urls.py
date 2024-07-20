from django.urls import path
from .views import RecipeDetailView, RecipeListView

urlpatterns = [
    path('api/recipe/', RecipeDetailView.as_view(), name='recipe-detail'),
    path('api/recipes/', RecipeListView.as_view(), name='recipe-list'),
]
