default_set = set(range(0,11))
first_student, second_student, third_student = set(map(int, input().split())), set(map(int, input().split())), set(map(int, input().split()))
print(*default_set.difference(first_student, second_student, third_student))