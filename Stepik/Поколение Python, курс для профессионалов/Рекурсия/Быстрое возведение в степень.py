def get_fast_pow(a, n):
    if n == 0:
        return 1
    if n % 2 == 1:
        return a * get_fast_pow(a, n-1)
    else:
        return get_fast_pow(a, n // 2) * get_fast_pow(a, n // 2)

print(get_fast_pow(2, 10))
print(get_fast_pow(5, 2))