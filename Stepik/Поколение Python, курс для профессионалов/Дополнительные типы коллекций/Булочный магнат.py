from collections import ChainMap, Counter 

bread = {'булочка с кунжутом': 15, 'обычная булочка': 10, 'ржаная булочка': 15}
meat = {'куриный бифштекс': 50, 'говяжий бифштекс': 70, 'рыбный бифштекс': 40}
sauce = {'сливочно-чесночный': 15, 'кетчуп': 10, 'горчица': 10, 'барбекю': 15, 'чили': 15}
vegetables = {'лук': 10, 'салат': 15, 'помидор': 15, 'огурцы': 10}
toppings = {'сыр': 25, 'яйцо': 15, 'бекон': 30}

menu = ChainMap(bread, meat, sauce, vegetables, toppings)

def print_check(ingridients):
    counter = Counter(ingridients.split(','))
    total_sum = 0
    max_len = len(max(counter.keys(), key=len))
    max_space = max_len + 3 + len(str(max(counter.values())))

    for position in ingridients.split(','):
        total_sum += menu[position]

    for item, count in sorted(counter.items(), key=lambda x: x[0]):
        space = ' ' * (max_len - len(item))
        print(f'{item}{space} x {count}')

    if max_space < len(str(total_sum)) + 7:
        max_space = len(str(total_sum)) + 7
    delim_space = '-' * max_space
    
    print(delim_space)
    print(f'ИТОГ: {total_sum}р')

print_check(input())