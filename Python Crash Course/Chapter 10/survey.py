filename = "D:/Python-Studying/txt_files/survey.txt"
with open(filename, "a") as f:
    question = input('Hello! Why do you like Python: \n\t')
    print("Great answer. Thank You!")
    f.write(f"{question.title()}\n")
    while True:
        quit = input((f"Someone else?\nEnter the answer why you like Python or if you don't want to do it enter 'q'\n\t" ))
        if quit.lower() == 'q':
            break
        else:
            f.write(f"{quit.title()}\n")