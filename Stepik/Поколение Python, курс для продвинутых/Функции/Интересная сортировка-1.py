nums = [int(i) for i in input().split()]

def comparator(n):
    return sum(int(i) for i in str(n))

print(*sorted(nums, key=comparator))
