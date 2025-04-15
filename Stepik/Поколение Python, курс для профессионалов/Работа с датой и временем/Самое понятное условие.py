from datetime import datetime, timedelta

def wtf(start, end):
    result = []
    pattern = '%d.%m.%Y'
    start = datetime.strptime(start, pattern)
    end = datetime.strptime(end, pattern)

    while True:
        if (start.day + start.month)%2 != 0:
            break
        else:
            start = start + timedelta(days=1)

    while start <= end:
        if start.weekday() != 0 and start.weekday() != 3:
            result.append(start.strftime(pattern))
        start = start + timedelta(days=3)
    
    return result

print(*wtf(input(), input()), sep='\n')