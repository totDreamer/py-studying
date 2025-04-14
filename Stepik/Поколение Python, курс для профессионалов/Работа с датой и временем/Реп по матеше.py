from datetime import datetime, timedelta

def schedule(start, end):
    pattern = '%H:%M'
    start = datetime.strptime(start, pattern)
    end = datetime.strptime(end, pattern)
    lessons = []

    while True:
        lesson_end = start + timedelta(minutes=45)
        if lesson_end > end:
            break
        lessons.append(f'{start.strftime(pattern)} - {lesson_end.strftime(pattern)}')
        start = lesson_end + timedelta(minutes=10)
    
    return lessons

print(*schedule('10:00', '12:35'), sep='\n')
print(*schedule(input(), input()), sep='\n')