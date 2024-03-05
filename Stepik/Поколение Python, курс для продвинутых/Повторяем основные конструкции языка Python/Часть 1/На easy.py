from math import sqrt
first_number = int(input())
second_number = int(input())


def math_operations(*, first : int, second : int) -> int:
    sum = first + second
    dif = first - second
    multiply = first * second
    divide = first / second
    divide_by_zero = first // second
    remainder = first % second
    example = sqrt(first**10 + second**10)
    print(sum, dif, multiply, divide, divide_by_zero, remainder, example, sep = '\n')
    return sum, dif, multiply, divide, remainder, example

math_operations(first = first_number, second = second_number)