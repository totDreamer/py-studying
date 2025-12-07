from functools import lru_cache

@lru_cache
def ways(n):
    if n <= 3:
        return 1
    if n == 4:
        return 2
    return ways(n-1) + ways(n-3) + ways(n-4)

print(ways(5))
print(ways(1))
print(ways(2))