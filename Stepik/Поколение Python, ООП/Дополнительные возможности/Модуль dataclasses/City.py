from dataclasses import dataclass


@dataclass
class City:
    name: str
    population: int
    founded: int


city = City("Tokyo", 14043239, 1457)

print(city)
print(city.name)
print(city.population)
print(city.founded)
