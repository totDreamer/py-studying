class Color:
    def __init__(self, hexcode):
        self.hexcode = hexcode

    @property
    def hexcode(self):
        return f"{self.r:0>2X}{self.g:0>2X}{self.b:0>2X}"

    @hexcode.setter
    def hexcode(self, hexcode):
        self.r = int(hexcode[:2], 16)
        self.g = int(hexcode[2:4], 16)
        self.b = int(hexcode[4:6], 16)


color = Color("0000FF")

print(color.hexcode)
print(color.r)
print(color.g)
print(color.b)
