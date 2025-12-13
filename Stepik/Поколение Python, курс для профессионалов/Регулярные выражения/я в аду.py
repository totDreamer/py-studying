def watta_hell(phrase):
    data = iter(phrase.replace(',', ' ').replace('.', ' ').split())

    def f_test(word):

        if word.startswith(('7', '8', '+7')):
            try:
                    if word.startswith('+7'):
                        word = word[1:]

                    digits = word.split('-')

                    if word.startswith('7'):
                        if len(digits) == 5:
                            if all(99 < int(num) < 1000 for num in digits[1:3]) and all(9 < int(num) < 100 for num in digits[3:]):
                                yield word

                    if word.startswith('8'):
                        if len(digits) == 4:
                            if 99 < int(digits[1]) < 1000 and all(999 < int(num) < 10000 for num in digits[2:]):
                                yield word

            except:
                pass
        

    final_result = (w for word in data for w in f_test(word))
    return final_result

print(*watta_hell(input()), sep='\n')