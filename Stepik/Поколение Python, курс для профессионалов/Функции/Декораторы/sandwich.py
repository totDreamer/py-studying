def sandwich(f):
    def wrapper(*args, **kwargs):
        print('---- Верхний ломтик хлеба ----')
        result = f(*args, **kwargs)
        print('---- Нижний ломтик хлеба ----')
        return result

    return wrapper

@sandwich
def add_ingredients(ingredients):
    print(' | '.join(ingredients))

add_ingredients(['томат', 'салат', 'сыр', 'бекон'])


@sandwich
def beegeek():
    return 'beegeek'
    
print(beegeek())