from functools import wraps

def make_html(tag):
    def make_html_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            return f'<{tag}>' + f(*args, **kwargs) + f'</{tag}>'
        return wrapper
    return make_html_decorator

@make_html('del')
def get_text(text):
    return text
    
print(get_text('Python'))

@make_html('i')
@make_html('del')
def get_text(text):
    return text
    
print(get_text(text='decorators are so cool!'))