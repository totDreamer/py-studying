name = input("Как тебя зовут?\n")
olya_name = ["Оля", "Олечка", "Олячка", "Хельга"]
if name.title() in olya_name:
    print(f"{name.title()}, я тебя люблю!")
if name not in olya_name:
    print(f"{name.title()}, вы кто такие? Я вас не звал. Идите нахуй")

