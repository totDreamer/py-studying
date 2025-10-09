def polynom(x: int) -> int:
    result = x**2 + 1
    if not hasattr(polynom, 'values'):
        polynom.__dict__['values'] = set()
    polynom.values.add(result)
    return result

polynom(1)
polynom(2)
polynom(3)

print(*sorted(polynom.values))


for _ in range(10):
    polynom(10)
    
print(polynom.values)