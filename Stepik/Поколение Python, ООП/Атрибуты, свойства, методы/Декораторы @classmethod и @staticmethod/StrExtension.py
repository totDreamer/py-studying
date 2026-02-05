class StrExtension:
    @staticmethod
    def remove_vowels(string):
        vowels = ("a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "Y")
        return "".join(filter(lambda x: x not in vowels, string))

    @staticmethod
    def leave_alpha(string):
        return "".join(filter(str.isalpha, string))

    @staticmethod
    def replace_all(string, chars, char):
        return "".join((sym if sym not in chars else char for sym in string))


print(StrExtension.remove_vowels("Python"))
print(StrExtension.remove_vowels("Stepik"))


print(StrExtension.leave_alpha("Python111"))
print(StrExtension.leave_alpha("__Stepik__()"))


print(StrExtension.replace_all("Python", "Ptn", "-"))
print(StrExtension.replace_all("Stepik", "stk", "#"))
