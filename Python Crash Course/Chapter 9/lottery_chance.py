from lottery import Lottery
from random import choices


class LotteryChance(Lottery):
    def __init__(self, subsequence):
        super().__init__(subsequence)
        self.try_ticket = ""
        self.lottery_chance = 0

    def win_lottery_chance(self):
        count_try = 0
        while True:
            count_try += 1
            self.try_ticket = "".join(choices(self.subsequence, k=4))
            if self.try_ticket == self.win_ticket:
                self.lottery_chance += count_try
                print(f"It took {self.lottery_chance} attempts to win")
                break