order = []
cooking_list = []
sandwiches = ["big bro", "original", "chefburger", "cheeseburger", "hamburger", "pastrami"]
flag = True

while flag:
    sandwich = input("Write what sandwich you want to order?\nIf this is all, enter 'quit'\n\t")
    if sandwich.lower() == "quit":
        break
    if sandwich.lower() not in sandwiches:
        print("Check if the sandwich name is entered correctly and try again")
        continue
    else:
        order.append(sandwich.lower())
        print(f"The {sandwich.title()} was successfully added to the order\n"
            "Current order list:")
        for sand in order:
            print(f"\t{sand.title()}")

if "pastrami" in order:
    print("Sorry, we don`t have pastrami...")
    while "pastrami" in order:
        order.remove("pastrami")

while order:
    position = order.pop()
    cooking_list.append(position)

print(cooking_list, order, sep = "\n")