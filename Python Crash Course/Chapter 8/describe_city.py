def describe_city(*, city, country = "USA"):
    print(f"{city.title()} is in {country.title()}")


describe_city(city = "New York")
describe_city(city = "Verkhoturye", country = "Russia")
describe_city(city = "Gleendale")