def total_sum_in_stage(file, stage='a'):
    with open(file, 'r', encoding='UTF-8') as f:
        file_lines = (line for line in f)
        line_values = (line.rstrip().split(',') for line in file_lines)
        titles = next(line_values)
        line_dicts = (dict(zip(titles, data)) for data in line_values)
        result = sum(int(line['raisedAmt']) for line in line_dicts if line['round'] == stage)
        return result

print(total_sum_in_stage('/home/user/study/py-studying/Stepik/Поколение Python, курс для профессионалов/Итераторы, генераторы/data.csv'))