pizza_list = ["Hawaiian", "4 cheese", "Pepperoni"]
new_pizza = pizza_list[:]
pizza_list.append("Naruto")
new_pizza.append("Dor Blu")

print("My favorite pizzas:", end = " ")
for pizza in pizza_list:
    print(pizza, end = " ")
print("\n")
print("My friend favorite pizzas:", end = " ")
for pizza in new_pizza:
    print(pizza, end = " ")