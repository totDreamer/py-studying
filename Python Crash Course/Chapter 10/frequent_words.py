def count_words(file, word):
    try:
        with open(file, encoding = 'utf-8') as f:
            contents = f.read()

    except FileNotFoundError:
        print(f'File {file} not found')

    else:
        result = contents.lower().count(word)
        print(f'"{word}" appears in {file} {result} times')


file = "D:/Python-Studying/txt_files/Weeds.txt"
file_2 = "D:/Python-Studying/txt_files/Little Jack Rabbit and Danny Fox.txt"
count_words(file, "the")
count_words(file, "the ")
count_words(file_2, "the")
count_words(file_2, "the ")