def convert(string):
    lower_count = 0
    upper_count = 0
    for char in string:
        if char.islower():
            lower_count += 1
        elif char.isupper():
            upper_count += 1
    return string.upper() if upper_count > lower_count else string.lower()

print(convert('BEEgeek'))
print(convert('pyTHON'))
print(convert('pi31415!'))