def reading_names(names):
    try:
        with open(names) as f:
            names_list = f.readlines()

    except FileNotFoundError:
        pass

    else:
        for name in names_list:
            print(name)


catdog = ["D:/Python-Studying/txt_files/cats.txt", "D:/Python-Studying/txt_files/dogs.txt"]

for file in catdog:
    reading_names(file)