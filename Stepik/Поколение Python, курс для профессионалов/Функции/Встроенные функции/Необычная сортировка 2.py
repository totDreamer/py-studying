def uncommon_sorting(string):
    return ''.join(sorted(string, key=lambda x: (x in '24680', x.isdigit(), x.isupper(), x)))

print(uncommon_sorting(input()))