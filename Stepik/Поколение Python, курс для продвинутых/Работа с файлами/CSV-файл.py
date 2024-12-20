def read_csv(file_name):
    with open(file_name, 'r', encoding='utf')as f:
        keys = f.readline().strip().split(',')
        values = list(map(lambda x: x.rstrip().split(','), f.readlines()))
        final_resut = []
        for line in values:
            final_resut.append(dict(zip(keys, line)))
        return final_resut



