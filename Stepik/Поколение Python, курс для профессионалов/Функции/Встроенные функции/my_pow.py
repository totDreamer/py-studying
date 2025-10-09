def my_pow(number):
    numbers = enumerate([int(num) for num in list(str(number))], 1)
    return sum(num[1]**num[0] for num in numbers)

print(my_pow('139'))