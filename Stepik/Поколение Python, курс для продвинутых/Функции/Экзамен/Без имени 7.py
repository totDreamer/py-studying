from operator import *

def arithmetic_operation(sym):
    kw = {'+': add,
          '-': sub,
          '*': mul,
          '/': truediv}
    return kw[sym]

add = arithmetic_operation('+')
div = arithmetic_operation('/')
print(add(10, 20))
print(div(20, 5))