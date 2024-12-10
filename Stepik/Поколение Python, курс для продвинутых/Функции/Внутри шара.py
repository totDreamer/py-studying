def on_circle(abscissas, ordinates, applicates):
    return all(map(lambda x: x[0]**2 + x[1]**2 + x[2]**2 <= 4, zip(abscissas, ordinates, applicates)))

print(on_circle(map(float, input().split()), map(float, input().split()), map(float, input().split())))