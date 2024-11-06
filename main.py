"""linter"""
import json


def adjust_recipe(recipe, servings):
    current_servings = recipe.get("servings", 1)
    factor = servings / current_servings
    adjusted_ingredients = {
        ingredient: round(quantity * factor, 2)
        for ingredient, quantity in recipe["ingredients"].items()
    }
    return {
        "title": recipe["title"],
        "servings": servings,
        "ingredients": adjusted_ingredients
    }


def load_recipe(recipe):
    return json.loads(recipe)


if __name__ == "__main__":
    # Beispiel für die Datenstruktur eines Rezepts
    recipe_json = ('{"title": "Spaghetti Bolognese", "ingredients": {"Spaghetti": 400, "Tomato Sauce": 300, '
                   '"Minced Meat": 500}, "servings": 4}')
    adjust_recipe(recipe_json, 3)

