def sand_watch():
    num = 1
    count = 16
    def new_row(num, count):
        print((str(num) * (count)).center(16))
        if num < 4:    
            new_row(num+1, count-4)
            print((str(num) * (count)).center(16))
    new_row(num, count)

sand_watch()