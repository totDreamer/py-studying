def rec_sum(num):
    if not num:
        return 0
    return int(num[0]) + int(rec_sum(num[1:]))

print(rec_sum(input()))
print(rec_sum('45'))
print(rec_sum('12345'))