def multiplication_of_two_numbers(*, count : int):
    list_of_numbers = []
    result = False
    for j in range(count):
        list_of_numbers.append(int(input()))
    final_number = int(input())
    for number in range(len(list_of_numbers)):
        for number2 in range(number+1, len(list_of_numbers)):
            if list_of_numbers[number] * list_of_numbers[number2] == final_number:
                result = True
    if result == True:
        return "ДА"
    else:
        return "НЕТ"


print(multiplication_of_two_numbers(count = int(input())))