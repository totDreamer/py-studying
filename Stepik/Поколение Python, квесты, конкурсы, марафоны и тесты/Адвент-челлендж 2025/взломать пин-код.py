from itertools import product

combs = {
    '0': ('0', '8'), '1': ('1', '2', '4'), '2': ('1', '2', '3', '5'), '3': ('2', '3', '6'), '4': ('1', '4', '5', '7'), '5': ('2', '4', '5', '6', '8'), 
    '6': ('3', '5', '6', '9'), '7': ('4', '7', '8'), '8': ('0', '5', '7', '8', '9'), '9': ('6', '8', '9')
        }

def crack_pincode(pincode):
    variables = [combs[dig] for dig in pincode]
    result = list(''.join(num) for num in product(*variables))
    return result

print(crack_pincode('0'))
print(crack_pincode('2'))
print(crack_pincode('46'))
print(crack_pincode('007'))
print(crack_pincode('80'))
print(crack_pincode('111'))