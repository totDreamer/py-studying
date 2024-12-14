from functools import reduce
def product_of_odds(data):
    return reduce(lambda x, y: x * y, filter(lambda y: y % 2 == 1, data), 1)

print(product_of_odds([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))