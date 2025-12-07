from itertools import groupby

def group_anagrams(words):
    sorted_words = groupby(sorted(words, key=lambda x: sorted(x)), key=lambda x: sorted(x))
    final_list = []
    for _, data in sorted_words:
        final_list.append((*data,))
    
    return final_list

groups = group_anagrams(['evil', 'father', 'live', 'levi', 'book', 'afther', 'boko'])
print(*groups)

groups = group_anagrams(['evil', 'father', 'book', 'stepik', 'beegeek'])
print(*groups)

groups = group_anagrams(['крона', 'сеточка', 'тесачок', 'лучик', 'стоечка', 'норка', 'чулки'])
print(*groups)