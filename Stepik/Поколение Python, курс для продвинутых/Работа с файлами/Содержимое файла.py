file = open(input(), 'r', encoding='utf')
for line in file:
    print(line.rstrip())
file.close()