class Car:
    model = "default_model"
    year = 0
    manufacturer = "default_manufacturer"
    engine_capacity = "default_capacity"
    color = "default_color"
    price = 0
    count_of_cars = 0
    prefix = "_000"

    @staticmethod
    def change_prefix(new_prefix):
        Car.prefix = new_prefix

    def __init__(self, model, year, manufacturer):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        Car.count_of_cars += 1
        self.vin = self.manufacturer + self.prefix + str(Car.count_of_cars)

    def input_capacity(self, engine_capacity):
        self.engine_capacity = engine_capacity

    def input_color(self, color_of_car):
        self.color = color_of_car

    def input_price(self, price_of_car):
        self.price = price_of_car

    def show_info(self):
        print(f"Manufacturer: {self.manufacturer}\nModel: {self.model}\nYear of manufacture: {self.year}")
        print(f"Engine capacity: {self.engine_capacity}\nColor: {self.color}\nPrice: {self.price}\nVin: {self.vin}")


audi = Car("A4", 2009, "Audi")
mercedes = Car("C220", 2013, "Mercedes")
vw = Car("Passat", 2016, "VolksWagen")
audi.input_color("Grey")
audi.input_capacity(2.0)
audi.input_price(9500)
mercedes.input_color("Black")
mercedes.input_capacity(2.2)
mercedes.input_price(12000)
vw.input_color("Red")
vw.input_capacity(2.0)
vw.input_price(15000)
audi.show_info()
mercedes.show_info()
vw.show_info()
Car.change_prefix("_001")
porsche = Car("911GT", 2016, "Porsche")
porsche.show_info()
audi.show_info()
