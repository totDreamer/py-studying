rivers = {"russia": "volga",
          "usa": "missuri",
          "kazakhstan": "irtish",
          "japan": "sinano"
          }
for country, river in rivers.items():
    print(f"{river.title()} is a largest river in {country.title()}")