import json
from django.http import JsonResponse
from django.views import View
import os

class RecipeView(View):
    def get(self, request):
        json_path = os.path.join(os.path.dirname(__file__), '../recipe_project/recipes.json')
        with open(json_path, 'r') as file:
            recipes = json.load(file)
        return JsonResponse(recipes, safe=False)
