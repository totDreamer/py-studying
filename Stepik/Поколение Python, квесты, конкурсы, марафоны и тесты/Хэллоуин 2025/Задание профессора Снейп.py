def room_count():
    if switch() == 'OFF':
        switch()

    count = 1
    while True:
        for _ in range(count):
            if front() == 'ON':
                switch()
        for _ in range(count):
            state = back()
        
        if state == 'OFF':
            return count
         
        count += 1

    

