from itertools import groupby

def ranges(numbers):
    data = groupby(numbers, key=lambda x: numbers.index(x) - x)
    final_result = []
    
    for _, d in data:
        ran = list(d)
        final_result.append((ran[0], ran[-1]))

    return final_result


numbers = [1, 2, 3, 4, 7, 8, 10]

print(ranges(numbers))