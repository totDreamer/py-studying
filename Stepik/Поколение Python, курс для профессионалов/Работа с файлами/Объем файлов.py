from zipfile import ZipFile

z_path = 'D:/Python-Studying/Stepik/Поколение Python, курс для профессионалов/Работа с файлами/workbook.zip'
with ZipFile(z_path) as z_file:
    diff_weight = {'zip': 0, 'unzip': 0}
    for f in z_file.infolist():
        diff_weight['zip'] += f.compress_size
        diff_weight['unzip'] += f.file_size
    print(f'Объем исходных файлов: {diff_weight['unzip']} байт(а)')
    print(f'Объем сжатых файлов: {diff_weight['zip']} байт(а)')