city = ["Saint-Petersburg", "Yekaterinburg", "Verkhoturye"]
mountains = ["Ural mountains", "Shymbulak", "Medeu"]
rivers = ["Tura", "Volga", "Missuri"]
favorite_places = {"city" : city,
                   "mountains" : mountains,
                   "rivers" : rivers
                   }
for place, places in favorite_places.items():
    print(f"\nMichael favorite {place} is:")
    for name in places:
        print(f"\t{name}")

