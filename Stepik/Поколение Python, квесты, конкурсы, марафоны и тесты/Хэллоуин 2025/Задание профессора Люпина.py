def journey_ends(flights):
    points = {}
    for start, end in flights:
        points[start] = points.get(start, 0) + 1
        points[end] = points.get(end, 0) - 1

    start = next(p for p, b in points.items() if b==1)
    end = next(p for p, b in points.items() if b==-1)
    return (start, end)

flights = [('Hogsmeade', 'Little Whinging'), ('London', 'Hogsmeade')]
print(journey_ends(flights))

flights = [('Hogsmeade', 'Tinworth'), ("Ottery St. Catchpole", 'Chipping Clodbury'), ("Godric's Hollow", "Ottery St. Catchpole"), ('Chipping Clodbury', 'Hogsmeade')]
print(journey_ends(flights))

flights = [('C', 'D'), ('A', 'B'), ('B', 'C')]
print(journey_ends(flights))