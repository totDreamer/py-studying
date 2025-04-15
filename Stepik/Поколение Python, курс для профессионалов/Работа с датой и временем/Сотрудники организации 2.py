from datetime import datetime

def massive_date(number_of_people):
    birthday_dates = {}
    pattern = '%d.%m.%Y'

    for _ in range(number_of_people):
        string = input().split()
        birthday_dates[string[2]] = birthday_dates.get(string[2], 0)
        birthday_dates[string[2]] += 1

    count_of_day = {}
    for key, value in birthday_dates.items():
        count_of_day[value] = count_of_day.get(value, [])
        count_of_day[value].append(key)
        count_of_day[value] = sorted(count_of_day[value], key=lambda x: datetime.strptime(x, pattern))
    
    result = count_of_day[max(count_of_day)]

    return result


print(*massive_date(int(input())), sep='\n')