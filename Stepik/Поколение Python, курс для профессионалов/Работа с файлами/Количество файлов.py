from zipfile import ZipFile

z_path = 'D:/Python-Studying/Stepik/Поколение Python, курс для профессионалов/Работа с файлами/workbook.zip'
with ZipFile(z_path) as z_file:
    count_of_files = 0
    for f in z_file.infolist():
        if not f.is_dir():
            count_of_files += 1

    print(count_of_files)