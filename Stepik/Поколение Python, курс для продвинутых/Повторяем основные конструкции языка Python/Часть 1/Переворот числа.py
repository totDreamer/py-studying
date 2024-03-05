def reverse(*, num : str):
    if len(num) == 5:
        return int(num[::-1])
    else:
        return int(num[0]+num[-1:-6:-1])


n = str(input())
print(reverse(num = n))