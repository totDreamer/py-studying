class AttrsNumberObject:
    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)

    def __getattr__(self, name):
        if name == "attrs_num":
            return len(self.__dict__) + 1


music_group = AttrsNumberObject(name="Silent Poets", genre="acid jazz")

print(music_group.attrs_num)
