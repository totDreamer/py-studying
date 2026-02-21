class DefaultObject:
    def __init__(self, default=None, **kwargs):
        self.default = default
        for key, value in kwargs.items():
            object.__setattr__(self, key, value)

    def __getattr__(self, name):
        return self.default


god = DefaultObject(name="Ares", mythology="greek")

print(god.name)
print(god.mythology)
print(god.age)


god = DefaultObject(default=0, name="Tyr", mythology="scandinavian")

print(god.name)
print(god.mythology)
print(god.age)
