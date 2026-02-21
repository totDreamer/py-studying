class Ord:
    def __getattr__(self, name):
        if isinstance(name, str) and len(name) == 1:
            return ord(name)


obj = Ord()

print(obj.a)
print(obj.b)


obj = Ord()

print(obj.в)
print(obj.г)
