from itertools import product

def ch_counter(n, m):
    chars = '0123456789ABCDEF'
    for tup in product(chars[:n], repeat=m):
        yield (''.join(str(num) for num in tup))


print(*ch_counter(int(input()), int(input())))
print(*ch_counter(2, 3))
print(*ch_counter(3, 2))
