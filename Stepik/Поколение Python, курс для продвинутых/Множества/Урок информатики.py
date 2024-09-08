first_set, second_set, third_set = set(input().split()), set(input().split()), set(input().split())
final_result = first_set.intersection(second_set) - third_set
print(*sorted(final_result, reverse= True, key= int))