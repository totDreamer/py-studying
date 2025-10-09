def exception_decorator(f):
    def wrapper(*args, **kwargs):
        try:
            result = f(*args, **kwargs)
            return (result, 'Функция выполнилась без ошибок')
        except:
            return (None, 'При вызове функции произошла ошибка')
    
    return wrapper

@exception_decorator
def f(x):
    return x**2 + 2*x + 1
    
print(f(7))

sum = exception_decorator(sum)

print(sum(['199', '1', 187]))