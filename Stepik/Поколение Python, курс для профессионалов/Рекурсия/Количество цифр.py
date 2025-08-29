def fckng_len(num):
    if num == 0:
        return 0
    return 1 + fckng_len(num//10)


print(fckng_len(50))
print(fckng_len(78566))
print(fckng_len(input()))