import json
from favorite_num_check import favorite_num_read
def print_favorite_num(file):
    try:
        with open(file, "r") as f:
            result = json.load(f)
    except FileNotFoundError:
        favorite_num_read(file)
    else:
        print(f"Your favorite number is '{result}'")