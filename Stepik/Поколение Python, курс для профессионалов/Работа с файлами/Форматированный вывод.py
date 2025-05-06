from zipfile import ZipFile
from datetime import datetime
import os

z_path = 'D:/Python-Studying/Stepik/Поколение Python, курс для профессионалов/Работа с файлами/workbook.zip'
files = []

with ZipFile(z_path) as z_file:
    for f in z_file.infolist():
        if not f.is_dir():
            files.append({
                'name': os.path.basename(f.filename),
                'date': f.date_time,
                'size_b': f.file_size,
                'size_a': f.compress_size
            })

for f in sorted(files, key=lambda x: x['name']):
    date_str = datetime(*f['date']).strftime('%Y-%m-%d %H:%M:%S')
    print(f['name'])
    print(f'  Дата модификации файла: {date_str}')
    print(f'  Объем исходного файла: {f["size_b"]} байт(а)')
    print(f'  Объем сжатого файла: {f["size_a"]} байт(а)')
    print()