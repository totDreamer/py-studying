class Privileges():
    def __init__(self, user_group):
        self.user_group = user_group
        if user_group.lower() == "admin":
            self.privileges_list = ["allowed to add messages", "allowed to delete messages", "allowed to delete users",
                                    "allowed to ban users"]
        else:
            self.privileges_list = ["allowed to add messages", "allowed to delete messages"]

    def add_privileges(self, user_group):
        if user_group == "admin":
            print("You already have admin rights")
        else:
            self.user_group = user_group
            self.privileges_list = ["allowed to add messages", "allowed to delete messages", "allowed to delete users",
                                    "allowed to ban users"]
            print("You now have admin rights")


    def show_privileges(self):
        print(f"\nThe user's privileges are:")
        for privilege in self.privileges_list:
            print(f"\t- {privilege}")


class Users():
    def __init__(self, first_name, last_name, gender, age):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.privileges = Privileges("user")

    def describe_user(self):
        print(f"\nThe user's name is {self.first_name} {self.last_name}, {self.gender}, {self.age} years old"
              f"\nThe user has {self.privileges.user_group.lower()} rights")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}!\nNice to meet you.")

class Admin(Users):
    def __init__(self, first_name, last_name, gender, age):
        super().__init__(first_name, last_name, gender, age)
        self.privileges = Privileges("admin")