class ProtectedObject:
    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            object.__setattr__(self, name, value)

    def __getattribute__(self, name):
        if name.startswith("_"):
            raise AttributeError("Доступ к защищенному атрибуту невозможен")
        return object.__getattribute__(self, name)

    def __setattr__(self, name, value):
        if name.startswith("_"):
            raise AttributeError("Доступ к защищенному атрибуту невозможен")
        object.__setattr__(self, name, value)

    def __delattr__(self, name):
        if name.startswith("_"):
            raise AttributeError("Доступ к защищенному атрибуту невозможен")
        object.__delattr__(self, name)


user = ProtectedObject(login="PG_kamiya", _password="alreadybanned")

try:
    print(user.login)
    print(user._password)
except AttributeError as e:
    print(e)
