from datetime import date

def is_correct(day, month, year):
    try:
        date(year, month, day)
        return 'Корректная', True
    except:
        return 'Некорректная', False

data = input()
count = 0

while data != 'end':
    day, month, year = (int(i) for i in data.split('.'))
    
    result, is_valid = is_correct(day, month, year)
    print(result)
    
    if is_valid:
        count += 1
    
    data = input()

print(count)
