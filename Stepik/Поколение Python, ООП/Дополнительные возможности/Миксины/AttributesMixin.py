class AttributesMixin:
    def get_public_attributes(self):
        return list(
            (key, value)
            for key, value in self.__dict__.items()
            if not key.startswith("_")
        )

    def get_protected_attributes(self):
        return list(
            (key, value)
            for key, value in self.__dict__.items()
            if key.startswith("_") and self.__class__.__name__ not in key
        )


class Cat(AttributesMixin):
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self._breed = breed


cat = Cat("Кемаль", 6, "Британский")
print(cat.get_public_attributes())
print(cat.get_protected_attributes())
print()


class BankAccount(AttributesMixin):
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self.__balance = balance


bank_account = BankAccount(245980, 1000)
print(bank_account.get_public_attributes())
print(bank_account.get_protected_attributes())
