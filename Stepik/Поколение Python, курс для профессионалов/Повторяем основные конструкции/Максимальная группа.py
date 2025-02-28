def max_group(n):
    dig_sum_dict = {}
    nums = [str(i) for i in range(1, n+1)]
    for num in nums:
        dig_sum = sum(map(int, list(num)))
        dig_sum_dict[dig_sum] = dig_sum_dict.get(dig_sum, [])
        dig_sum_dict[dig_sum].append(num)
    return len(max(dig_sum_dict.values(), key=len))

print(max_group(13))
print(max_group(20))
#print(list('13'))