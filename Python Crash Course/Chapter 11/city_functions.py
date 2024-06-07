def city_functions(city, country, population = ""):
    if population:
        value = f"{city.title()}, {country.title()} - population {population}"
    else:
        value = f"{city.title()}, {country.title()}"
    return value
