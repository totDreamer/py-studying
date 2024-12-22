def longest_word(file):
    with open(file, 'r', encoding='utf-8') as f:
        data = f.read().split()
        count_of_len = {}
        for word in data:
            count_of_len[len(word)] = count_of_len.get(len(word), '') + f'{word}\n'
        return count_of_len[max(count_of_len.keys())]
    
print(longest_word('D:/Python-Studying/Stepik/Поколение Python, курс для продвинутых/Работа с файлами/Экзамен/words.txt'))