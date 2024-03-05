def multiply_tab(*, n : int, m : int):
    mult = [[0 for i in range(m)] for i in range(n)]
    for i in range(len(mult)):
        for j in range(len(mult[i])):
            mult[i][j] = str(i*j)
    return mult


result = multiply_tab(n = int(input()), m = int(input()))
for i in range(len(result)):
    for j in range(len(result[i])):
        print(result[i][j].ljust(3, " "), end = "")
    print()