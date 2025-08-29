def to_binary(n):
    if n <= 1:
        return str(n)
    return str(to_binary(n//2)) + str(n % 2)

print(to_binary(15))
print(to_binary(7))
print(to_binary(8))
print(to_binary(0))