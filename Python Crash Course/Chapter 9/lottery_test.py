from lottery import Lottery
from lottery_chance import LotteryChance

subsequence_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "A", "B", "C", "D", "E"]
lottery_1 = LotteryChance(subsequence_list)
lottery_1.choice_ticket()
lottery_1.winner_announce()
lottery_1.win_lottery_chance()