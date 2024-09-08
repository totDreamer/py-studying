first_set, second_set, third_set = set(input().split()), set(input().split()), set(input().split())
final_result = (first_set | second_set | third_set) - (first_set & second_set & third_set)
print(*sorted(final_result, key= int))