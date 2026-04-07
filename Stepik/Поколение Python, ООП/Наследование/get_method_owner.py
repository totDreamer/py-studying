def get_method_owner(cls, method):
    cls_has_method = None
    for c in cls.mro():
        if method in c.__dict__:
            cls_has_method = c
            break
    return cls_has_method


class A:
    def m(self):
        pass


class B(A):
    pass


print(get_method_owner(B, "m"))
print()


class A:
    def m(self):
        pass


class B(A):
    def m(self):
        pass


print(get_method_owner(B, "m"))
print()


class A:
    pass


class B(A):
    pass


print(get_method_owner(B, "m"))
