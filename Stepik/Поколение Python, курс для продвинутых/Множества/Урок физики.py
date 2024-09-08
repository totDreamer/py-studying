first_set, second_set, third_set = set(input().split()), set(input().split()), set(input().split())
final_result = third_set.difference(first_set | second_set)
print(*sorted(final_result, key= int, reverse= True))