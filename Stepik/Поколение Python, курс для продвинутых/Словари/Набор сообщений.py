keyboard = {
    '1': ['.', ',', '?', '!', ':'],
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z'],
    '0': [' '],
}
string = input().lower().replace('"', '')
answer = ''
for s in string:
    for key, value in keyboard.items():
        if s in value:
            answer += key * (value.index(s) + 1)
print(answer)