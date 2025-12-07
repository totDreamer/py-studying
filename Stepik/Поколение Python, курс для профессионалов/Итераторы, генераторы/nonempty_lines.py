def nonempty_lines(file):
    with open(file, 'r', encoding='UTF-8') as f:
        file_lines = (line.rstrip() for line in f if line.strip())
        dots_fill = (line if len(line) <= 25 else '...' for line in file_lines)
        yield from dots_fill

lines = nonempty_lines('/home/user/study/py-studying/Stepik/Поколение Python, курс для профессионалов/Итераторы, генераторы/data.csv')
print(next(lines))
print(next(lines))
print(next(lines))
print(next(lines))