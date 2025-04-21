import sys

height = [int(line.strip()) for line in sys.stdin]
if len(height) > 0:
    print(f'Рост самого низкого ученика: {min(height)}\nРост самого высокого ученика: {max(height)}\nСредний рост: {sum(height)/len(height)}')
else:
    print('нет учеников')