import json
from favorite_num import whats_your_num
def favorite_num_read(filename):
    try:
        with open(filename) as f:
            favorite_num = json.load(f)
    except FileNotFoundError:
        print("No such file or directory")
        whats_your_num(filename)

    else:
        return favorite_num
