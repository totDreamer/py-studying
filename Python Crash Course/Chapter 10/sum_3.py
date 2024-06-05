print("Hello. This is a simple two number calculator")
first_num = input("Enter the first number: ")
second_num = input("Enter the second number:")
try:
    first_num = int(first_num)
    second_num = int(second_num)

except ValueError:
    print("Please, enter two numbers. Not words")

else:
    print("The sum of two numbers is", first_num + second_num)