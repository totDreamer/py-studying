import json
def whats_your_num():
    fav_num = input("What's your favorite number?\n\t")
    try:
        fav_num = int(fav_num)

    except ValueError:
        print("Please enter a number")

    else:
        filename = input("What's directory you want to save your favorite numbers?\n\t")
        with open(filename, "w") as f:
            json.dump(fav_num, f)