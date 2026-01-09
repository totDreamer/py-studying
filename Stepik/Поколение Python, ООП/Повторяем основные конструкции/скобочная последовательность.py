from re import search, sub


def is_closed(string):
    pattern = r"\(\)"

    def rec_test(result):
        if not result:
            return True
        if result and not search(pattern, result):
            return False

        result = sub(pattern, "", result)
        return rec_test(result)

    return rec_test(string)


print(is_closed("()()()"))
print(is_closed("(())"))
print(is_closed("()()()("))
print(is_closed(")("))
print(is_closed("(()))"))
