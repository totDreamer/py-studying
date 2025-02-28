def more_then_one(values):
    values_count = {}
    final_result = []

    for n in values:
        values_count[n] = values_count.get(n, 0) + 1

    for key, value in values_count.items():
        if value > 1:
            final_result.append(key)

    return final_result

values = sorted(list(map(int, input().split())))
print(*more_then_one(values))