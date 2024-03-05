guests_list = ["Michael Jackson", "Keanu Reeves", "Leonardo DiCaprio"]

guests_list[guests_list.index("Michael Jackson")] = "Samuel L Jackson"
for guest in guests_list:
    print(f"Dear {guest}, you are invited to our modest dinner!")