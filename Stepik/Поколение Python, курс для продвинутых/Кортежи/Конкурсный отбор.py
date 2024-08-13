students = [tuple(input().split()) for _ in range(int(input()))]

for student in students:
    print(*student)

print()

for name, grade in students:
    if int(grade) > 3:
        print(name, grade)