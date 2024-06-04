guest = input('Hello! Enter your name: \n\t')
filename = "D:/Python-Studying/txt_files/guest.txt"
with open(filename, "w") as f:
    f.write(guest)