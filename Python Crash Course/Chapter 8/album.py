def make_album(*, name : str, album : str):
    new_album = {}
    new_album[name.title()] = album.title()
    return new_album


linkin_park = make_album(name = "Linkin Park", album = "Meteora")
hollywood_undead = make_album(name = "hollywood undead", album = "notes from the undeground")
skillet = make_album(name = "skillet", album = "Awake and Alive")

groups = [linkin_park, hollywood_undead, skillet]

for group in groups:
    for name, album in group.items():
        print(f"{name} : {album}")