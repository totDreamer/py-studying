from re import search, IGNORECASE

s = input()
pattern = r'^Здравствуйте|^Доброе утро|^Добрый (день|вечер)'
if search(pattern, s, flags=IGNORECASE):
    print(True)
else:
    print(False)