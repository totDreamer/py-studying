def suefa(*, first_symbol : str, second_symbol : str):
    symbols = ["ножницы", "бумага", "камень", "ящерица", "Спок"]
    result = ["Тимур", "Руслан", "ничья"]
    first_index = symbols.index(first_symbol)
    second_index = symbols.index(second_symbol)
    if first_index == second_index:
        return result[2]
    elif (first_index - second_index) % 2 == 0:
        if first_index > second_index:
            return result[0]
        else:
            return result[1]
    elif (first_index - second_index) % 2 != 0:
        if first_index < second_index:
            return result[0]
        else:
            return result[1]
print(suefa(first_symbol=input(), second_symbol=input()))