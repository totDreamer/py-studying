import csv

input_path = '/home/user/py-studying/Stepik/Поколение Python, курс для профессионалов/Работа с файлами/student_counts.csv'
output_path = '/home/user/py-studying/Stepik/Поколение Python, курс для профессионалов/Работа с файлами/sorted_student_counts.csv'
def sort_key(class_name):
    num, letter = class_name.split('-')
    return (int(num), letter)

with open(input_path, 'r', encoding='UTF-8', newline='') as f, \
    open(output_path, 'w', encoding='UTF-8', newline='') as f2:
    data = csv.DictReader(f)
    f_names = data.fieldnames

    sorted_f = ['year'] + sorted([n for n in f_names if n!='year'], key=sort_key)

    writer = csv.DictWriter(f2, fieldnames=sorted_f)
    writer.writeheader()
    writer.writerows(data)

    