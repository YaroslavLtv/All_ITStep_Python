class Car:
    # Attributes(fields)
    name = "default"
    make = "default"
    model = 2008
    price = 5000
    fuel = 5
    # Methods

    def start(self):
        self.fuel = self.fuel - 1
        print("start engine")

    def stop(self):
        print("stop engine")

    def refuel(self, volume):
        self.fuel = self.fuel + volume
        print("Refuel done!")

    def __str__(self):
        return f"name: {self.name}\nmake: {self.make}\nmodel: {self.model}\nprice: {self.price}"

    def show_name(self):
        print(self.name)

    def __init__(self, name, make, model, price, wheels):
        self.name = name
        self.make = make
        self.model = model
        self.price = price
        self.wheels = wheels


audi = Car("Q7", "Frankfurt", 2013, 20000, 18)
# audi.start()
# audi.stop()
# print(audi.make)
# audi.make = "audi"
# print(audi.make)
# print(audi.fuel)
audi.refuel(50)
print(audi.fuel)
audi.start()
audi.start()
audi.start()
audi.start()
print(audi.fuel)
audi.show_name()
print(audi)
print(audi.__dir__())
print(audi.wheels)

'''Задание 1
Реализуйте класс «Человек». Необходимо хранить в
полях класса: ФИО, дату рождения, контактный телефон,
город, страну, домашний адрес. Реализуйте методы класса
для ввода данных, вывода данных, реализуйте доступ к
отдельным полям через методы класса.'''


class Human:
    name = "no_named"
    date_of_birth = "date"
    tel = "phone_number"
    city = "city_name"
    country = "country_name"
    address = "address"
    job = "no_job"

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"name: {self.name}, phone:{self.phone}"

    def change_country(self, country):
        self.country = country

    def change_address(self, address):
        self.address = address

    def change_city(self, city):
        self.city = city


yarek = Human("Yaroslav", "+380931112233")
yarek.change_country("Ukraine")
print(yarek.country)
