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
family = [helga, michael]
for name in family:
    for key in name:
        print(key.replace("_", " ").title(), end = " - ")
        print(name[key], end = "\n")
    print()