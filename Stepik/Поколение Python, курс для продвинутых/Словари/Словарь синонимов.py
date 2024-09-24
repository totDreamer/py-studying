n = int(input())
string_dict = {}
string_dict_rev = {}
for _ in range(n):
    value, key = input().split()
    string_dict[key] = value
    string_dict_rev[value] = key
new_word = input()
if new_word in string_dict:
    print(string_dict[new_word])
else:
    print(string_dict_rev[new_word])