def nums_reverse(n, x, y, a, b):
    nums_list = [i for i in range(1, n+1)]    
    nums_list[x-1:y] = nums_list[x-1:y][::-1]
    nums_list[a-1:b] = nums_list[a-1:b][::-1]
    return nums_list

n, x, y, a, b = map(int, input().split())
print(*nums_reverse(n, x, y, a, b))