words = input()
alert_sym = ['.', ',', ';', ':', '!', '-', '?']
new_words = ''
for sym in words:
    if sym not in alert_sym:
        new_words += sym.lower()
print(len(set(new_words.split())))