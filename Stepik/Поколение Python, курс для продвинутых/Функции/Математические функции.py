from math import sin, sqrt
def f_num_word(num, f):
    func_dict = {'квадрат': lambda x: x**2,
                 'куб': lambda x: x**3,
                 'корень': lambda x: sqrt(x),
                 'модуль': lambda x: abs(x),
                 'синус': lambda x: sin(x)}
    return func_dict[f](num)
num, f = int(input()), input()
print(f_num_word(num, f))