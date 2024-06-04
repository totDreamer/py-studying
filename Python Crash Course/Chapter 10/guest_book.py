filename = "D:/Python-Studying/txt_files/guest_book.txt"
with open(filename, "a") as f:
    guest = input('Hello! Enter your name: \n\t')
    print((f"Nice to meet you {guest.title()}"))
    f.write(f"{guest.title()}\n")
    while True:
        quit = input((f"Someone else?\nEnter your name or, if there are no more guests, enter 'q'\n\t" ))
        if quit.lower() == 'q':
            break
        else:
            f.write(f"{quit.title()}\n")