# объявление функции
def is_even(num1, num2):
    if num1 % num2 == 0:
        return "делится"
    else:
        return "не делится"

# считываем данные
print(is_even(num1 = int(input()), num2 = int(input())))