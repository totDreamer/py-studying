import random


class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.mine = False
        self.neighbours = 0


class Game:
    def __init__(self, rows, cols, mines):
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.board = [[Cell(i, j) for j in range(cols)] for i in range(rows)]
        self._place_mines()
        self._calculate_neighbours()

    def _place_mines(self):
        positions = random.sample(
            [(i, j) for i in range(self.rows) for j in range(self.cols)], self.mines
        )

        for i, j in positions:
            self.board[i][j].mine = True

    def _calculate_neighbours(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j].mine:
                    self.board[i][j].neighbours = 0
                else:
                    self.board[i][j].neighbours = self._count_mines(i, j)

    def _count_mines(self, row, col):
        count = 0

        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if i == row and j == col:
                    continue
                if 0 <= i < self.rows and 0 <= j < self.cols:
                    if self.board[i][j].mine:
                        count += 1

        return count
