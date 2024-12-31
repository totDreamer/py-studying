def spell(*args):
    line = [word.lower() for word in args]
    first_char = {}

    for word in line:
        if word[0] not in first_char:
            first_char[word[0]] = len(word)
        else:
            if len(word) > first_char[word[0]]:
                first_char[word[0]] = len(word)    

    return first_char

words = ['Россия', 'Австрия', 'Австралия', 'РумыниЯ', 'Украина', 'КИТай', 'УЗБЕКИСТАН']
print(spell(*words))

print(spell('Математика', 'История', 'химия', 'биология', 'Информатика'))

words = ['fruit', 'football', 'February', 'forest', 'Family']
print(spell(*words))