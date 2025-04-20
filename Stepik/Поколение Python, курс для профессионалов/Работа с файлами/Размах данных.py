import arrow, sys

dates = [arrow.get(line.strip()) for line in sys.stdin]
print((max(dates)-min(dates)).days)