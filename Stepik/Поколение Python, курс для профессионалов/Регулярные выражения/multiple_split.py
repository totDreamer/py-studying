from re import split, escape


def multiple_split(string, delimiters):
    pattern = r"|".join(escape(r) for r in sorted(delimiters, key=len, reverse=True))
    return split(pattern, string)


print(multiple_split("beegeek-python.stepik", [".", "-"]))
print(multiple_split("Timur---Arthur+++Dima****Anri", ["---", "+++", "****"]))
print(multiple_split("timur.^[+arthur.^[+dima.^[+anri.^[+roma.^[+ruslan", [".^[+"]))
