def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Проверяем только нечетные числа до корня из n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

data = (1537, 27644437, 1, 101, 19922991, 271828, 1100101, 31415, 4801)
prime_count = sum(1 for num in data if is_prime(num))

if prime_count > len(data) // 2:
    print(sum(data))
else:
    result = 1
    for num in data:
        result *= num
    print(result)