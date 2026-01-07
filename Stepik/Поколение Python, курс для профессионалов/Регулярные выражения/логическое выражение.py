from re import split

print(", ".join(split(r"\s*(?:and|or|\||&)\s*", input())))
