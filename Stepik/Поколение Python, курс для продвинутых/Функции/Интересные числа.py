def interesting_num(a, b):
    list_in_range = [str(i) for i in range(int(a), int(b)+1)]
    result_list = [j for j in list_in_range if all(map(lambda x: int(j) % int(x) == 0 if x != '0' else None, [x for x in j]))]
    return result_list

print(*interesting_num(1, 25))
print(*interesting_num(20, 30))
print(*interesting_num(50, 150))
print(*interesting_num(24, 36))
print(*interesting_num(input(), input()))