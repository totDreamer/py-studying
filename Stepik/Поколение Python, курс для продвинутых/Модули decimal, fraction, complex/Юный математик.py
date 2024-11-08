from fractions import Fraction as F
num = int(input())
numerator = [i for i in range(1, num // 2 + 1)]
denominator = [i for i in range(num - 1, num // 2 - 1, -1)]

result = [F(n, d) for n, d in zip(numerator, denominator)]
result = [i for i in result if i.numerator + i.denominator == num]

print(max(result))