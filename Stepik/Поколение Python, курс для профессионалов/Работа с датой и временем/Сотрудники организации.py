from datetime import datetime

def who_is_older(number_of_people):
    birthday_dates = {}
    pattern = '%d.%m.%Y'

    for _ in range(number_of_people):
        string = input().split()
        birthday_dates[string[2]] = birthday_dates.get(string[2], [])
        birthday_dates[string[2]].append(' '.join(string[:2]))

    birthday_dates = dict(sorted(birthday_dates.items(), key= lambda x: datetime.strptime(x[0], pattern)))
    oldest = None

    for d, n in birthday_dates.items():
        if len(n) > 1:
            oldest = f'{d} {len(n)}'
        else:
            oldest = f'{d} {n[0]}'
        break
    
    return oldest


print(who_is_older(int(input())))