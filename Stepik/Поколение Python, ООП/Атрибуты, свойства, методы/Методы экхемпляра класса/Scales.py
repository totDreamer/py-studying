class Scales:
    def __init__(self):
        self.left_weight = 0
        self.right_weight = 0

    def add_right(self, weight):
        self.right_weight += weight

    def add_left(self, weight):
        self.left_weight += weight

    def get_result(self):
        if self.left_weight == self.right_weight:
            return "Весы в равновесии"
        elif self.left_weight > self.right_weight:
            return "Левая чаша тяжелее"
        else:
            return "Правая чаша тяжелее"


scales = Scales()

scales.add_right(1)
scales.add_right(1)
scales.add_left(2)

print(scales.get_result())


scales.add_right(1)
scales.add_left(2)

print(scales.get_result())

scales = Scales()

scales.add_right(2)
scales.add_left(1)

print(scales.get_result())
