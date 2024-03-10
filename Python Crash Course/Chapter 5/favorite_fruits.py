favorite_fruits = ["pineapple", "orange", "lemon", "lime", "kiwi"]
fruits_for_test = ["Apple", "Pineapple", "Banana", "Orange", "Lemon", "Lime", "Kiwi"]
if favorite_fruits:
    if fruits_for_test:
        for fruit in fruits_for_test:
            if fruit.lower() in favorite_fruits:
                print(f"You really like {fruit}")