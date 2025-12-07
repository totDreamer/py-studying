def palindromes():
    start = 0

    def is_palindrome(num):
        s = str(num)
        return s == s[::-1]

    def next_num():
        nonlocal start
        start += 1
        if is_palindrome(start):
            yield start

    while True:
        yield from next_num()


for i, num in enumerate(palindromes()):
    if i > 20:
        break
    print(num)