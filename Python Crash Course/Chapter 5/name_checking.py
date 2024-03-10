current_users = ["admin", "MBA", "BMA", "HBS", "BOS"]
new_users = ["admin", "Helga", "BMA", "Misa", "Itachi"]
current_users = [i.lower() for i in current_users]
if new_users:
    for user in new_users:
        if user.lower() in current_users:
            print(f"{user} is already registered.")
        else:
            current_users.append(user.lower())
            print(f"{user} is registered.")

print(current_users)