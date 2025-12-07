def txt_to_dict():
    with open('/home/user/study/py-studying/Stepik/Поколение Python, курс для профессионалов/Итераторы, генераторы/planets.txt', 'r', encoding='UTF-8') as f:
        lines = (line.strip().split(' = ') for line in f)
        pl_predict = []

        for line in lines:
            if line == ['']:
                yield {key: value for key, value in pl_predict}
                pl_predict = []
                continue

            pl_predict.append(line)
        
        yield {key: value for key, value in pl_predict}

planets = txt_to_dict()
for _ in range(9):
    print(next(planets))