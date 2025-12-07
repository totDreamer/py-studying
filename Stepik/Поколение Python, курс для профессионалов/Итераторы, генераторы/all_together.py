def all_together(*args):
    return (o for arg in args for o in arg)

objects = [range(3), 'bee', [1, 3, 5], (2, 4, 6)]
print(*all_together(*objects))