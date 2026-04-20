class Testpaper:
    def __init__(self, subject, answers, pass_mark):
        self.subject = subject
        self.answers = answers
        self.pass_mark = int(pass_mark.rstrip("%"))


class Student:
    def __init__(self):
        self._tests_taken = {}

    @property
    def tests_taken(self):
        if not self._tests_taken:
            return "No tests taken"
        return self._tests_taken

    def take_test(self, testpaper, student_answers):
        correct = sum(1 for a, b in zip(testpaper.answers, student_answers) if a == b)

        percent = round(correct / len(testpaper.answers) * 100)

        result = "Passed!" if percent >= testpaper.pass_mark else "Failed!"
        self._tests_taken[testpaper.subject] = f"{result} ({percent}%)"
