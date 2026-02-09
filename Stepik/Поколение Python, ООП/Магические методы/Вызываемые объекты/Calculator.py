class Calculator:
    def __call__(self, a, b, operation):
        if operation == "/" and b == 0:
            raise ValueError("Деление на ноль невозможно")
        return eval(f"{a}{operation}{b}")


calculator = Calculator()

print(calculator(10, 5, "+"))
print(calculator(10, 5, "-"))
print(calculator(10, 5, "*"))
print(calculator(10, 5, "/"))


calculator = Calculator()

try:
    print(calculator(10, 0, "/"))
except ValueError as e:
    print(e)
    print(type(e))
