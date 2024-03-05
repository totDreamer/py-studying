def str_price(*, str : str) -> str:
    price = len(str) * 60
    return f"{price//100} р. {price%100} коп."

s = input()
print(str_price(str = s))