class Path:
    def __init__(self, *args):
        self.path = args

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, args):
        full_path = []
        for arg in args:
            if isinstance(arg, self.__class__):
                full_path.append(arg.path)
            elif isinstance(arg, str):
                full_path.append(arg)
        self._path = "/".join(full_path)

    def __repr__(self):
        return f"Path('{self.path}')"

    def __str__(self):
        return f"{self.path}"

    def __truediv__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self.path + "/" + other.path)
        elif isinstance(other, str):
            return self.__class__(self.path + "/" + other)
        return NotImplemented

    def __itruediv__(self, other):
        if isinstance(other, self.__class__):
            self._path += "/" + other.path
            return self
        elif isinstance(other, str):
            self._path += "/" + other
            return self
        return NotImplemented


path = Path("home", "user", "docs")

print(str(path))
print(repr(path))


path = Path(Path("home"), "user", Path("docs"))

print(path)


path = Path("home", "user") / Path("docs")

print(path)


path1 = Path("home")
path2 = Path("user/docs")
path3 = path1 / path2

print(path1)
print(path2)
print(path3)


path = Path("home")
path /= "user"

print(path)


path1 = Path("home") / Path("user")
path2 = Path("docs")
path1 /= path2

print(path1)


path = Path("home")

print(path.__truediv__(2))
print(path.__itruediv__(5))


path1 = Path("home")
path2 = Path("user/docs", Path("books/book.pdf"))
path3 = path1 / path2

print(path3)
