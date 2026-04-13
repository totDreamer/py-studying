def auto_repr(args, kwargs):
    def decorator(cls):
        def format_value(value):
            if isinstance(value, str):
                return repr(value)
            return str(value)

        def __repr__(self):
            parts = []

            for attr in args:
                parts.append(format_value(getattr(self, attr)))

            for attr in kwargs:
                parts.append(f"{attr}={format_value(getattr(self, attr))}")

            return f"{cls.__name__}({', '.join(parts)})"

        cls.__repr__ = __repr__
        return cls

    return decorator
