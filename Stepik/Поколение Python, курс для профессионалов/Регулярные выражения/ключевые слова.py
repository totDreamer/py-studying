from re import sub, search, IGNORECASE

kw_list = [
    "False",
    "None",
    "True",
    "and",
    "as",
    "assert",
    "async",
    "await",
    "break",
    "class",
    "continue",
    "def",
    "del",
    "elif",
    "else",
    "except",
    "finally",
    "for",
    "from",
    "global",
    "if",
    "import",
    "in",
    "is",
    "lambda",
    "nonlocal",
    "not",
    "or",
    "pass",
    "raise",
    "return",
    "try",
    "while",
    "with",
    "yield",
]

kw_string = " ".join(kw_list)


def kw_test(s):
    s = s.group()
    if search(rf"\b{s}\b", kw_string, flags=IGNORECASE):
        return "<kw>"
    else:
        return s


def kw(string):
    return sub(r"\b\w{2,}\b", kw_test, string)


print(kw(input()))
