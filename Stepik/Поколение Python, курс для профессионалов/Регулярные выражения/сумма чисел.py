from re import compile, findall

rejex_obj = compile(r"\d+")
a, b = map(int, input().split())
print(sum(map(int, rejex_obj.findall(input(), pos=a, endpos=b))))
