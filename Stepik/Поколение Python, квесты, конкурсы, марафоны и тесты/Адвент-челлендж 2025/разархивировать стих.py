words_dict = {
    '1': 'A',
    '2': 'ALOUD',
    '3': 'ALWAYS',
    '4': 'BE',
    '5': 'BLUE',
    '6': 'CLOUD',
    '7': 'EVERY',
    '8': 'FLOATING',
    '9': 'HIM',
    '10': 'HOW',
    '11': 'IN',
    '12': 'IT',
    '13': 'LITTLE',
    '14': 'MAKES',
    '15': 'PROUD',
    '16': 'SINGS',
    '17': 'SWEET',
    '18': 'THE',
    '19': 'TO',
    '20': 'VERY',
    '21': '19 4 1',
    '22': '13 6',
    '23': '24 25',
    '24': '10 17 21 6',
    '25': '8 11 18 5',
}

pattern = '23 7 22 3 16 2 23 12 14 9 20 15 21 22'.split()
result = []

while pattern:
    key = pattern.pop(0)
    value = words_dict[key]
    
    if value.isalpha():
        result.append(value)
    else:
        new_keys = value.split()
        pattern = new_keys + pattern

print(*result)