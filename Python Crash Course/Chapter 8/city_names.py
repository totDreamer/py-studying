def describe_city(*, city, country = "USA"):
    location = city.title() + ", " + country.title()
    return location
locations = []
while True:
    city = input("Enter a city name\nFor stop enter 'q'\n\t")
    if city == "q":
        break
    country = input("Enter a country in which the city is located\n\t")
    locations.append(describe_city(city=city, country=country))

for location in locations:
    print(location)