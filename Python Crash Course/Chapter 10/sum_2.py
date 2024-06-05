print("Hello. This is a simple two number calculator")
first_num, second_num = map(int, input("Enter first number and second number separated by one space:\n\t").split())
try:
    first_num + second_num

except ValueError:
    print("Please, enter two numbers. Not words")

else:
    print("The sum of two numbers is", first_num + second_num)