from abc import ABC, abstractmethod


class Paragraph(ABC):
    def __init__(self, length):
        self.length = length
        self.lines = []
        self.current_line = ""

    def add(self, text):
        words = text.split()

        for word in words:
            if not self.current_line:
                self.current_line = word
            else:
                if len(self.current_line) + 1 + len(word) <= self.length:
                    self.current_line += " " + word
                else:
                    self.lines.append(self.current_line)
                    self.current_line = word

    def end(self):
        if self.current_line:
            self.lines.append(self.current_line)

        for line in self.lines:
            print(self._format_line(line))

        self._reset()

    def _reset(self):
        self.lines = []
        self.current_line = ""

    @abstractmethod
    def _format_line(self, line):
        pass


class LeftParagraph(Paragraph):
    def _format_line(self, line):
        return line


class RightParagraph(Paragraph):
    def _format_line(self, line):
        return " " * (self.length - len(line)) + line


leftparagraph = LeftParagraph(10)

leftparagraph.add("death")
leftparagraph.add("can have me")
leftparagraph.add("when it earns me")
leftparagraph.end()
print()


rightparagraph = RightParagraph(10)

rightparagraph.add('death')
rightparagraph.add('can have me')
rightparagraph.add('when it earns me')
rightparagraph.end()