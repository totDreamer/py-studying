from string import ascii_lowercase, ascii_uppercase


class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift

    def encode(self, text):
        result = []
        for char in text:
            if char in ascii_lowercase:
                idx = (ascii_lowercase.index(char) + self.shift) % 26
                result.append(ascii_lowercase[idx])
            elif char in ascii_uppercase:
                idx = (ascii_uppercase.index(char) + self.shift) % 26
                result.append(ascii_uppercase[idx])
            else:
                result.append(char)
        return "".join(result)

    def decode(self, text):
        result = []
        for char in text:
            if char in ascii_lowercase:
                idx = (ascii_lowercase.index(char) - self.shift) % 26
                result.append(ascii_lowercase[idx])
            elif char in ascii_uppercase:
                idx = (ascii_uppercase.index(char) - self.shift) % 26
                result.append(ascii_uppercase[idx])
            else:
                result.append(char)
        return "".join(result)


cipher = CaesarCipher(5)

print(cipher.encode("Beegeek"))
print(cipher.decode("Gjjljjp"))
