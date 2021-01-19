# class Human:
#     name = "no_named"
#     date_of_birth = "date"
#     tel = "phone_number"
#     city = "city_name"
#     country = "country_name"
#     address = "address"
#     job = "no_job"
#     objects_count = 0
#
#     def __init__(self, name, phone):
#         self.name = name
#         self.phone = phone
#         Human.count_of_objects()
#
#     @staticmethod
#     def count_of_objects():
#         Human.objects_count += 1
#
#     def __str__(self):
#         return f"name: {self.name}, phone:{self.phone}"
#
#     def change_country(self, country):
#         self.country = country
#
#     def change_address(self, address):
#         self.address = address
#
#     def change_city(self, city):
#         self.city = city
#
#
# yarek = Human("Yaroslav", "+380931112233")
# yarek.change_country("Ukraine")
#
#
# yarek_1 = Human("Yaroslav", "+380931112233")
# yarek_1.change_country("Ukraine")
# print(Human.objects_count)
# print(yarek_1.objects_count)
# print(yarek.objects_count)

# class Figure:
#     count_of_work = 0
#     count_of_side = 0
#     length_of_side = 0
#     degree = 0
#     type_of_figure = "square"  # triangle, rectangle, rombus
#
#     @staticmethod
#     def count_work():
#         Figure.count_of_work += 1
#
#     @staticmethod
#     def show_count_work():
#         return Figure.count_of_work
#
#     def __init__(self, type_of_figure, a, b):
#         self.type_of_figure = type_of_figure
#         self.a = a
#         self.b = b
#
#     def square(self):
#         Figure.count_work()
#         print(self.a * self.b)
#
#
# s1 = Figure("square", 4, 4)
# s1.square()
# print(Figure.show_count_work())
#
# s2 = Figure("square_2", 4, 3)
# s2.square()
# print(Figure.show_count_work())

class Human:
    name = "no_named"
    date_of_birth = "date"
    tel = "phone_number"
    city = "city_name"
    country = "country_name"
    address = "address"
    job = "no_job"
    objects_count = 0

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        Human.count_of_objects()

    @staticmethod
    def count_of_objects():
        Human.objects_count += 1

    def __str__(self):
        return self.__class__.__name__

    def change_country(self, country):
        self.country = country

    def change_address(self, address):
        self.address = address

    def change_city(self, city):
        self.city = city


yarek = Human("Yaroslav", "+380931112233")
yarek.change_country("Ukraine")


yarek_1 = Human("Yaroslav", "+380931112233")
yarek_1.change_country("Ukraine")
print(Human.objects_count)
print(yarek_1.objects_count)
print(yarek.objects_count)


class Seller(Human):
    # def __str__(self):
    #     return self.__class__.name
    pass


class Builder(Human):
    # def __str__(self):
    #     return self.__class__.name
    pass


class Pilot(Human):
    # def __str__(self):
    #     return self.__class__.name
    pass


h = Human("Yaroslav", "12345")
b = Builder("Yaroslav", "12345")
s = Seller("Yaroslav", "12345")
p = Pilot("Yaroslav", "12345")

print(h, b, s, p)