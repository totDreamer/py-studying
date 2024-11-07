from decimal import *
num = Decimal(input())
num_str = [abs(int(n)) for n in str(num) if n in '0123456789']
print(max(num_str) + min(num_str))