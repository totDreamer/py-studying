def make_album(*, name: str, album: str):
    new_album = {}
    new_album[name.title()] = album.title()
    return new_album


linkin_park = make_album(name="Linkin Park", album="Meteora")
hollywood_undead = make_album(name="hollywood undead", album="notes from the undeground")
skillet = make_album(name="skillet", album="Awake and Alive")

groups = [linkin_park, hollywood_undead, skillet]

while True:
    n = input(f"Enter the name of the music group or artist\nIf you want to end enter 'q'\n\t")
    if n == "q":
        break
    a = input(f"Enter the name of the album\n\t")
    groups.append(make_album(name=n, album=a))

print("\n\nFinal list looks like:\n")
for group in groups:
    for name, album in group.items():
        print(f"{name} : {album}")
