def verification(login, password, success, failure):
    def you_shoudnt_pass(password):
        has_alpha = False
        has_upper = False
        has_lower = False
        has_digit = False

        for char in password:
            if 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122:
                has_alpha = True
                if char.isupper():
                    has_upper = True
                if char.islower():
                    has_lower = True
            if char.isdigit():
                has_digit = True

            
            if has_alpha and has_upper and has_lower and has_digit:
                break

        if not has_alpha:
            return 'Error 0'
        if not has_upper:
            return 'Error 1'
        if not has_lower:
            return 'Error 2'
        if not has_digit:
            return 'Error 3'
        return True

    wrong_pass = {
        'Error 0': 'в пароле нет ни одной буквы',
        'Error 1': 'в пароле нет ни одной заглавной буквы',
        'Error 2': 'в пароле нет ни одной строчной буквы',
        'Error 3': 'в пароле нет ни одной цифры',
    }

    result = you_shoudnt_pass(password)
    if result is True:
        return success(login)
    else:
        return failure(login, wrong_pass[result])



def success(login):
    print(f'Привет, {login}!')

def failure(login, text):
    print(f'{login}, попробуйте снова. Ошибка: {text}')

verification('timyrik20', 'Beegeek314', success, failure)



def success(login):
    print(f'Здравствуйте, {login}!')

def failure(login, text):
    print(f'{login}, попробуйте снова. Текст ошибки: {text}')

verification('Ruslan_Chaniev', 'stepikstepik2', success, failure)


def success(login):
    print(f'Здравствуйте, {login}!')


def failure(login, text):
    print(f'{login}, попробуйте снова. Текст ошибки: {text}')


verification('Arthur_Davletov', 'мойпарольBEE123', success, failure)