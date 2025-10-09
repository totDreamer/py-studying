from sys import stdin

def max_math(math_list):
    results = []

    for example in math_list:
        results.append(eval(example))

    return max(results)

print(max_math(stdin.readlines()))