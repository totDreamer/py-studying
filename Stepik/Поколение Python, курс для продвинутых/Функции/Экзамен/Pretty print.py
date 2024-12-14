def pretty_print(data, side='-', delimiter='|'):
    list_string = f'{delimiter} ' + f' {delimiter} '.join(map(str, data)) + f' {delimiter}'
    print(f' {side*(len(list_string)-2)} \n{list_string}\n {side*(len(list_string)-2)} ')
pretty_print([1, 2, 10, 23, 123, 3000])
pretty_print(['abc', 'def', 'ghi', '12345'])
pretty_print(['abc', 'def', 'ghi'], side='*')
pretty_print(['abc', 'def', 'ghi'], delimiter='#')
pretty_print(['abc', 'def', 'ghi'], side='*', delimiter='#')