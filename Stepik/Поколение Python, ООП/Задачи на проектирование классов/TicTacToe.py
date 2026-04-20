class TicTacToe:
    def __init__(self):
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.turn = "X"
        self.game_over = False

    def mark(self, row, col):
        if self.game_over:
            print("Игра окончена")
            return

        r, c = row - 1, col - 1

        if self.board[r][c] is not None:
            print("Недоступная клетка")
            return

        self.board[r][c] = self.turn

        # проверка победы
        if self._check_winner(self.turn):
            self.game_over = True
        # проверка ничьей (ВАЖНО)
        elif all(cell is not None for row in self.board for cell in row):
            self.game_over = True

        self.turn = "O" if self.turn == "X" else "X"

    def winner(self):
        if self._check_winner("X"):
            return "X"
        if self._check_winner("O"):
            return "O"

        if all(cell is not None for row in self.board for cell in row):
            return "Ничья"

        return None

    def show(self):
        for i, row in enumerate(self.board):
            print("|".join(cell if cell else " " for cell in row))
            if i < 2:
                print("-----")

    def _check_winner(self, p):
        b = self.board

        for i in range(3):
            if all(b[i][j] == p for j in range(3)):
                return True
            if all(b[j][i] == p for j in range(3)):
                return True

        if all(b[i][i] == p for i in range(3)):
            return True

        if all(b[i][2 - i] == p for i in range(3)):
            return True

        return False
