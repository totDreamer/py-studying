class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"\nThe restaurant name is {self.restaurant_name}")
        print(f"The restaurant specializes in {self.cuisine_type} cuisine")

    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name} is opened!")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def append_icecream(self, icecream_list):
        self.flavors.extend(icecream_list)

    def describe_restaurant(self):
        print(f"\nThe Icecream Stand name is {self.restaurant_name}")

    def show_menu(self):
        print("Currently the following types of ice cream are available:")
        for flavor in self.flavors:
            print("\t" + flavor.title())


my_icecream_stand = IceCreamStand("ICELAND", "Icecream Stand")
my_icecream_stand.append_icecream(["Classic", "Chocolate", "Peanut"])
my_icecream_stand.describe_restaurant()
my_icecream_stand.show_menu()
