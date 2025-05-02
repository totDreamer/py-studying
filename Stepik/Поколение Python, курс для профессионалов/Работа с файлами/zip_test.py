from zipfile import ZipFile

zip_path = 'D:/Python-Studying/Stepik/Поколение Python, курс для профессионалов/Работа с файлами/test.zip'
with ZipFile(zip_path) as zip_file:
    zip_file.printdir()
    info = zip_file.infolist()
    print()

    print(info[2].file_size)
    print(info[2].compress_size)            # размер сжатого файла в байтах
    print(info[2].filename)                 # имя файла
    print(info[2].date_time)
    print(info[0].is_dir())
    print(info[6].is_dir())
    print()

    names = zip_file.namelist()
    print(names)
    print(*names, sep='\n')
    print()

    last_file = zip_file.getinfo(names[-4])
    print(last_file.file_size)
    print(last_file.compress_size)
    print(last_file.filename)
    print(last_file.date_time)
    print()

    with zip_file.open('test/Разные файлы/astros.json') as file:
        print(file.read().decode('UTF-8'))

with ZipFile(zip_path, mode='a') as zip_file_w:
    w_path_1 = 'D:/Python-Studying/Stepik/Поколение Python, курс для профессионалов/Работа с файлами/Wi-Fi Москвы.py'
    w_path_2 = 'D:/Python-Studying/Stepik/Поколение Python, курс для профессионалов/Работа с файлами/wifi.csv'
    zip_file_w.write(w_path_1, 'test/wifi.py')
    zip_file_w.write(w_path_2)
    print(zip_file_w.namelist())