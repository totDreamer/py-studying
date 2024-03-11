favorite_languages = {"jen": "python",
                      "sarah": "c",
                      "edward": "ruby",
                      "phil": "python",
                      }
names = ["jen", "sarah", "michael", "edward", "phil", "helga"]
for name in names:
    if name in favorite_languages:
        print(f"{name.title()}, thank you for your answer")
    else:
        favorite_languages[name] = input(f"{name.title()}, what is your favorite language?\n")
print()
for name, fl in favorite_languages.items():
    print(f"{name.title()} favorite language is {fl.title()}")

# Выводим уникальные значения в словаре
print("\nUnique values:")
for language in set(favorite_languages.values()):
    print(language.title())