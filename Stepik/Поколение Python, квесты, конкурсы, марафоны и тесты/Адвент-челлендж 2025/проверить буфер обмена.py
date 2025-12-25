from re import split

def copy_paste(text):
    data = filter(lambda x: x != '', map(str.strip, split(r'(Ctrl \+ [CV])', text)))
    
    semi_res = []
    result = []
    for w in data:
        if w not in ('Ctrl + C', 'Ctrl + V'):
            result.append(w)
        if w == 'Ctrl + C' and result:
            semi_res = result[:]
        if w == 'Ctrl + V' and semi_res:
            result.extend(semi_res)

    return ' '.join(result)

print(copy_paste('jingle bells Ctrl + C Ctrl + C Ctrl + V jingle all the way') == 'jingle bells jingle bells jingle all the way')
print(copy_paste('LET IT SNOW Ctrl + V Ctrl + C Ctrl + V') == 'LET IT SNOW LET IT SNOW')
print(copy_paste('Merry Ctrl + C Ctrl + V Christmas Ctrl + C Ctrl + V') == 'Merry Merry Christmas Merry Merry Christmas')
print(copy_paste('one two Ctrl + C three four Ctrl + C Ctrl + V') == 'one two three four one two three four')
print(copy_paste('beegeek Ctrl + C Ctrl + V Ctrl + C Ctrl + V Ctrl + C Ctrl + V') == 'beegeek beegeek beegeek beegeek beegeek beegeek beegeek beegeek')
print(copy_paste('Happy Ctrl + V New Ctrl + V Year') == 'Happy New Year')
print(copy_paste('Hello Ctrl + C World Ctrl + V') == 'Hello World Hello')
print(copy_paste('Winter Ctrl + C Ctrl + V Ctrl + V Ctrl + V') == 'Winter Winter Winter Winter')