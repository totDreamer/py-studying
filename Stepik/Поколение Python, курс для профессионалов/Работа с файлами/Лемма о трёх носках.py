import sys

count = 0
last_result = {'Анри': 0, 'Дима': 0}
for line in sys.stdin:
    count += 1
    if count % 2 == 1:
        last_result['Анри'] = int(line.strip())
    else:
        last_result['Дима'] = int(line.strip())

if count%2==1:
    if last_result['Анри'] % 2 == 0:
        print('Анри')
    else:
        print('Дима')
else:
    if last_result['Дима'] % 2 == 0:
        print('Дима')
    else:
        print('Анри')