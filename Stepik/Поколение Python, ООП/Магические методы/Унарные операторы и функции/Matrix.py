class Matrix:
    def __init__(self, rows, cols, value=0):
        self.rows = rows
        self.cols = cols
        self.matrix = value

    @property
    def matrix(self):
        return self._matrix

    @matrix.setter
    def matrix(self, value):
        if isinstance(value, list):
            self._matrix = value
        else:
            self._matrix = [[value for _ in range(self.cols)] for _ in range(self.rows)]

    def get_value(self, row, col):
        return self.matrix[row][col]

    def set_value(self, row, col, value):
        self.matrix[row][col] = value

    def __repr__(self):
        return f"Matrix({self.rows}, {self.cols})"

    def __str__(self):
        return "\n".join([" ".join(map(str, row)) for row in self.matrix])

    def __pos__(self):
        return Matrix(self.rows, self.cols, [row[:] for row in self.matrix])

    def __neg__(self):
        return Matrix(
            self.rows, self.cols, [list(map(lambda x: -x, row)) for row in self.matrix]
        )

    def __invert__(self):
        return Matrix(self.cols, self.rows, [list(row) for row in zip(*self.matrix)])

    def __round__(self, n=None):
        if n is not None:
            return Matrix(
                self.rows,
                self.cols,
                [list(map(lambda x: round(x, n), row)) for row in self.matrix],
            )
        return Matrix(
            self.rows,
            self.cols,
            [list(map(lambda x: round(x), row)) for row in self.matrix],
        )


print(Matrix(2, 3))


matrix = Matrix(2, 3, 1)

print(+matrix)
print()
print(-matrix)


matrix = Matrix(2, 3, 1)

print(matrix)
print()
print(~matrix)
