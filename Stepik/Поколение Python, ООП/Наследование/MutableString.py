from collections import UserString


class MutableString(UserString):
    def lower(self):
        self.data = self.data.lower()

    def upper(self):
        self.data = self.data.upper()

    def sort(self, key=None, reverse=False):
        self.data = "".join(sorted(self.data, key=key, reverse=reverse))

    def __setitem__(self, index, value):
        semi_res = list(self.data)
        semi_res[index] = value
        self.data = "".join(semi_res)

    def __delitem__(self, index):
        semi_res = list(self.data)
        del semi_res[index]
        self.data = "".join(semi_res)


mutablestring = MutableString("Beegeek")

mutablestring.lower()
print(mutablestring)
mutablestring.upper()
print(mutablestring)
print(mutablestring)
print()


mutablestring = MutableString("beegeek")

print(mutablestring)
mutablestring[0] = "B"
mutablestring[-4] = "G"
print(mutablestring)
print()


words = [
    "improve",
    "north",
    "now",
    "there",
    "outside",
    "set",
    "into",
    "time",
    "campaign",
    "onto",
    "change",
    "source",
    "use",
    "huge",
    "specific",
    "consumer",
    "speak",
    "card",
    "century",
    "late",
    "focus",
    "money",
    "successful",
    "myself",
    "available",
    "rise",
    "no",
    "charge",
    "hit",
    "friend",
    "cost",
    "billion",
    "financial",
    "model",
    "decade",
    "whole",
    "space",
    "service",
    "agreement",
    "home",
    "represent",
    "away",
    "describe",
    "plan",
    "drop",
    "dream",
    "leg",
    "mouth",
    "interesting",
    "provide",
    "indeed",
    "thing",
    "practice",
    "miss",
    "bring",
    "important",
    "court",
    "talk",
    "true",
    "conference",
    "tell",
    "issue",
    "identify",
    "hand",
    "appear",
    "stuff",
    "run",
    "present",
    "good",
    "region",
    "detail",
    "recognize",
    "international",
    "behavior",
    "attack",
    "politics",
    "great",
    "baby",
    "measure",
    "whether",
    "yard",
    "with",
    "pressure",
    "role",
    "eight",
    "man",
    "she",
    "four",
    "them",
    "adult",
    "clear",
    "marriage",
    "meeting",
    "notice",
]

for word in words:
    mutablestring = MutableString(word)
    print(mutablestring, end=" ")

    mutablestring.upper()
    print(mutablestring, end=" ")

    mutablestring.sort(key=lambda char: ord(char), reverse=True)
    print(mutablestring)
print()


text = "Beautiful is better than ugly."

mutablestring = MutableString(text)

del mutablestring[9]
print(mutablestring)

del mutablestring[-6]
print(mutablestring)
print()


mutablestring = MutableString("Beegeek")
del mutablestring[-1]

print(mutablestring)
