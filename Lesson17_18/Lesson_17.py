# # Task2
# s = "Abrakadabra Babra Dabrakadabra"
# d1 = "bra"
# s = s.replace(d1, d1.upper())
# print(s)
# # Task1
# s = "Abrakadabra Babra Dabrakadabra"
# s = s.replace(" ", "")
# s = s.lower()
# print(s[::-1])
# if s == s[::-1]:
#     print("Palindrome")
#
# s1 = ""
# for i in range(1, len(s) + 1):
#     s1 = s1 + s[-i]
# if s == s1:
#     print("Palindrome")
# print(s1, s)
# print(s[:5])
#
# # Lists
# li = [1, 2, 345, 276]
# f = list()
#
# d = []
# print(li, d, f)
# user = ["Yarek", 27, 1.77, True]
# print(user)
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# for i in range(len(numbers)):
#     print(numbers[i])
#     numbers[i] = 0
#
#
# for number in numbers:
#     print(number)
#
# print(numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(len(numbers)):
    if numbers[i] == 7:
        print(f"Your number is {numbers[i]} and index is {i}")

for number in numbers:
    if number == 7:
        print(number, numbers.index(number))

user_proxy = ["127.0.0.1", "admin", "admin", 27]
print(user_proxy[0])
print(user_proxy[1])
print(user_proxy[2])
print(user_proxy[3])

user_info = ["Name", "Address", "Age", "Place of work"]
print(len(user_info))
print(user_info[0], user_info[2])

num = ["red", "Blue"]
print(0, num)
num.append("Purple")

num.insert(0, "Green")
print(2, num)
num.insert(100, "Green")
print(num)
num.pop()  # Delete from last
num.pop(0)  # Delete by index
print(3, num)
num.remove("Blue")
print(4, num)
