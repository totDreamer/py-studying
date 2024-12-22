def translyuter():
    translit = {
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e',
    'ё': 'jo', 'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'j', 'к': 'k',
    'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
    'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c',
    'ч': 'ch', 'ш': 'sh', 'щ': 'shh', 'ъ': '*', 'ы': 'y', 'ь': '\'',
    'э': 'je', 'ю': 'ju', 'я': 'ya',
    
    'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E',
    'Ё': 'Jo', 'Ж': 'Zh', 'З': 'Z', 'И': 'I', 'Й': 'J', 'К': 'K',
    'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R',
    'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'H', 'Ц': 'C',
    'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shh', 'Ъ': '*', 'Ы': 'y', 'Ь': '\'',
    'Э': 'Je', 'Ю': 'Ju', 'Я': 'Ya'
    }
    with open('D:/Python-Studying/Stepik/Поколение Python, курс для продвинутых/Работа с файлами/Экзамен/cyrillic.txt', 'r', encoding='utf-8') as f,\
    open('D:/Python-Studying/Stepik/Поколение Python, курс для продвинутых/Работа с файлами/Экзамен/transliteration.txt', 'w', encoding='utf-8') as f2:
        for line in f:
            for letter in line:
                if letter in translit:
                    f2.write(translit[letter])
                else:
                    f2.write(letter)

translyuter()