def suefa(*, first_symbol : str, second_symbol : str):
    symbols = ["камень", "ножницы", "бумага"]
    if first_symbol == second_symbol:
        return "ничья"
    elif first_symbol == symbols[0] and second_symbol == symbols[1]:
        return "Тимур"
    elif first_symbol == symbols[1] and second_symbol == symbols[2]:
        return "Тимур"
    elif first_symbol == symbols[2] and second_symbol == symbols[0]:
        return "Тимур"
    else:
        return "Руслан"

print(suefa(first_symbol=input(), second_symbol=input()))