from re import findall

def abbreviate(phrase):
    return ''.join(map(str.upper, findall(r'\b[A-Z]+\b|\b\w|\B[A-Z]\B', phrase)))

print(abbreviate('javaScript object notation'))
print(abbreviate('frequently asked questions'))
print(abbreviate('JS game sec'))