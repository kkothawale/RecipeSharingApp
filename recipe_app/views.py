import json
from django.http import JsonResponse
from django.views import View
import os
import json

def load_recipes_from_file():
    json_path = os.path.join(os.path.dirname(__file__), '../recipe_project/recipes.json')
    with open(json_path, 'r') as f:
        return json.load(f)

# class RecipeView(View):
#     def get(self, request):
#         json_path = os.path.join(os.path.dirname(__file__), '../recipe_project/recipes.json')
#         with open(json_path, 'r') as file:
#             recipes = json.load(file)
#         return JsonResponse(recipes, safe=False)


class RecipeDetailView(View):
    def get(self, request):
        recipe_id = request.GET.get('id')
        recipes = load_recipes_from_file()
        if recipe_id:
            try:
                recipe_id = int(recipe_id)
                recipe = next((r for r in recipes if r["id"] == recipe_id), None)
                if recipe:
                    return JsonResponse(recipe, safe=False)
                else:
                    return JsonResponse({'error': 'Recipe not found'}, status=404)
            except ValueError:
                return JsonResponse({'error': 'Invalid recipe ID'}, status=400)
        else:
            return JsonResponse({'error': 'Recipe ID not provided'}, status=400)
        

class RecipeListView(View):
    def get(self, request):
        recipes = load_recipes_from_file()
        recipe_summaries = [
            {
                "id": r["id"],
                "name": r["name"],
                "author": r.get("author", "Unknown"),  # Assuming author is a field in your JSON data
                "image": r["image"],
                "rating": r["rating"]
            }
            for r in recipes
        ]
        return JsonResponse(recipe_summaries, safe=False)
