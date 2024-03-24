class Restaurant():
    def __init__(self, restaraunt_name, cuisine_type):
        self.restaurant_name = restaraunt_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"\nThe restaurant name is {self.restaurant_name}")
        print(f"The restaurant specializes in {self.cuisine_type} cuisine")
    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name} is opened!")


besh = Restaurant("Besh", "Kazakh")
bolivia = Restaurant("Bolivia", "Bolivian")
ekb = Restaurant("EKB", "Russian")

besh.describe_restaurant()
bolivia.describe_restaurant()
ekb.describe_restaurant()