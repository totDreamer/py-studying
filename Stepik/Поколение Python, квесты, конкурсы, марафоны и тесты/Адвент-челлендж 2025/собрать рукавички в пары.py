def split(data):
    final_result = []
    counter = 0
    semi_res = ''

    for d in data:
        semi_res += d
        if d in ('(', '['):
            counter += 1
        elif d in (')', ']'):
            counter -= 1
        if  counter == 0:
            final_result.append(semi_res)
            semi_res = ''
    
    return final_result


print(split('()()()') == ['()', '()', '()'])
print(split('((()))') == ['((()))'])
print(split('((()))(())()()(()())') == ['((()))', '(())', '()', '()', '(()())'])
print(split('([[]])()[][()]') == ['([[]])', '()', '[]', '[()]'])
print(split('[][][][]()()') == ['[]', '[]', '[]', '[]', '()', '()'])
print(split('[][[][[]()([(())])]]') == ['[]', '[[][[]()([(())])]]'])