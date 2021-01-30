# class Car:
#     wheels = 4
#     engine = 'gas'
#     fuel = 0
#     fuel_limit = 300
#
#     def __init__(self,engine):
#         self.engine = engine
#
#     def set_max_speed(self):
#         if self.engine == 'gas':
#             self.max_speed = 120
#         elif self.engine == 'diesel':
#             self.max_speed = 100
#         else:
#             self.engine = 'gas'
#
#     def set_fuel(self,fuel_count):
#         if self.fuel >= self.fuel_limit:
#             return "Перелив"
#         self.fuel = fuel_count + self.fuel
#         return self.fuel
#
#
# sedun = Car('gas')
# sedun.set_max_speed()
# truck = Car('diesel')
# truck.set_max_speed()
# print(sedun.max_speed)
# print(truck.max_speed)
# print(sedun.set_fuel(100))
# print(sedun.set_fuel(100))
# print(sedun.set_fuel(100))
# print(sedun.set_fuel(100))
# print(sedun.set_fuel(100))
# print(sedun.fuel_limit)

class User:
    __id = 0
    __count_of_users = 0
    name = "default"
    password = "default"

    def __init__(self, name, password):
        self.name = name
        self.password = password
        User.change_count_of_users()
        self.set_user_id()

    def __str__(self):
        return f"Name: {self.name}\n" \
               f"Password: {self.password}\n" \
               f"Count: {User.__count_of_users}\n" \
               f"ID: {self.__id}"

    @staticmethod
    def change_count_of_users():
        User.__count_of_users = User.__count_of_users + 1

    def set_user_id(self):
        self.__id = User.__count_of_users


admin = User("admin", "password")
print("admin")
yaroslav = User("yaroslav", "password")
print(yaroslav)