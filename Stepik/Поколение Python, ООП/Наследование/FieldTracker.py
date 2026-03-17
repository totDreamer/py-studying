class FieldTracker:
    def __init__(self):
        self._base = {}
        for field in self.__class__.fields:
            self._base[field] = getattr(self, field)

    def base(self, attr):
        if getattr(self, attr) != self._base[attr]:
            return self._base[attr]
        return getattr(self, attr)

    def has_changed(self, attr):
        return getattr(self, attr) != self._base[attr]

    def changed(self):
        return {
            attr: base
            for attr, base in self._base.items()
            if getattr(self, attr) != base
        }

    def save(self):
        for attr in self.__class__.fields:
            self._base[attr] = getattr(self, attr)
