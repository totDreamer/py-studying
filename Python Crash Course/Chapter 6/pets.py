itachi = {"kind" : "cat",
          "name" : "Itachi",
          "owner_name" : "Mikhael",
          "phone" : "7776665544"
          }
misa = {"kind" : "cat",
          "name" : "Misa",
          "owner_name" : "Mikhael",
          "phone" : "7776665544"
          }
marta = {"kind" : "cat",
          "name" : "Marta",
          "owner_name" : "Marina",
          "phone" : "8887776655"
          }
vasya = {"kind" : "cat",
          "name" : "Vasya",
          "owner_name" : "Marina",
          "phone" : "8887776655"
          }
anfisa = {"kind" : "cat",
          "name" : "Anfisa",
          "owner_name" : "Marina",
          "phone" : "8887776655"
          }
druzhok = {"kind" : "dog",
          "name" : "Druzhok",
          "owner_name" : "Alexandr",
          "phone" : "9998887766"
          }
kroshka = {"kind" : "dog",
          "name" : "Kroshka",
          "owner_name" : "Alexandr",
          "phone" : "9998887766"
           }
tosya = {"kind" : "dog",
          "name" : "Tosya",
          "owner_name" : "Marina",
          "phone" : "8887776655"
         }
pets = [itachi, misa, marta, vasya, anfisa, druzhok, kroshka, tosya]

for pet in pets:
    print(f"\n{pet['name']} is a {pet['kind']}.\n"
          f"Owner: {pet['owner_name']}\n"
          f"Owner phone number: {pet['phone']}")