class SuppressAll:
    def __enter__(self):
        return self

    def __exit__(self, *exc_info):
        return True


print("start")

with SuppressAll():
    print("Python generation!")
    raise ValueError

print("end")
print()


print("start")

with SuppressAll():
    print("Python generation!")

print("end")
