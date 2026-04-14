class ToStringMixin:
    def __str__(self):
        return self._format()

    def __repr__(self):
        return self._format()

    def _format(self):
        items = list(self.__dict__.items())

        if len(items) > 6:
            items = items[:6]
            body = ", ".join(f"{repr(k)}: {repr(v)}" for k, v in items)
            body += ", ..."
        else:
            body = ", ".join(f"{repr(k)}: {repr(v)}" for k, v in items)

        return f"{self.__class__.__name__}({{{body}}})"
