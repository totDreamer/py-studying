def input_reverse():
    data = []
    
    def new_input():
        elem = int(input())
        data.insert(0, elem)
        if elem != 0:
            new_input()

    new_input()
    print(*data, sep='\n')

input_reverse()