class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant_name}")
        print(f"The restaurant specializes in {self.cuisine_type} cuisine")

    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name} is opened!")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, number):
        self.number_served += number


besh = Restaurant("Besh", "Kazakh")

print(besh.number_served)
besh.number_served = 23
print(besh.number_served)
besh.set_number_served(35)
print(besh.number_served)
besh.increment_number_served(5)
print(besh.number_served)