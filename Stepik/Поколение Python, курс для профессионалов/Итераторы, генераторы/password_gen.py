from itertools import product

def password_gen():
    for i in range(10):
        for j in range(10):
            for k in range(10):
                yield str(i) + str(j) + str(k)

passwords = password_gen()

print(next(passwords))
print(next(passwords))
print(next(passwords))

def password_gen():
    data = product(range(10), range(10), range(10))
    for tup in data:
        yield ''.join(str(d) for d in tup)


passwords = password_gen()

print(next(passwords))
print(next(passwords))
print(next(passwords))