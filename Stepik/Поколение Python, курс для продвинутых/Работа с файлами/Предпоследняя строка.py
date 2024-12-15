file = open(input(), 'r', encoding='utf')

print(file.readlines()[-2].rstrip())

file.close()