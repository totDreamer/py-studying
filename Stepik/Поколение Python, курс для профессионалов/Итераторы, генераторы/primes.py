def primes(left, right):
    def is_simple(num):
        if num != 1:
            return all(num % div for div in range(2, num // 2 + 1))
    for num in filter(is_simple, range(left, right + 1)):
        yield num

generator = primes(1, 15)
print(*generator)