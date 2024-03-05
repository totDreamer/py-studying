def one_survived(*, people_count : int, kill: int):
    people_list = list(range(1, people_count+1))
    while len(people_list) > 1:
        for k in range(1, kill):
            first_blood = people_list.pop(0)
            people_list.append(first_blood)
        people_list.pop(0)
    return people_list[0]


n, k = int(input()), int(input())
print(one_survived(people_count = n, kill = k))