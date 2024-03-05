def IMT(*, weight : float, height : float) -> int:
    IMT = weight / (height ** 2)
    if IMT < 18.5:
        return "Недостаточная масса"
    elif 18.5 <= IMT <= 25:
        return "Оптимальная масса"
    else:
        return "Избыточная масса"
w = float(input())
h = float(input())
print(IMT(weight = w, height = h))