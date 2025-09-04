def one_hundred():
    def print_num(num):
        if num <= 100:
            print(num)
            print_num(num + 1)

    print_num(1)

one_hundred()