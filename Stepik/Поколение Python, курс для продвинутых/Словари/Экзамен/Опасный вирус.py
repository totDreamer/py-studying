files_accept = {}
commands = {
    'execute': 'X',
    'read': 'R',
    'write': 'W'
            }

for _ in range(int(input())):
    file = input().split()
    for i in file:
        if file.index(i) == 0:
            files_accept[i] = files_accept.get(i, set())
        else:
            files_accept[file[0]].add(i)

for _ in range(int(input())):
    file = input().split()
    file_check = {}
    for i in file:
        if file.index(i) == 0:
            file_check[commands[i]] = file_check.get(commands[i], [])
        else:
            file_check[commands[file[0]]].append(i)
    for key, value in file_check.items():
        if key in files_accept[value[0]]:
            print('OK')
        else:
            print('Access denied')