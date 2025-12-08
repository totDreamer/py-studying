from collections import namedtuple
from itertools import combinations

Item = namedtuple('Item', ['name', 'mass', 'price'])

items = [Item('Обручальное кольцо', 7, 49_000),
         Item('Мобильный телефон', 200, 110_000),
         Item('Ноутбук', 2000, 150_000),
         Item('Ручка Паркер', 20, 37_000),
         Item('Статуэтка Оскар', 4000, 28_000),
         Item('Наушники', 150, 11_000),
         Item('Гитара', 1500, 32_000),
         Item('Золотая монета', 8, 140_000),
         Item('Фотоаппарат', 720, 79_000),
         Item('Лимитированные кроссовки', 300, 80_000)]


def high_price_stuff(weight):
    right_comb = set()

    for i in range(1, 11):
        for c in filter(lambda x: sum(obj.mass for obj in x) <= int(weight), combinations(items, i)):
            right_comb.add(c)
    
    if not right_comb:
        return ('Рюкзак собрать не удастся',)
    
    best_comp = sorted(obj.name for obj in max(right_comb, key=lambda x: sum(obj.price for obj in x)))
    
    return best_comp

print(*high_price_stuff(input()), sep='\n')