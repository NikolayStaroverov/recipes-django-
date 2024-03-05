from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def omlet(request):
    num = int(request.GET.get("servings", 1))
    recipe = DATA['omlet']
    recipe_new={}
    for a, b in recipe.items():
        recipe_new[a] = str(num*float(b))
    context = {"recipe": recipe_new}
    return render(request,'index.html', context)

def pasta(request):
    num = int(request.GET.get("servings", 1))
    recipe = DATA['pasta']
    recipe_new = {}
    for a, b in recipe.items():
        recipe_new[a] = str(num * float(b))
    context = {"recipe": recipe_new}
    return render(request, 'index.html', context)

def buter(request):
    num = int(request.GET.get("servings", 1))
    recipe = DATA['pasta']
    recipe_new = {}
    for a, b in recipe.items():
        recipe_new[a] = str(num * float(b))
    context = {"recipe": recipe_new}
    return render(request, 'index.html', context)