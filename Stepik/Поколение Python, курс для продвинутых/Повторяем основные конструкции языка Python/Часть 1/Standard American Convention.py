def sac(*, number : str):
    final = list(number)
    for j in range(-1, -len(number), -1):
        if j % 3 == 0:
            final[j] = ',' + final[j]
    return ''.join(final)

n = input()
print(sac(number = n))