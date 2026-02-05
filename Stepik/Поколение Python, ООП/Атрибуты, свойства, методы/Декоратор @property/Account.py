class Account:
    def __init__(self, login, password):
        self._login = login
        self.password = password

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, login):
        raise AttributeError("Изменение логина невозможно")

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = self.hash_function(password)

    def hash_function(self, password):
        hash_value = 0
        for char, index in zip(password, range(len(password))):
            hash_value += ord(char) * index
        return hash_value % 10**9


account = Account("hannymad", "cakeisalie")

print(account.login)
print(account.password)


account = Account("timyr-guev", "lovebeegeek")

print(account.password)
account.password = "verylovebeegeek"
print(account.password)


account = Account("timyr-guev", "lovebeegeek")
try:
    account.login = "timyrik30"
except AttributeError as e:
    print(e)
