def hi_five(num):
    base = num
    flag = True

    def plus_minus(num):
        nonlocal flag
        print(num)
        if num <= 0:
            flag = False
        if flag:
            return plus_minus(num - 5)
        elif not flag and num < base:
            return plus_minus(num + 5)
    
    plus_minus(num)

hi_five(16)