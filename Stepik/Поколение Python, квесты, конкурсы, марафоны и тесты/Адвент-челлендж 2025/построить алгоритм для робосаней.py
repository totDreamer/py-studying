from itertools import combinations_with_replacement

waste_dict = {
    '1': 35,
    '5': 130,
    '10': 170,
    '15': 240,
    '20': 300
}

all_combs = []

for r in range(3, 45):
    combs = combinations_with_replacement(waste_dict.keys(), r)
    filtered = filter(lambda comb: 44 <= sum(map(int, comb)) <= 61, combs)
    all_combs.extend(filtered)

combs_sum = {key: sum(waste_dict[k] for k in key) for key in all_combs}
print(min(combs_sum.items(), key=lambda x: x[1]))