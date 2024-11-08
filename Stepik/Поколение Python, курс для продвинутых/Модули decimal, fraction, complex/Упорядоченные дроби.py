from fractions import Fraction as F

dig_list = [i for i in range(1, int(input()) + 1)]
fractions_list = sorted({F(n, d) for n in dig_list for d in dig_list if n < d})

print(*fractions_list, sep='\n')