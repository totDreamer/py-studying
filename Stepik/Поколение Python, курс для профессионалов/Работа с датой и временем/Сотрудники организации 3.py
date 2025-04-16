from datetime import datetime, timedelta

def most_younger(day):
    pattern = '%d.%m.%Y'
    base_day = datetime.strptime(day, pattern)

    people = {}
    for _ in range(int(input())):
        *name, d = input().split()
        birth_date = datetime.strptime(d, pattern)
        people[birth_date] = ' '.join(name)

    f1, f2 = base_day - timedelta(days=7), base_day + timedelta(days=7)
    result = {}

    for d, name in people.items():
        try:
            same_year_date = d.replace(year=base_day.year)
            if f1 <= same_year_date <= f2 and same_year_date.day != base_day.day:
                result[d] = name
        except ValueError:
            continue

    if result:
        return result, result[max(result)]
    else:
        return 'Дни рождения не планируются'

print(most_younger(input()))