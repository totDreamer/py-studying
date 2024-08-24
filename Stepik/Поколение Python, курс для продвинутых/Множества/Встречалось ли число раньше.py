nums = list(map(int, input().split()))
nums_set = set()
for num in nums:
    if num not in nums_set:
        nums_set.add(num)
        print('NO')
    else:
        print('YES')