def numbers_sum(elems: list) -> (int, float):
    """Принимает список и возвращает сумму его чисел (int, float),
игнорируя нечисловые объекты. 0 - если в списке чисел нет."""
    if not elems:
        return 0
    return sum(filter(lambda x: type(x) in (int, float), elems))

print(numbers_sum([1, '2', 3, 4, 'five']))
print(numbers_sum(['beegeek', 'stepik', '100']))
print(numbers_sum.__doc__)