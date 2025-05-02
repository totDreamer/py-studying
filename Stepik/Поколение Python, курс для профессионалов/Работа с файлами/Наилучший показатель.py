from zipfile import ZipFile
import os

z_path = 'D:/Python-Studying/Stepik/Поколение Python, курс для профессионалов/Работа с файлами/workbook.zip'
with ZipFile(z_path) as z_file:
    best_compress, bc_size = None, 100 
    for f in z_file.infolist():
        if not f.is_dir() and (f.compress_size/f.file_size)<bc_size:
            best_compress = f.filename
            bc_size = f.compress_size/f.file_size
    print(os.path.basename(best_compress))
    print(bc_size)