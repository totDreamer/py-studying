users = ["admin", "MBA", "BMA", "HBS", "BOS"]
for user in users:
    if user == "admin":
        print(f"Hello {user}, would you like to see status report?")
    else:
        print(f"Hello {user}, thank you for logging in again!")