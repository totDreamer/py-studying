with open('lines.txt', 'r', encoding='UTF') as f:
    lines = list(map(lambda x: x.rstrip(), f.readlines()))
    max_length = len(max(lines, key=len))
    final_list = [string for string in lines if len(string) == max_length ]
    print(*final_list, sep='\n')