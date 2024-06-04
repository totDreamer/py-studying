from random import choices


class Lottery():
    def __init__(self, subsequence):
        self.subsequence = subsequence
        self.win_ticket = ""

    def choice_ticket(self):
        self.win_ticket = "".join(choices(self.subsequence, k=4))

    def winner_announce(self):
        print(f"The winning combination is {self.win_ticket.upper()}")


subsequence_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "A", "B", "C", "D", "E"]
