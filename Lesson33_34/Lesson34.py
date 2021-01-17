# l = [1, 2, 1, 3, 4, 5, 6, 6, 7]
# my_set = set(l)
# print(my_set)
# print(list(my_set))
# my_set_2 = {1, 2, 333, 4, 5, 6}
# print(type(my_set_2))
# print(my_set_2)
#
# my_set_2.add(444)
# print(my_set_2)
# my_set_2.remove(333)
# print(my_set_2)
# my_set_2.discard(334)
# print(my_set_2)
#
# my_set_3 = {1, 2, 3, 4}
# my_set_4 = {1, 2, 4, 5}
#
# #Объединение
# s1 = {1,2,3,4}
# s2 = {1,2,4,5}
# s1 |= s2
# print(s1)
# s1 = {1,2,3,4}
# s2 = {1,2,4,5}
# s3 = s1 | s2
# print(s3)
#
# #Пересечение
# s1 = {1,2,3,4}
# s2 = {1,2,4,5}
# s1 &= s2 #  s1.intersection_update(s2)
# print(s1)
# s1 = {1,2,3,4}
# s2 = {1,2,4,5}
# s3 = s1 & s2
# print(s3)
#
# #Вычитание
# s1 = {1,2,3,4}
# s2 = {1,2,4,5}
# s1 -= s2
# print(s1)
# s1 = {1,2,3,4}
# s2 = {1,2,4,5}
# s3 = s1 - s2
# print(s3)
#
# #Симметричное сложение
# s1 = {1,2,3,4}
# s2 = {1,2,4,5}
# s1 ^= s2
# print(s1)
# print(s1.symmetric_difference(s2))  # Те саме що і вище
# s1 = {1,2,3,4}
# s2 = {1,2,4,5}
# s3 = s1 ^ s2
# print(s3)
#
# s1 = {1, 2, 3, 4, 5}
# s2 = {1, 2, 4, 5}
# print(s1 == s2)
# print(s1 >= s2)
# print(s1 <= s2)

# lfs = [1, 2, 3, 4, 5, 6, 7, 7, 7, 8]
# lfs = frozenset(lfs)
# print(lfs)
#
# countries = set()
# countries = {'USA', 'GB', 'SAR'}
# command = ""
# while True:
#     command = str(input("Enter command: "))
#     if command == "add":
#         country = str(input("Enter country: "))
#         countries.add(country)
#     elif command == "del":
#         country = str(input("Enter country: "))
#         countries.discard(country)
#     elif command == "find":
#         country_symbols = str(input("Enter country: "))
#         for country in countries:
#             if country_symbols in country:
#                 print("YES")
#     elif command == "find_all":
#         country_1 = str(input("Enter country: "))
#         for country in countries:
#             if country in country_1:
#                 print("YES")

# set_of_cities_1 = {'Kyiv', 'Warsaw', 'Berlin'}
# set_of_cities_2 = {'Kyiv', 'Gdansk', 'Munich'}
#
# set_of_cities_1 &= set_of_cities_2
# print(set_of_cities_1)

# set_of_cities_1 = {'Kyiv', 'Warsaw', 'Berlin'}
# set_of_cities_2 = {'Kyiv', 'Gdansk', 'Munich'}
# set_of_cities_3 = set_of_cities_1 - set_of_cities_2
# print(set_of_cities_3)

# fourth
# set_of_cities_1 = {'Kyiv', 'Warsaw', 'Berlin'}
# set_of_cities_2 = {'Kyiv', 'Gdansk', 'Munich'}
# set_of_cities_3 = set_of_cities_2 - set_of_cities_1
# print(set_of_cities_3)

# fifth
# set_of_cities_1 = {'Kyiv', 'Warsaw', 'Berlin'}
# set_of_cities_2 = {'Kyiv', 'Gdansk', 'Munich'}
# set_of_cities_3 = set_of_cities_1 ^ set_of_cities_2
# print(set_of_cities_3)

countries = {'Ukraine': 'Kyiv', 'Poland': 'Warsaw'}
in_country = input("Enter country name: ")
change_city = input("Enter a new name of city: ")
command = ""

while True:
    command = str(input("Enter command: "))
    for country in countries:
        if in_country == country:
            countries[country] = change_city
    print(countries)
