def horse_step(*, start_dot : str):
    map = [["." for _ in range(8)] for _ in range(8)]
    x = ["a", "b", "c", "d", "e", "f", "g", "h"]
    y = [str(i) for i in range(8, 0, -1)]
    x_in = x.index(start_dot[0])
    y_in = y.index(start_dot[1])
    map[y_in][x_in] = "N"
    for i in range(len(map)):
        for j in range(len(map[i])):
            if (x_in - j) * (y_in - i) == 2 or (x_in - j) * (y_in - i) == -2:
                map[i][j] = "*"
    return map

final_map = horse_step(start_dot = input())
for row in final_map:
    print(*row)