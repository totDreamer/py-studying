age = int(input("How old are you?\n"))
if age < 2:
    print("You are an infant")
elif 2 <= age < 4:
    print("You are a toddler")
elif 4 <= age < 13:
    print("You are a child")
elif 13 <= age < 20:
    print("You are a teenager")
elif 20 <= age < 65:
    print("You are an adult")
else:
    print("You are an old man")
