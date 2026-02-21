def hash_function(obj):
    obj = str(obj)

    def first_value(string):
        length = len(string)
        result = 0
        for i in range(length // 2):
            result += ord(string[i]) * ord(string[-(i + 1)])
        if length % 2:
            result += ord(string[length // 2])
        return result

    def second_value(string):
        result = 0
        for i, char in enumerate(string, start=1):
            if i % 2:
                result += ord(char) * i
            else:
                result -= ord(char) * i
        return result

    return (first_value(obj) * second_value(obj)) % 123456791


print(hash_function("python"))
