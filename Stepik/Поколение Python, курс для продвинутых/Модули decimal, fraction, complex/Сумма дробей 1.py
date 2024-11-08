from fractions import Fraction as F
result = 0
for i in range(1, int(input()) + 1):
    result += F(1, i**2)
print(result)