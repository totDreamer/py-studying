guests_list = ["Michael Jackson", "Keanu Reeves", "Leonardo DiCaprio"]

guests_list[guests_list.index("Michael Jackson")] = "Samuel L Jackson"

guests_list.insert(0, "Karl Urban")
guests_list.insert(len(guests_list) // 2, "Charlie Hunnam")
guests_list.append("Matthew McConaughey")
while (len(guests_list)) > 2:
    canceled_guest = guests_list.pop(-1)
    print(f"{canceled_guest}, we have to cancel your invitation, I'm sorry ")

for guest in guests_list:
    print(f"Dear {guest}, you are invited to our modest dinner!")

for _ in range(len(guests_list)):
    del guests_list[0]
print(guests_list)