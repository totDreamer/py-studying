file = open('nums.txt', 'r', encoding='utf')
sum_numbers = sum(map(int, filter(lambda x: x.isdigit(), file.read().split())))
print(sum_numbers)
