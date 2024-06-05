import json
from fav_num_user import fav_num_user

def fav_num_user_check(user_name, fav_num):
    try:
        with open(user_name) as u:
            user = json.load(u)
        with open(fav_num) as f:
            fav_num = json.load(f)
    except FileNotFoundError:
        print("We haven't met before")
        fav_num_user(user_name)
    else:
        return user, fav_num

