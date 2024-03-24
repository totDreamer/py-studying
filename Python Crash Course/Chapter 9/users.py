class Users():
    def __init__(self, first_name, last_name, gender, age):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age

    def describe_user(self):
        print(f"\nThe user's name is {self.first_name} {self.last_name}, {self.gender}, {self.age} years old")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}!\nNice to meet you.")


mikhail = Users("Mikhail", "Bekker", "male", "24")
helga = Users("Helga", "Bekker", "female", "24")

mikhail.describe_user()
mikhail.greet_user()
helga.describe_user()
helga.greet_user()