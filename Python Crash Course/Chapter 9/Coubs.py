from random import randint


class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(f"You rolled a {randint(1, self.sides)} on the die")

six_sides_coub = Die(sides = 6)
while True:
    six_sides_coub.roll_die()
    reroll = input("Press any key to continue\nPress 'q' to quit\n\t")
    if reroll.lower() == 'q':
        print("Thanks for playing!")
        break