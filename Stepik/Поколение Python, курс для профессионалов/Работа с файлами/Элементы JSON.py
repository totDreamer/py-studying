import json, sys

string = sys.stdin.read()
jd_print = json.loads(string)

for key, value in jd_print.items():
    if isinstance(value, (list, tuple)):
        value = [str(i) for i in value]
        print(f'{key}: {', '.join(value)}')
    else:
        print(f'{key}: {value}')