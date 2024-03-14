michael = ["7", "4"]
helga = ["5"]
egor = ["10"]
julia = ["19"]
marina = ["5", "7"]
alexandr = ["2"]
favorite_num = {"Michael": michael,
                "Helga": helga,
                "Egor": egor,
                "Julia": julia,
                "Marina": marina,
                "Alexandr": alexandr,
                }
for name, num in favorite_num.items():
    print(f"\n{name} favorite num is:")
    for n in num:
        print(f"\t{n}")