class Car:
    model = "default_model"
    year = 0
    manufacturer = "default_manufacturer"
    engine_capacity = "default_capacity"
    color = "default_color"
    price = 0

    def __init__(self, model, year, manufacturer):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer

    def input_capacity(self, engine_capacity):
        self.engine_capacity = engine_capacity

    def input_color(self, color):
        self.color = color

    def input_price(self, price):
        self.price = price

    def show_info(self):
        print(f"Manufacturer: {self.manufacturer}\nModel: {self.model}\nYear of manufacture: {self.year}")
        print(f"Engine capacity: {self.engine_capacity}\nColor: {self.color}\nPrice: {self.price}")


make = input("Enter a manufacturer of car: ")
year_of_manufacture = int(input("Enter a year of manufacture: "))
model = input("Enter a model of car: ")

new_car = Car(model, year_of_manufacture, make)

edit = True
while edit:
    edit = input("To change car parameters type:\n[ca] - edit engine capacity\n"
                 "[co] - edit color\n"
                 "[pr] - change price\n"
                 "\tTo see info about car:\n\t[i] - info\n"
                 "or press [Enter] to exit: ")
    if edit == "ca":
        capacity = float(input("Enter engine capacity: "))
        new_car.engine_capacity = capacity
    elif edit == "co":
        color = input("Enter color of a car: ")
        new_car.color = color
    elif edit == "pr":
        price = int(input("Enter price of a car: "))
        new_car.price = price
    elif edit == "i":
        new_car.show_info()

