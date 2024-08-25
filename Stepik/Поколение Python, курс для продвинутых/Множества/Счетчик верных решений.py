n = int(input())
if n != 0:
    names_set = set()
    answers_list = []
    all_right_answers_count = 0
    for i in range(n):
        name = input()
        name_len = name.index(':')
        if name[:name_len] not in names_set:
            if name[name_len+2:] == 'Correct':
                names_set.add(name[:name_len])
                answers_list.append(name[name_len + 2:])
                all_right_answers_count += 1
        elif name[:name_len] in names_set:
            if name[name_len+2:] == 'Correct':
                all_right_answers_count += 1

    right_answers = 0
    for answer in answers_list:
        if answer == 'Correct':
            right_answers += 1
    right_percentage = str(int(round((all_right_answers_count / n + 0.005) * 100, 2))) + '%'
    if all_right_answers_count != 0:
        print(f'Верно решили {right_answers} учащихся\nИз всех попыток {right_percentage} верных')
    else:
        print('Вы можете стать первым, кто решит эту задачу')
else:
    print('Вы можете стать первым, кто решит эту задачу')