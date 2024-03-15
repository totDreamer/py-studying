dream_vacation = {}

while True:
    name = input("Hello! What`s your name\n")
    place = input(f"Nice to meet you, {name.title()}!\n"
                  "Where would you most like to go on your holiday?\n")
    again = input(f"Thank you for answer!\n\nAnyone else want to tell you about their favorite vacation spot?\n"
                  "Write 'yes' or 'no'\n\t")
    dream_vacation[name] = place
    if again.lower() == "no":
        break
print("\nHere's what we got:")
for name, place in dream_vacation.items():
    print(f"{name.title()} : {place.title()}")