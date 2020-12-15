# Create a class Vehicle. A Vehicle object will have 3 attributes:
# make
# model
# year

# A vehicle is created like this:

# car = Vehicle('Nissan', 'Leaf', 2015)

# And you can access it's attributes individually like so:

# print(car.make, car.model, car.year)
# Add a method

# Add a print_info method to the Vehicle class. It will print out the vehicle's information like so:
# >>> car.print_info()
# 2015 Nissan Leaf

class Vehicle:
    wheels = 4

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def print_info(self):
        print(f"My {self.make} {self.model} is a {self.year}")

car1 = Vehicle('Volkswagen', 'Passat', 2014)
car2 = Vehicle('BMW', '220i', 2019)

car1.print_info()
car2.print_info()