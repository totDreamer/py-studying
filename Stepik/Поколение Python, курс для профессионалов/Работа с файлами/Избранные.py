from zipfile import ZipFile
from datetime import datetime
import os

z_path = 'D:/Python-Studying/Stepik/Поколение Python, курс для профессионалов/Работа с файлами/workbook.zip'
cutoff = datetime(2021, 11, 30, 14, 22, 0)
filenames = []

with ZipFile(z_path) as z_file:
    for f in z_file.infolist():
        if not f.is_dir() and datetime(*f.date_time) > cutoff:
            base_name = os.path.basename(f.filename)
            if base_name:
                filenames.append(base_name)

for name in sorted(filenames):
    print(name)