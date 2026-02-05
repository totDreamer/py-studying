from re import findall, fullmatch


class CaseHelper:
    @staticmethod
    def is_snake(string):
        if fullmatch(r"[a-z]+(_[a-z]+)*", string):
            return True
        else:
            return False

    @staticmethod
    def is_upper_camel(string):
        if fullmatch(r"([A-Z][a-z]+)+", string):
            return True
        else:
            return False

    @staticmethod
    def to_snake(string):
        data = findall(r"[A-Z][a-z]+", string)
        return "_".join(map(str.lower, data))

    @staticmethod
    def to_upper_camel(string):
        data = findall(r"[a-z]+[^_]?", string)
        return "".join(map(str.title, data))


cases = [
    "assert_equal",
    "tear_down",
    "assertEqual",
    "setUp",
    "tearDown",
    "run",
    "exit",
    "setup",
    "its_wednesday_my_dudes",
]

for case in cases:
    print(CaseHelper.is_snake(case))
