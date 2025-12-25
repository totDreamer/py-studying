def next_palindrome(n):
    length = len(n)

    if all(c == '9' for c in n):
        return '1' + '0' * (length - 1) + '1'

    half = (length + 1) // 2
    left = n[:half]

    if length % 2 == 0:
        pal = left + left[::-1]
    else:
        pal = left + left[:-1][::-1]

    if pal > n:
        return pal

    left_inc = str(int(left) + 1).zfill(len(left))

    if length % 2 == 0:
        return left_inc + left_inc[::-1]
    else:
        return left_inc + left_inc[:-1][::-1]


print(next_palindrome(input()))