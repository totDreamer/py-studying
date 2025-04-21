import sys

nums = [int(n) for n in sys.stdin]
answer = ['Арифметическая прогрессия', 'Геометрическая прогрессия', 'Не прогрессия']
d = nums[1] - nums[0]
q = nums[1] // nums[0]
if all(nums[i] - nums[i-1] == d for i in range(1, len(nums))):
    print(answer[0])
elif all(nums[i] // nums[i-1] == q for i in range(1, len(nums))):
    print(answer[1])
else:
    print(answer[2])