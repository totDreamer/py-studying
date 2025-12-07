def filter_names(names, ignore_char, max_names):
    correct_names = (name for name in names if name[0].lower() != ignore_char.lower() and name.isalpha())
    limited = (name for i, name in enumerate(correct_names) if i < max_names)
    yield from limited


data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']
print(*filter_names(data, 'D', 3))