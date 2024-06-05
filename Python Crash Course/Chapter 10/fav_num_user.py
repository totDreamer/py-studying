import json
from favorite_num import whats_your_num


def fav_num_user(user_file):
    user_name = input("Enter your name: ").title()
    try:
        with open(user_file, "w") as u:
            json.dump(user_name, u)
    except FileNotFoundError:
        pass
    else:
        whats_your_num()