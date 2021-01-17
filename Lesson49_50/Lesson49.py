import time


class Car:
    count_of_cars = 0
    engine = "gas"  # fields of class
    color = "red"

    @staticmethod  # Переназначає поля класа через метод
    # (тобто всі об'єкти класу (нові і старі) переініціалізуються і приймуть нові значення полів через метод)
    def change_engine(engine):
        Car.engine = engine

    def start(self):
        print("Start engine")
        self.mileage += 10

    def __init__(self, user, price):  # Constructor-method
        self.price = price  # fields of object of class
        self.user = user
        # всі об'єкти класу (нові і старі) переініціалізуються і приймуть нові значення полів
        Car.count_of_cars = Car.count_of_cars + 1
        # vin код залишиться індивідуальним для кожного створеного об'єкту класа Car
        self.vin = Car.count_of_cars
        self.mileage = 0
        self.date = time.time()  # Показує в який час були створені об'єкти класа Car (тобто під час ініціалізації)

    def __str__(self):
        return f"{self.user}"


audi = Car("Yaroslaw", 12000)  # Class example(object of class Car)
time.sleep(0.5)
bmw = Car("Sten", 13000)
time.sleep(0.5)
citroen = Car("Ben", 10000)

print(audi.price)
print(dir(audi))
print(audi.engine)
print(bmw.engine)
# audi.engine = "diesel"
Car.engine = "electric"
print(audi.engine)
print(bmw.engine)
print(audi.engine)
print(bmw.engine)
print(Car.count_of_cars)
print(citroen.count_of_cars)
print(citroen.vin)
print(audi.vin)

print(citroen.engine)
Car.change_engine("Electric")
daewoo = Car("Glen", 2500)
print(daewoo.vin)
print(bmw.vin)
print(audi.vin)

print(citroen.engine)

print(citroen)
audi.start()
audi.start()
bmw.start()

print(audi.mileage, bmw.mileage, citroen.mileage)
print(f"{audi.date}\n{bmw.date}\n{citroen.date}")
