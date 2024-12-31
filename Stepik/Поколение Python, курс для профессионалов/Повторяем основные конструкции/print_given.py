def print_given(*args, **kwargs):
    kwargs_list = sorted([f'{key} {value} {type(value)}' for key, value in kwargs.items()])
    for arg in args:
        print(f'{arg} {type(arg)}')
    for kwarg in kwargs_list:
        print(kwarg)

print_given(1, [1, 2, 3], 'three', two=2)
print_given(b=2, d=4, c=3, a=1)
print_given()