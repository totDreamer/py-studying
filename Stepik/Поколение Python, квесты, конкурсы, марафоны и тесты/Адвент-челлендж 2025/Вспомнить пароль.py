def sum_mult_sum(num: int):
    str_num = str(num)
    digits_sum = sum(int(n) for n in str_num)
    digits_mult = 1
    for n in str_num:
        digits_mult *= int(n)
    
    if num == digits_mult + digits_sum:
        return True

for num in range(10, 100):
    if sum_mult_sum(num):
        print(num)