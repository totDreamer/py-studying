guest_count = int(input("How many seats do you want to make a restaurant reservation for?\n\t"))
if guest_count > 8:
    print("You'll have to wait")
else:
    print("Your table is ready")