def limited_hash(left, right, hash_function=hash):
    def wrapper(obj):
        result = hash_function(obj)
        length = right - left + 1
        return (result - left) % length + left

    return wrapper


hash_function = limited_hash(10, 15)

print(hash_function(10))
print(hash_function(11))
print(hash_function(15))

print()

hash_function = limited_hash(10, 15)

print(hash_function(16))
print(hash_function(17))
print(hash_function(21))
print(hash_function(22))
print(hash_function(23))

print()

hash_function = limited_hash(10, 15)

print(hash_function(9))
print(hash_function(8))
print(hash_function(4))
print(hash_function(3))
print(hash_function(2))
