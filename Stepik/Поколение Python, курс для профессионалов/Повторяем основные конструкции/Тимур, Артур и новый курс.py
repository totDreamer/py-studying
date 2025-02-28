def min_long(d1, d2, d3):
    d1, d2, d3 = int(d1), int(d2), int(d3)
    maximum = max(d1, d2, d3)
    if maximum < d1 + d2 + d3 - maximum:
        return d1+d2+d3
    else:
        return (d1+d2+d3 - maximum) * 2
    
print(min_long(input(), input(), input()) )