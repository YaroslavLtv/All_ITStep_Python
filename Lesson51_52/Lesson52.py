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
#         return self.__class__.__name__
#
#     def change_country(self, country):
#         self.country = country
#
#     def change_address(self, address):
#         self.address = address
#
#     def change_city(self, city):
#         self.city = city


# yarek = Human("Yaroslav", "+380931112233")
# yarek.change_country("Ukraine")
#
#
# yarek_1 = Human("Yaroslav", "+380931112233")
# yarek_1.change_country("Ukraine")
# print(Human.objects_count)
# print(yarek_1.objects_count)
# print(yarek.objects_count)


# class Sailor(Human):
#     # def __str__(self):
#     #     return self.__class__.name
#     sails = 0
#     sail_experience = 0
#
#     def sail(self):
#         self.sails += 1
#         if self.sails > 10:
#             self.sail_experience = 1
#         elif self.sails > 20:
#             self.sail_experience = 2
#
#
# class Builder(Human):
#     # def __str__(self):
#     #     return self.__class__.name
#     buildings = 0
#     build_experience = 0
#
#     def build(self):
#         self.buildings += 1
#         if self.buildings > 10:
#             self.build_experience = 1
#         elif self.buildings > 20:
#             self.build_experience = 2
#
#
# class Pilot(Human):
#     # def __str__(self):
#     #     return self.__class__.name
#     flights = 0
#     flight_experience = 0
#
#     def flight(self):
#         self.flights += 1
#         if self.flights > 10:
#             self.flight_experience = 1
#         elif self.flights > 20:
#             self.flight_experience = 2
#
#
# h = Human("Yaroslav", "12345")
# b = Builder("Yaroslav", "12345")
# s = Sailor("Yaroslav", "12345")
# p = Pilot("Yaroslav", "12345")
#
# print(b.build_experience, s.sail_experience, p.flight_experience)
#
#
# class SeaBuilder(Builder, Sailor):
#     pass
#
#
# sb = SeaBuilder("Yaroslav", "123455")
# sb.build()
# sb.sail()
# sb.build()
# sb.sail()
# print(sb.buildings, sb.sails)

class Passport:
    _first_name = ""
    _last_name = ""
    date_of_birth = ""
    __id = 1

    def __init__(self, user_first_name, user_last_name):
        Passport.__id += 1
        self._first_name = user_first_name
        self._last_name = user_last_name
        self.__id = Passport.__id

    def __str__(self):
        return f"ID: {self.__id}, {Passport.__id}"


# passport_1 = Passport("Yaroslav", "Lytvyniuk")
# print(passport_1.__id)


class ForeignPassport(Passport):
    visas = 0  # public

    @staticmethod
    def travel(travels):
        ForeignPassport.visas += travels

    def change_id(self, new_id):
        self.__id = new_id

    def show_id(self):
        print(self.__id)



# some_foreign = ForeignPassport("Yaroslav", "Lytvynyuk")
# # print(some_foreign.__id)
# some_foreign.travel(2)
# some_foreign.travel(1)
# some_foreign_2 = ForeignPassport("Jenny", "Lytvyniuk")
# some_foreign_3 = ForeignPassport("Jenny", "Lytvyniuk")
# print(some_foreign.visas)
# print(some_foreign)
# print(passport_1)
# print(some_foreign_2)
# print(some_foreign_3)
# some_foreign.change_id(132)
# print(some_foreign)
# some_foreign.show_id()
# public        data
# protected     _data
# private       __data
p = Passport("Yarek", "Ltv")
p_1 = Passport("Yarek", "Ltv")
print(p)
print(p_1)

f_1 = ForeignPassport("Yarek", "Ltv")
f_1.change_id(123)
f_2 = ForeignPassport("Yarek", "Ltv")
print(f"foreign_1: {f_1}")
f_1.show_id()
print(f_1.__dir__())
print()
print(f_2)
f_3 = ForeignPassport("Yarek", "Ltv")
print(f_3)
print(p)