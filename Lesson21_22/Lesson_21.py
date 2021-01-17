# def sum(a, b):
#     print(a + b)
# sum(2, 2)
# sum(3, 4)
# sum(5, 6)
# sum(7, 8)
#
# def sum_1(a, b):
#     return a + b
# print(sum_1(7, 8))

# def plus(a, b):
#     return a + b
#
# def minus(a, b):
#     return a - b
#
# def mult(a, b):
#     return a * b
# def div(a, b):
#     return a / b
#
# number_1 = int(input("Enter number 1: "))
# command = str(input("Enter command: "))
# number_2 = int(input("Enter number2: "))
# if command == "+":
#     result = plus(number_1, number_2)
# if command == "-":
#     result = minus(number_1, number_2)
# if command == "*":
#     result = mult(number_1, number_2)
# if command == "/":
#     result = div(number_1, number_2)
#
# print(f"{number_1}{command}{number_2} = {result}")

# def sum_of_four(num1, num2, num3, num4):
#     summa = num1 + num2 + num3 + num4
#     return summa
# print(sum_of_four(1, 2, 3, 4))

# def sum_of_four(num1, num2, num3, num4):
#     summa = num1 + num2 + num3 + num4
#     average = summa / 4
#     return average
# print(sum_of_four(1, 2, 3, 4))

# def sum_of_four(num1, num2, num3, num4):
#     summa = num1 + num2 + num3 + num4
#     average = summa / 4
#     return average
#
# def quad_average_1(a, b, c, d):
#     summa = sum_of_four(a, b, c, d)
#     average = summa / 4
#     return average
# print(quad_average_1(1, 2, 3, 4))
# Task 1
# def format_text():
#     s = f"'Don't let the noise of other's opinions\n " \
#         f"drown out your own inner voice.'\n" \
#         f"\t\t\t\t\t\t\tSteve Jobs"
#     return s
# print(format_text())

# Task 2

# def odd(num1, num2):
#     if num1 > num2:
#         for i in range(num2, num1):
#             if i % 2 != 0:
#                 print(i)
#     else:
#         for i in range(num1, num2):
#             if i % 2 != 0:
#                 print(i)
# odd(1, 20)

# Task 3
# def line(length, direction, symbol):
#     if direction == "h":
#         for i in range(length):
#             print(f"{symbol}", end="")
#     elif direction == "v":
#         for i in range(length):
#             print(f"{symbol}")
# line(10, "h", "*")

# Task 4
# def quad_max(num1, num2, num3, num4):
#     maximum_num = 0
#     list_of_arguments = [num1, num2, num3, num4]
#     for i in range(len(list_of_arguments)):
#         if list_of_arguments[i] > maximum_num:
#             maximum_num = list_of_arguments[i]
#     return maximum_num
# print(quad_max(15, 25, 3, 10))

# Task 5 not finished
def sum_of_nums(num1, num2):
    sum_of_range = 0
    if num1 > num2:
        for i in range(num2, num1):
            sum_of_range = sum_of_range + i
        return sum_of_range
    else:
        for i in range(num1, num2):
            sum_of_range = sum_of_range + i
        return sum_of_range
print(sum_of_nums(1, 10))