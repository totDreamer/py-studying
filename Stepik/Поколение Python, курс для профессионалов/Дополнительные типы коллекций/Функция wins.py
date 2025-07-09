from collections import defaultdict

def wins(pairs):
    results = defaultdict(set)
    for winner, loser in pairs:
        results[winner].add(loser)
    
    return results

result = wins([('Тимур', 'Артур'), ('Тимур', 'Дима'), ('Дима', 'Артур')])

for winner, losers in sorted(result.items()):
    print(winner, '->', *sorted(losers))