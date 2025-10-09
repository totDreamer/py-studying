def power(degree: int):
    def math(x):
        return x**degree
    return math

square = power(2)
print(square(5))
