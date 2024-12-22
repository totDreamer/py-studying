def count_strings(file_name):
    with open(file_name, 'r') as file:
        return len(file.readlines())
    
print(count_strings(input()))