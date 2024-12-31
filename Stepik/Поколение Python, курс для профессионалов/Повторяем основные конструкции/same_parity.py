def same_parity(l):
    if len(l) == 0 :
        return l
    elif l[0] % 2 == 0:
        return [x for x in l if x % 2 == 0]
    else:
        return [x for x in l if x % 2 != 0]

print(same_parity([]))