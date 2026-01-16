import calendar


def fourth_thursday(year, month):
    year, month = int(year), int(month)
    cal = calendar.monthcalendar(year, month)
    week = 3

    if calendar.monthrange(year, month)[0] > 3:
        week += 1
    if month < 10:
        month = f"0{month}"
    return f"{cal[week][3]}.{month}.{year}"


print(fourth_thursday(2012, 3))
print(fourth_thursday(input(), input()))
