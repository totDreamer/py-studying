class HtmlTag:
    level = -1

    def __init__(self, tag, inline=False):
        self._tag = tag
        self._inline = "" if inline else "\n"

    def __enter__(self):
        self.__class__.level += 1
        print(self.__class__.level * "  " + f"<{self._tag}>", end=self._inline)
        return self

    def __exit__(self, *exc_info):
        if self._inline == "\n":
            print(self.__class__.level * "  " + f"</{self._tag}>")
        else:
            print(f"</{self._tag}>")
        self.__class__.level -= 1

    def print(self, text):
        if self._inline == "\n":
            print("  " * (self.__class__.level + 1) + text)
        else:
            print(text, end=self._inline)


with HtmlTag("body") as _:
    with HtmlTag("h1") as header:
        header.print("Поколение Python")
    with HtmlTag("p") as section:
        section.print(
            "Cерия курсов по языку программирования Python от команды BEEGEEK"
        )
print()


with HtmlTag("body") as _:
    with HtmlTag("h1", True) as header:
        header.print("Поколение Python")
    with HtmlTag("p", True) as section:
        section.print(
            "Cерия курсов по языку программирования Python от команды BEEGEEK"
        )
print()


with HtmlTag("body") as _:
    with HtmlTag("h1", True) as header:
        header.print("Здесь есть что-то интересное")
    with HtmlTag("a", True) as section:
        section.print("https://stepik.org/media/attachments/course/98974/watch_me.mp4")
