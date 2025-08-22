def is_good_password(string):
    if any(char.isdigit() for char in string) and len(string) >= 9 and any(char.islower() for char in string) and any(char.isupper() for char in string):
        return True
    else:
        return False

print(is_good_password('41157082'))
print(is_good_password('мойпарольсамыйлучший'))
print(is_good_password('МойПарольСамыйЛучший111'))