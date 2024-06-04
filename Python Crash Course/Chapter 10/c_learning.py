filename = "D:/Python-Studying/txt_files/python_learning.txt"
with open(filename) as f:
    lines = f.readlines()
for line in lines:
    line = line.replace("Python", "C#")
    print(line.rstrip())