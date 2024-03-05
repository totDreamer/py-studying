def pascal(*, num : int):
    triangle_pascal = [[1]]
    for i in range(2, num + 2):
        triangle_pascal.append([1] * i)
    for j in range(len(triangle_pascal)):
        for k in range(1, len(triangle_pascal[j])-1):
            triangle_pascal[j][k] = triangle_pascal[j-1][k-1] + triangle_pascal[j-1][k]
    return triangle_pascal[:num]


final_string = pascal(num = int(input()))
for i in range(len(final_string)):
    for j in range(len(final_string[i])):
        print(str(final_string[i][j]), end = " ")
    print()