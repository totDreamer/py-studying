def traffic(n):
    if n > 0:
        print('Не парковаться')
        n -= 1
        traffic(n)

traffic(3)
traffic(5)
traffic(0)