class PasswordError(Exception):
    pass

class LengthError(PasswordError):
    pass

class LetterError(PasswordError):
    pass

class DigitError(PasswordError):
    pass

def is_good_password(string):
    if len(string) < 9:
        raise LengthError
    if not any(char.isalpha() for char in string) or not all([any(char.islower() for char in string), any(char.isupper() for char in string)]):
        raise LetterError        
    if not any(char.isdigit() for char in string):
        raise DigitError
    else:
        return 'Success!'

while True:
    try:
        print(is_good_password(input()))
        break
    except Exception as err:
        print(err.__class__.__name__)
    
