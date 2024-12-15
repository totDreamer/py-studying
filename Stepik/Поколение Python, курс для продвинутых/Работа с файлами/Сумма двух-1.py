file = open('numbers.txt', 'r', encoding='utf')
sum_numbers = sum(map(lambda x: int(x.rstrip()), file.readlines()))
print(sum_numbers)