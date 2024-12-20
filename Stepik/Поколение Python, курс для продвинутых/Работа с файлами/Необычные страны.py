with open('population.txt', 'r', encoding='utf') as f:
    lines = [x.rstrip().split('\t') for x in f.readlines()]
    final_list = filter(lambda x: x[0][0].lower() == 'g' and int(x[-1]) > 500000, lines)
    for name, count in final_list:
        print(name)