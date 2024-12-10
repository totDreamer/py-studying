def evaluate(coefficients, x):
    coef_range = [i for i in range(len(coefficients)-1, -1, -1)]
    coefficients = list(map(int, coefficients))
    return sum(map(lambda i: coefficients[i] * x**coef_range[i], range(len(coef_range))))

new_coef, x = input().split(), int(input())
print(evaluate(new_coef, x))