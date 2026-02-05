from math import sqrt


class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c
        self._d = self.b**2 - 4 * self.a * self.c

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, a):
        self._a = a
        self._d = self.b**2 - 4 * self.a * self.c

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, b):
        self._b = b
        self._d = self.b**2 - 4 * self.a * self.c

    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, c):
        self._c = c
        self._d = self.b**2 - 4 * self.a * self.c

    @property
    def x1(self):
        if self._d > 0:
            return (-self.b - sqrt(self._d)) / (2 * self.a)
        elif self._d == 0:
            return 0.0

    @property
    def x2(self):
        if self._d > 0:
            return (-self.b + sqrt(self._d)) / (2 * self.a)
        elif self._d == 0:
            return 0.0

    @property
    def view(self):
        char_1 = "-" if self.b < 0 else "+"
        char_2 = "-" if self.c < 0 else "+"
        return f"{self.a}x^2 {char_1} {abs(self.b)}x {char_2} {abs(self.c)}"

    @property
    def coefficients(self):
        return (self.a, self.b, self.c)

    @coefficients.setter
    def coefficients(self, tup):
        self.a, self.b, self.c = tup
        self._d = self.b**2 - 4 * self.a * self.c


polynom = QuadraticPolynomial(1, 2, -3)

print(polynom.a)
print(polynom.b)
print(polynom.c)


polynom = QuadraticPolynomial(1, 2, -3)

print(polynom.x1)
print(polynom.x2)


polynom = QuadraticPolynomial(1, 2, -3)

print(polynom.view)
print(polynom.coefficients)


polynom = QuadraticPolynomial(1, 2, -3)

polynom.coefficients = (1, -5, 6)
print(polynom.x1)
print(polynom.x2)
print(polynom.view)


polynom = QuadraticPolynomial(1, 2, -3)

polynom.coefficients = (5, 0, 0)
print(polynom.x1)
print(polynom.x2)
print(polynom.view)


polynom = QuadraticPolynomial(500, -601, 101)

print(polynom.a, polynom.b, polynom.c)
print(polynom.x1)
print(polynom.x2)
print(polynom.coefficients)
print(polynom.view)


polynom = QuadraticPolynomial(500, -601, 101)

print(polynom.a, polynom.b, polynom.c)
print(polynom.x1)
print(polynom.x2)
print(polynom.coefficients)
print(polynom.view)

print()

polynom.a, polynom.b, polynom.c = (-1000, 1202, -202)
print(polynom.a, polynom.b, polynom.c)
print(polynom.x1)
print(polynom.x2)
print(polynom.coefficients)
print(polynom.view)
