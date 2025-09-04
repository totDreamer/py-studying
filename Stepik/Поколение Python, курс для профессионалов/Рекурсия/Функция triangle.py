def triangle(num):
    if num > 0:
        print('*' * num)
        triangle(num - 1)

triangle(3)