from sys import stdin
from collections import defaultdict

pokemons = defaultdict(int)
for name in stdin:
    pokemons[name.strip()] += 1

result = sum(
    map(
        lambda f_name: pokemons[f_name] - 1,
        filter(lambda name: pokemons[name] > 1, pokemons),
    )
)

print(result)
