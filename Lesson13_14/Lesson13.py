# s = "Hello World!"  # Ітеруємі і незмінні
# print(s[0])
# print(s[1])
# print(s[2])
# print(s[3])
# print(s)
#
# n = "Yaroslav Lytvyniuk"
# print(f"{n[0]}{n[3]}{n[16]}")
# print(f"{n[2]}{n[3]}{n[10]}{n[1]}{n[5]}{n[4]}")
# print(f"{n[5]}{n[1]}{n[7]}{n[1]}")
#
# print(n[0:3])
# print(n[-7:])
# print(n[:9])
# print(n[:])
# print(len(n))
#
# for i in range(len(n)):
#     print(n[i])
#
# a = "Abrakadabra"
#
# for i in range(len(a)):
#     if i % 2 == 0:
#         print(a[i])

s = "Abrakadabra"  # str(input("Enter string: "))
#
# for i in range(1, len(s) + 1):
#     print(s[-i], end="")

print(s.count("a"))
print(s.find("a"))
print(s.rfind("a"))
print(s.find("akad"))

print(s.isalpha())
print(s.isdigit())

s = "1234Abrakadabra1234_55"
alpha = 0
number = 0


for i in range(len(s)):
    if s[i].isalpha():
        alpha += 1
    elif s[i].isdigit():
        number += 1
print(f"{alpha}  {number}")


