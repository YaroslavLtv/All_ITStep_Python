# print(f"5 > 2 {5 > 2}")
# print(f"5 < 2 {5 < 2}")
# print(f"5 >= 5 {5 >= 5}")
# print(f"5 > 5 {5 > 5}")
# print(f"5 <= 2 {5 <= 2}")
# print(f"5 != 2 {5 != 2}")
# print(f"5 == 2 {5 == 2}")
# print(f"5 != 5 {5 != 5}")
# print(f"5 == '5' {5 == '5'}")
# a = 7
# b = 3
# print(f"{a} != {b} {a != b}")
#
# # if a > b:
# #     print(a)
# #
# # if bool(input("Enter something: ")):
# #     print(a)
#
# name = "Admin"
# password = "Admin"
# user_name = input("Enter your login: ")
# user_password = input("Enter your password: ")
#
# if name == user_name:
#     print("Success")
# else:
#     print("Wrong")
#
# if password == user_password:
#     print("Success")

# age = -10
# if age < 0:
#     print("Error -")
# elif age < 13:
#     print("You are child")
# elif age < 18:
#     print("You are teen")
# elif age < 135:
#     print("You are an adult")
# else:
#     print("Error +")


# height = int(input("Enter your height: "))
# if height <= 0:
#     print("Liar")
# elif height <= 100:
#     print("You are little baby")
# elif height <= 150:
#     print("You are teenager")
# elif height <= 180:
#     print("You are adult and middle height")
# elif height <= 200:
#     print("You are toll")
# else:
#     print("wrong input")

# user_type = "Buyer"
# user_form = "Privat"
#
# if user_type == "Buyer":
#     if user_form == "Privat":
#         print("Your tax is 5%")
#     elif user_form == "Company":
#         print("Your tax is 10%")
# elif user_type == "Seller":
#     if user_form == "Privat":
#             print("Your tax is 2%")
#     elif user_form == "Company":
#             print("Your tax is 4%")

# gender = int(input("Enter your gender: 1 = Male, 2 = Female: "))
# age = int(input("Enter your age: "))
#
# if gender == 1:
#     if age <= 0:
#         print("Wrong input")
#     elif age <= 9:
#         print("You are little boy")
#     elif age <= 17:
#         print("You are boy")
#     elif age <= 60:
#         print("You are adult man")
# elif gender == 2:
#     if age <= 0:
#         print("Wrong input")
#     elif age <= 9:
#         print("You are little girl")
#     elif age <= 17:
#         print("You are girl")
#     elif age <= 60:
#         print("You are adult women")

# x = -5
# y = 2
#
# if x == 0 or y == 0:
#     if x == 0 and y == 0:
#         print("Point Zero")
#     elif x == 0 and y > 0:
#         print("Y +")
#     elif x == 0 and y < 0:
#         print("Y -")
#     elif y == 0 and x > 0:
#         print("X +")
#     elif y == 0 and x < 0:
#         print("X -")
# elif x > 0:
#     if y > 0:
#         print("I")
#     elif y < 0:
#         print("IV")
# elif x < 0:
#     if y > 0:
#         print("II")
#     elif y < 0:
#         print("III")


login = input("Enter login: ")
password = input("Enter password: ")

if login == "admin" and password == "admin":
    print("Access gran"
          "ted")
elif not login or not password:
    print("wrong value")
else:
    print("Login or Password is wrong, try again")
