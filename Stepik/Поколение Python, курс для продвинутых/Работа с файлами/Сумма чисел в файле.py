with open('nums.txt', 'r', encoding='UTF') as f:
    one_string = f.read()
    for char in one_string:
        if not char.isdigit():
            one_string = one_string.replace(char, ' ')
    print(sum(map(int, one_string.split())))