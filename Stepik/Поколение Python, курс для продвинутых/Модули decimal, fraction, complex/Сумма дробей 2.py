from fractions import Fraction as F
from math import factorial
result = 0
for i in range(1, int(input()) + 1):
    result += F(1, factorial(i))
print(result)