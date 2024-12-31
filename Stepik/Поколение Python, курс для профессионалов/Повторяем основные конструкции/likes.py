def likes(list_of_names):
    if len(list_of_names) == 0:
        return 'Никто не оценил данную запись'
    elif len(list_of_names) == 1:
        return f'{list_of_names[0]} оценил(а) данную запись'
    elif len(list_of_names) == 2:
        return f'{list_of_names[0]} и {list_of_names[1]} оценили данную запись'
    elif len(list_of_names) == 3:
        return f'{list_of_names[0]}, {list_of_names[1]} и {list_of_names[2]} оценили данную запись'
    else:
        return f'{list_of_names[0]}, {list_of_names[1]} и {len(list_of_names) - 2} других оценили данную запись'
    
print(likes(['Дима', 'Алиса']))
print(likes(['Эндрю', 'Тоби', 'Том']))
print(likes([]))