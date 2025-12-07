def is_prime(number):
    if number < 2:
        return False
    return(all(number % n for n in range(2, int(number**0.5) + 1)))

print(is_prime(7))
print(is_prime(8))
print(is_prime(1))