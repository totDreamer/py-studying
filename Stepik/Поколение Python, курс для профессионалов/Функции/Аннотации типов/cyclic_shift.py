def cyclic_shift(numbers: list[int | float], step: int) -> None:
    step = step % len(numbers)
    if step > 0:
        numbers[:] = numbers[-step:] + numbers[:-step]
    if step < 0:
        step = abs(step)
        numbers[:] = numbers[step:] + numbers[:step]
    return None

numbers = [1, 2, 3, 4, 5]
cyclic_shift(numbers, 1)

print(numbers)

numbers = [1, 2, 3, 4, 5]
cyclic_shift(numbers, -2)

print(numbers)


numbers = [234, 235]
cyclic_shift(numbers, 15)

print(numbers)


numbers = [234, 235]
cyclic_shift(numbers, -22)

print(numbers)