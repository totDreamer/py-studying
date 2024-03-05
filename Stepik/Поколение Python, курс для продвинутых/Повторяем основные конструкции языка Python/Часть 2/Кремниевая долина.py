def is_infection(*,  key_word : str):
    final_list = []
    count = int(input())
    for i in range(1, count+1):
        word = list(input())
        count_of_true = 0
        for letter in key_word:
            if letter in word:
                count_of_true += 1
                word = word[word.index(letter):]
        if count_of_true == len(key_word):
            final_list.append(str(i))
        count_of_true = 0
    return " ".join(final_list)


print(is_infection(key_word = "anton"))