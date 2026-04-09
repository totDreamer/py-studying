class Lecture:
    def __init__(self, topic, start_time, duration):
        self.topic = topic
        self.start_time = start_time
        self.duration = duration

    def start_minutes(self):
        h, m = map(int, self.start_time.split(":"))
        return h * 60 + m

    def duration_minutes(self):
        h, m = map(int, self.duration.split(":"))
        return h * 60 + m

    def end_minutes(self):
        return self.start_minutes() + self.duration_minutes()


class Conference:
    def __init__(self):
        self.lectures = []

    def add(self, lecture):
        for lec in self.lectures:
            if not (
                lecture.end_minutes() <= lec.start_minutes()
                or lecture.start_minutes() >= lec.end_minutes()
            ):
                raise ValueError("Провести выступление в это время невозможно")

        self.lectures.append(lecture)

    def total(self):
        total_minutes = sum(lec.duration_minutes() for lec in self.lectures)
        return self._to_time(total_minutes)

    def longest_lecture(self):
        if not self.lectures:
            return "00:00"
        max_minutes = max(lec.duration_minutes() for lec in self.lectures)
        return self._to_time(max_minutes)

    def longest_break(self):
        if len(self.lectures) < 2:
            return "00:00"

        lectures = sorted(self.lectures, key=lambda x: x.start_minutes())

        max_break = 0
        for i in range(len(lectures) - 1):
            break_time = lectures[i + 1].start_minutes() - lectures[i].end_minutes()
            max_break = max(max_break, break_time)

        return self._to_time(max_break)

    def _to_time(self, minutes):
        h = minutes // 60
        m = minutes % 60
        return f"{h:02d}:{m:02d}"


conference = Conference()

conference.add(Lecture("Простые числа", "08:00", "01:30"))
conference.add(Lecture("Жизнь после ChatGPT", "10:00", "02:00"))
conference.add(Lecture("Муравьиный алгоритм", "13:30", "01:50"))
print(conference.total())
print(conference.longest_lecture())
print(conference.longest_break())
print()


conference = Conference()
conference.add(Lecture('Простые числа', '08:00', '01:30'))

try:
    conference.add(Lecture('Жизнь после ChatGPT', '09:00', '02:00'))
except ValueError as error:
    print(error)
print()


conference = Conference()
conference.add(Lecture('Простые числа', '08:00', '01:00'))
conference.add(Lecture('Жизнь после ChatGPT', '11:00', '02:00'))

try:
    conference.add(Lecture('Муравьиный алгоритм', '10:00', '04:00'))
except ValueError as error:
    print(error)