def parse_ranges(ranges: str):
    for r in ranges.split(','):
        start, end = map(int, r.split('-'))
        yield from range(start, end + 1)

print(*parse_ranges('1-2,4-4,8-10'))
print(*parse_ranges('1-10,2-10'))