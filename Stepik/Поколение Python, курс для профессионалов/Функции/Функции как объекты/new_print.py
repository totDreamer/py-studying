old_print = print

def print(*args, sep=' ', end='\n'):
    def convert_arg(arg):
        if isinstance(arg, str):
            return arg.upper()
        elif isinstance(arg, (list, dict)):
            return arg
        else:
            return arg
    
    converted_args = [convert_arg(arg) for arg in args]
    

    old_print(*converted_args, sep=sep.upper(), end=end.upper())

print('beegeek', [1, 2, 3], 4)
print('bee', 'geek', sep=' and ', end=' wow')
words = ('black', 'white', 'grey', 'black-1', 'white-1', 'python')
print(*words, sep=' to ', end=' LOVE')