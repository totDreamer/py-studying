from datetime import datetime, timedelta

def most_younger(day):
    pattern = '%d.%m.%Y'
    base_day = datetime.strptime(day, pattern)
    near_dates = [((base_day + timedelta(days=i)).day, (base_day + timedelta(days=i)).month) for i in range(8) if i!=0]

    people = {}
    for _ in range(int(input())):
        *name, d = input().split()
        birth_date = datetime.strptime(d, pattern)
        people[birth_date] = ' '.join(name)

    result = {}
    for d, name in people.items():
        try:
            if (d.day, d.month) in near_dates:
                result[d] = name
        except ValueError:
            continue

    if result:
        return result[max(result)]
    else:
        return 'Дни рождения не планируются'

print(most_younger(input()))