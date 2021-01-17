# print("Hello start program")
#
# try:
#     f = open("settings.txt", "rt")
# except FileNotFoundError:
#     print("File not found")
# except:
#     print("Error")
# else:
#     a = f.read()
#     print(a)
# finally:
#     print("Everytime running")
#
# for i in range(1, 100):
#     if i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     elif i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
# result = 0
# while True:
#     num_1 = int(input("Enter first number: "))
#     user_sign = input("Enter mathematical sign: ")
#     num_2 = int(input("Enter second number: "))
#     print(f"{num_1}{user_sign}{num_2}")
#     if user_sign == "+":
#         try:
#             result = num_1 + num_2
#             print(f"Result is: {result}")
#         except TypeError:
#             print("Type error!")
#         except ValueError:
#             print("Value error!")
#     elif user_sign == "-":
#         result = num_1 - num_2
#         print(f"Result is: {result}")
#     elif user_sign == "*":
#         result = num_1 * num_2
#         print(f"Result is: {result}")
#     elif user_sign == "/":
#         result = num_1 / num_2
#         print(f"Result is: {result}")


# a = -1
# b = -1
# count = 0
# while True:
#     with open("log.txt", "at+") as f:
#         if a == -1:
#             try:
#                 a = int(input("Enter number a: "))
#             except:
#                 print("Incorrect number: ")
#                 continue
#         if b == -1:
#             try:
#                 b = int(input("Enter number: "))
#             except:
#                 print("Incorrect number b: ")
#                 continue
#         command = input("Enter command: ")
#         try:
#             if command == "*":
#                 print(a * b)
#                 f.write(f"{a}{command}{b} = {a * b}")
#             elif command == "/":
#                 print(a / b)
#             elif command == "exit":
#                 break
#         except ZeroDivisionError:
#             print("ZeroDiv")
#         else:
#             print("OK")
#             count = count + 1
#         finally:
#             a = -1
#             b = -1

dictionary = {"Yarek": "student", "Ben": "driver"}


# while True:
#     user_key = input("Enter key to delete item: ")
#     try:
#         dictionary.pop(user_key)
#     except KeyError:
#         print("Key is not found: ")

v = " "
while v == " ":
    k = input("Enter key"
              ""
              " to delete: ")
    try:
        v = dictionary.pop(k)
    except:
        pass
    else:
        print("ok")
        print(dictionary)
