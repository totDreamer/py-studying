from itertools import combinations, chain

def one_hundred(wallet):
    good_result = ()
    for i in range(1, len(wallet) + 1):
        good_result = chain(good_result, filter(lambda x: sum(x)==100, combinations(wallet, i)))
    return len(set(good_result))

wallet = [100, 100, 50, 50, 50, 50, 20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
print(one_hundred(wallet))