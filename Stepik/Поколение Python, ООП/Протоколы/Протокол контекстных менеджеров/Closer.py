class Closer:
    def __init__(self, obj):
        self._obj = obj

    def __enter__(self):
        return self._obj

    def __exit__(self, *exc_info):
        try:
            self._obj.close()
        except AttributeError:
            print("Незакрываемый объект")


with Closer(5) as i:
    i += 1

print(i)
