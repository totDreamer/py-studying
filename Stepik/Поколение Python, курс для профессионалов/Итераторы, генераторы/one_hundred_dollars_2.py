from itertools import combinations_with_replacement

def one_hundred_2(wallet):
    good_result = set()

    for i in range(1, 21):
        for c in combinations_with_replacement(wallet, i):
            if sum(c) == 100:
                good_result.add(c)

    return len(good_result)

wallet = [100, 50, 20, 10, 5]
print(one_hundred_2(wallet))