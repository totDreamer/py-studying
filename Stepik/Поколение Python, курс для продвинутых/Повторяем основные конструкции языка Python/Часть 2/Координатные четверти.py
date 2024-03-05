area_1 = 0
area_2 = 0
area_3 = 0
area_4 = 0
str_count = int(input())
for j in range(str_count):
    coordinates = input().split()
    if int(coordinates[0]) > 0 and int(coordinates[1]) > 0:
        area_1 += 1
    elif int(coordinates[0]) < 0 and int(coordinates[1]) > 0:
        area_2 += 1
    elif int(coordinates[0]) < 0 and int(coordinates[1]) < 0:
        area_3 += 1
    elif int(coordinates[0]) > 0 and int(coordinates[1]) < 0:
        area_4 += 1
print(f'Первая четверть: {area_1}', f'Вторая четверть: {area_2}', f'Третья четверть: {area_3}', f'Четвертая четверть: {area_4}', sep = "\n")