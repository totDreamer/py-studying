from itertools import product


class Knight:
    def __init__(self, horizontal, vertical, color):
        self.horizontal = horizontal
        self.vertical = vertical
        self.color = color
        self.h_translate = {
            "a": 1,
            "b": 2,
            "c": 3,
            "d": 4,
            "e": 5,
            "f": 6,
            "g": 7,
            "h": 8,
        }
        self.h_translate_rev = {value: key for key, value in self.h_translate.items()}

    def get_char(self):
        return "N"

    def all_moves(self):
        int_horizontal = self.h_translate[self.horizontal]

        movement = (
            step
            for step in product((1, -1, 2, -2), repeat=2)
            if set(map(abs, step)) == {1, 2}
        )

        result = {
            (self.h_translate_rev[step[0] + int_horizontal], step[1] + self.vertical)
            for step in movement
            if 1 <= step[0] + int_horizontal <= 8 and 1 <= step[1] + self.vertical <= 8
        }

        return result

    def can_move(self, h_mark, v_mark):
        return (h_mark, v_mark) in self.all_moves()

    def move_to(self, h_mark, v_mark):
        if self.can_move(h_mark, v_mark):
            self.horizontal = h_mark
            self.vertical = v_mark

    def draw_board(self):
        row_index = self.h_translate[self.horizontal] - 1
        col_index = self.vertical - 1
        board = [["." for _ in range(8)] for _ in range(8)]

        for move in self.all_moves():
            board[move[1] - 1][self.h_translate[move[0]] - 1] = "*"

        board[col_index][row_index] = self.get_char()

        for line in reversed(board):
            print(*line, sep="")


knight = Knight("c", 3, "white")

print(knight.color, knight.get_char())
print(knight.horizontal, knight.vertical)


knight = Knight("c", 3, "white")

print(knight.horizontal, knight.vertical)
print(knight.can_move("e", 5))
print(knight.can_move("e", 4))

knight.move_to("e", 4)
print(knight.horizontal, knight.vertical)


knight = Knight("c", 3, "white")

knight.draw_board()


knight = Knight("e", 5, "black")

knight.draw_board()
knight.move_to("d", 3)
print()
knight.draw_board()
