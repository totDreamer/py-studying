foods = ["pizza", "falafel", "carrot cake", "cannoli", "ice cream"]

print(f"The first three items in the list are: {foods[:3]}")
print(f"The items from the middle of the list are: {foods[len(foods)//3:len(foods)//3 + 3]}")
print(f"The last three items in the list are: {foods[-3:]}")
