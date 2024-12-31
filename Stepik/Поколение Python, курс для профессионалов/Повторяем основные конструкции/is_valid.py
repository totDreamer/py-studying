def is_valid(password):
    return 4 <= len(password) <= 6 and password.isdigit()
        
    

print(is_valid('1234'))
print(is_valid('4367'))
print(is_valid('89abc1'))
print(is_valid('89  1'))