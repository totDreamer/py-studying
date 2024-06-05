def sum_of_two(*, first_num : int, second_num : int):

    try:
        first_num + second_num

    except ValueError:
        print("Please, enter two numbers. Not words")

    else:
        print("The sum of two numbers is", first_num + second_num)


sum_of_two(first_num=1, second_num=2)
sum_of_two(first_num=55, second_num=2)
sum_of_two(first_num=1, second_num=542)
sum_of_two(first_num=567, second_num=2)