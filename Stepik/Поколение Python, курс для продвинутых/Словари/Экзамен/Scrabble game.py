points = {
    1: "AEILNORSTU",
    2: "DG",
    3: "BCMP",
    4: "FHVWY",
    5: "K",
    8: "JX",
    10: "QZ"
    }
result = 0
for sym in input().upper():
    for key, value in points.items():
        if sym in value:
            result += key
print(result)