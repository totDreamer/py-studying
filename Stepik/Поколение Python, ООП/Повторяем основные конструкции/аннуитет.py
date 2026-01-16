def annual_return(start: int, percent: int, years: int):
    percent = (percent + 100) / 100
    results = (start * percent**y for y in range(1, years + 1))
    yield from results


for value in annual_return(120000, 10, 3):
    print(round(value))

for value in annual_return(70000, 8, 10):
    print(round(value))
