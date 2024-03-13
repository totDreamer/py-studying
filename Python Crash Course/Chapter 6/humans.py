helga = {"first_name": "Helga",
         "last_name": "Bekker",
         "age": "24",
         "city": "San Francisco"
         }
michael = {"first_name": "Michael",
         "last_name": "Bekker",
         "age": "24",
         "city": "San Francisco"
         }
egor = {"first_name": "Egor",
         "last_name": "Gunko",
         "age": "13",
         "city": "Los Angeles"
         }
family = [helga, michael, egor]
for name in family:
    full_name = name["first_name"] + " " + name["last_name"]
    print(f"\nHello, {full_name}, i know you are {name['age']} years old and living in the {name['city']}")


    print()