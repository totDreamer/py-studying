def same_words(word):
    another_words = [input() for _ in range(int(input()))]

    reversed_w = convert_to_keys(word)
    reversed_a_w = [convert_to_keys(word) for word in another_words]

    same = [another_words[i] for i in range(len(another_words)) if reversed_a_w[i] == reversed_w]

    return same

def convert_to_keys(word):
    vow_con = {
        'v': ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е'],
        'c': ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']       
               }
    
    convert_word = ''.join([key for i in word for key, values in vow_con.items() if i in values])
    index = convert_word.rfind('v') + 1
    return convert_word[:index]

print(*same_words(input()), sep='\n')