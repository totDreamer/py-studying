def add_attr_to_class(**kwargs):
    def wrapper(cls):
        for key, value in kwargs.items():
            setattr(cls, key, value)

        return cls

    return wrapper


@add_attr_to_class(first_attr=1, second_attr=2)
class MyClass:
    pass


print(MyClass.first_attr)
print(MyClass.second_attr)
