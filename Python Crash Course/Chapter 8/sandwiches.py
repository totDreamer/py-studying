def sandwiches(*toppings):
    print("You have selected the following sandwich additions:\n")
    for topping in toppings:
        print(f"\t- {topping.title()}")


sandwiches("cucumbers", "tomatoes", "cheddar cheese", "cream cheese")