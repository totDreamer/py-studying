from collections import Counter

data = Counter('aksjaskfjsklfjdslkfjajfopewtoieqpwdpqworiiqjskanvmcxbmpewrqopkqwlmdzczmxvmvlnjpjqpkqzxvmbowiqeorewi')

data.max_values = lambda: [(k, v) for k, v in data.items() if v == max(data.values())]
data.min_values = lambda: [(k, v) for k, v in data.items() if v == min(data.values())]

print(data.max_values())
print(data.min_values())