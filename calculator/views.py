from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, кг': 0.3,
        'сыр, кг': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


def menu(request, name_dish):

    servings = int(request.GET.get('servings', 1))
    context = {'recipe': DATA[name_dish].copy()}

    if servings != 1:
        
        for key in context['recipe'].keys():
            
            if type(context['recipe'][key] * servings) == float: 
                context['recipe'][key] = round(context['recipe'][key] * servings, 2)
                
            if type(context['recipe'][key] * servings) == int: 
                context['recipe'][key] = context['recipe'][key] * servings

    return render(request, 'calculator/index.html', context)
