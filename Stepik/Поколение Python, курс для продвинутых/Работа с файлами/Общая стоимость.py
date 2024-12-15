file = open('prices.txt', 'r', encoding='utf')
result = sum([int(num.split()[-1]) * int(num.split()[-2]) for num in file.readlines()])
print(result)