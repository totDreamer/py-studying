list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
maximum = 0
for l in list1:
    for num in l:
        if num > maximum:
            maximum = num


print(maximum)