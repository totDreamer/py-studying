def fib_tree(h, k):
    fib = {1: (1,), 2: (1, 2), 3: (3, 5, 8, 13)}

    if h > 3:
        start = 4
        while start < h + 1:
            fib[start] = [fib[start-1][-1] + fib[start-1][-2], fib[start-1][-1] + fib[start-1][-2] + fib[start - 1][-1]]
            while len(fib[start]) < 2**(start-1):
                fib[start].append(fib[start][-1] + fib[start][-2])
            start += 1

    return fib[h][k-1]
            

print(fib_tree(1, 1))

print(fib_tree(3, 2))

print(fib_tree(3, 4))

print(fib_tree(4, 1))            
        
print(fib_tree(4, 5))