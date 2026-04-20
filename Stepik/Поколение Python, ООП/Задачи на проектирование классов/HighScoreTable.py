class HighScoreTable:
    def __init__(self, limit):
        self.limit = limit
        self.scores = []

    def update(self, score):
        if len(self.scores) < self.limit:
            self.scores.append(score)
        else:
            if score > self.scores[-1]:
                self.scores.append(score)
            else:
                return

        self.scores.sort(reverse=True)

        if len(self.scores) > self.limit:
            self.scores.pop()

    def reset(self):
        self.scores.clear()
