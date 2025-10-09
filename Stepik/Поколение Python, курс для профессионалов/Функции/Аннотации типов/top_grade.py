def top_grade(grades: dict[str, str | list[int]]) -> dict[str, str | int]:
    grades['top_grade'] = max(grades['grades'])
    del grades['grades']
    return grades

info = {'name': 'Timur', 'grades': [30, 57, 99]}

print(top_grade(info))

print(top_grade({'name': 'Ruslan', 'grades': [19, 48, 86, 45, 32]}))