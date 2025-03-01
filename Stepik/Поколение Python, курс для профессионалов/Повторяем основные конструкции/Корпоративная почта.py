already_use = [input() for _ in range(int(input()))]
new_names = [input() for _ in range(int(input()))]
already_use = [name[:name.rfind('@')] for name in already_use]

def new_mail(name):
    if name not in already_use:
            already_use.append(name)
            return f'{name}@beegeek.bzz'
    else:
        num = 0
        new_name = name
        while new_name in already_use:
            new_name = name
            num += 1
            new_name = f'{name}{num}'
        already_use.append(new_name)
        return f'{new_name}@beegeek.bzz'
    
for name in new_names:
     print(new_mail(name))