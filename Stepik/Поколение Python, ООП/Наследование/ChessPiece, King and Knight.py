from abc import ABC, abstractmethod
from string import ascii_lowercase


class ChessPiece(ABC):
    right_range = ascii_lowercase[:8]

    def __init__(self, horizontal, vertical):
        self.horizontal = self.is_correct(horizontal)
        self.vertical = self.is_correct(vertical)
        self._horizontal_index = self.right_range.index(self.horizontal)

    @abstractmethod
    def can_move(self):
        raise NotImplementedError

    @classmethod
    def is_correct(cls, value):
        if isinstance(value, int):
            if 1 <= value <= 8:
                return value
            else:
                raise ValueError("Число должно быть принадлежать диапазону от 1 до 8")
        elif isinstance(value, str):
            low_value = value.lower()
            if low_value in cls.right_range:
                return low_value
            else:
                raise ValueError("Значение должно быть символом от 'a' до 'h'")
        else:
            raise ValueError("Неккоректные данные")


class King(ChessPiece):
    def can_move(self, horizontal, vertical):
        vertical = self.is_correct(vertical)
        horizontal = self.is_correct(horizontal)
        dx = abs(self._horizontal_index - self.right_range.index(horizontal))
        dy = abs(self.vertical - vertical)
        return (dx <= 1 and dy <= 1) and (dx != 0 or dy != 0)


class Knight(ChessPiece):
    def can_move(self, horizontal, vertical):
        vertical = self.is_correct(vertical)
        horizontal = self.is_correct(horizontal)
        dx = abs(self._horizontal_index - self.right_range.index(horizontal))
        dy = abs(self.vertical - vertical)
        return sorted([dx, dy]) == [1, 2]


king = King("b", 2)

print(king.can_move("c", 3))
print(king.can_move("a", 1))
print(king.can_move("f", 7))
print()


knight = Knight("c", 3)

print(knight.can_move("e", 5))
print(knight.can_move("e", 4))
