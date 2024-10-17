crypt = input()
new_crypt = []
crypt_dict = {}
sym_dict = {}
for i in crypt:
    crypt_dict.setdefault(i, 0)
    crypt_dict[i] += 1
for _ in range(int(input())):
    new_sym = input()
    sym_dict.setdefault(int(new_sym[-1]), new_sym[0])
for s in crypt:
    new_crypt.append(crypt_dict[s])
for s in new_crypt:
    print(sym_dict[s], end="")