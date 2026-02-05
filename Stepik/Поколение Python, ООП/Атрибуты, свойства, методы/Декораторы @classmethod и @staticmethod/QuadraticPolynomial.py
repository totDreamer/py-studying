class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def from_iterable(cls, it):
        a, b, c = [char for char in it]
        return cls(a, b, c)

    @classmethod
    def from_str(cls, string):
        try:
            a, b, c = list(map(int, string.split()))
        except ValueError:
            a, b, c = list(map(float, string.split()))
        return cls(a, b, c)


polynom = QuadraticPolynomial(1, -5, 6)

print(polynom.a)
print(polynom.b)
print(polynom.c)


polynom = QuadraticPolynomial.from_iterable([2, 13, -1])

print(polynom.a)
print(polynom.b)
print(polynom.c)


polynom = QuadraticPolynomial.from_str("-1.5 4 14.8")

print(polynom.a)
print(polynom.b)
print(polynom.c)
print(polynom.a + polynom.b + polynom.c)
