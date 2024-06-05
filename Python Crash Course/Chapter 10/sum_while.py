print("Hello. This is a simple two number calculator")
while True:
    first_num = input("Enter the first number: ")
    if first_num == "q":
        break
    second_num = input("Enter the second number:")
    if second_num == "q":
        break
    try:
        first_num = int(first_num)
        second_num = int(second_num)

    except ValueError:
        print("Please, enter two numbers. Not words")

    else:
        print(f"The sum of two numbers is {first_num + second_num}\nIf you want to close the program then enter 'q'")
