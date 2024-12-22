def complete_exam_students(file):
    with open(file, 'r', encoding='utf') as f:
        data = [line.split() for line in f.readlines()]
        results = [True if int(n[1])>=65 and int(n[2])>=65 and int(n[3])>=65 else False for n in data]
        return sum(results)

print(complete_exam_students('D:/Python-Studying/Stepik/Поколение Python, курс для продвинутых/Работа с файлами/Экзамен/grades.txt'))
        