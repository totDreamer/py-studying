class ValueDict(dict):
    def key_of(self, value):
        key = self.keys_of(value)
        if key:
            return key[0]
        return None

    def keys_of(self, value):
        reversed_dict = {}
        for v, k in self.items():
            reversed_dict[k] = reversed_dict.get(k, [])
            reversed_dict[k].append(v)
        try:
            return reversed_dict[value]
        except KeyError:
            return []


valuedict = ValueDict({"apple": 1, "banana": 2, "orange": 2})

print(valuedict.key_of(2))
print(*valuedict.keys_of(2))
print()


countries = {
    "Monaco": "Monaco",
    "Iceland": "Reykjavik",
    "Kenya": "Nairobi",
    "Kazakhstan": "Nur-Sultan",
    "Mali": "Bamako",
    "Colombia": "Bogota",
    "Finland": "Helsinki",
    "Costa Rica": "San Jose",
    "Cuba": "Havana",
    "France": "Paris",
    "Gabon": "Libreville",
    "Liberia": "Monrovia",
    "Angola": "Luanda",
    "India": "New Delhi",
    "Canada": "Ottawa",
    "Australia": "Canberra",
}

valuedict = ValueDict(countries)

print(valuedict.key_of("Moscow"))
print(*valuedict.keys_of("Washington"))
