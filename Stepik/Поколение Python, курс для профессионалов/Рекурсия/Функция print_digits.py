def print_digits(number):
    number = list(str(number))
    def new_pop():
        print(number.pop())
        if len(number) > 0:
            new_pop()
    new_pop()

print_digits(12345)
print_digits(123987)