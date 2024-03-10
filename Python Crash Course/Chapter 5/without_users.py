users = ["admin", "MBA", "BMA", "HBS", "BOS"]
if users:
    for user in users:
        if user == "admin":
            print(f"Hello {user}, would you like to see status report?")
        else:
            print(f"Hello {user}, thank you for logging in again!")
else:
    print("We need to ind some users!")
