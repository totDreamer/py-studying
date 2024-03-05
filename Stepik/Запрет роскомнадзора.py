def rkm_block(*, word : str):
    list_word = list(word + " запретил букву ")
    sym_in_word = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
    for i in range(0, len(sym_in_word)):
        if sym_in_word[i] in list_word:
            while list_word[0] == " ":
                list_word = list_word[1:]
            for _ in range(len(list_word)):
                list_word = "".join(list_word).replace("  ", " ")
                list_word = "".join(list_word).replace("   ", " ")
                list_word = list(list_word)
            print("".join(list_word) + sym_in_word[i])
            while sym_in_word[i] in list_word:
                list_word.pop(list_word.index(sym_in_word[i]))

rkm_block(word = input())