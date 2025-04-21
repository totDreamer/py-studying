import sys

news = [line.rstrip().split(' / ') for line in sys.stdin]
key, news = *news[-1], news[:-1]
news = sorted([v for v in news if v[1]==key], key=lambda x: (float(x[2]), x[0]))

for line in news:
    print(line[0])