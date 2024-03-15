toppings = []
flag = True
while flag:
    supplements = input("Write what topping you want to add? \nIf you no longer need supplements, enter 'quit'\n\t")
    if supplements.lower() == "quit":
        break
    else:
        toppings.append(supplements)
        print(f"The {supplements.lower()} was successfully added to the order\n"
              "Current list of additives:")
        for topping in toppings:
            print(f"\t{topping}")