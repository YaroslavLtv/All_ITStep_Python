# s = "Hello World!" # итерируемыми, не изменяемими
# #    0123456789
# print(s[0])
# print(s[1])
# print(s[2])
# print(s[3])
# print(s)
#
# s = s + "Andrey"
# n = "Andrii Builuk"
# print(n[7],n[8],n[10],n[10])
# n1 = n[7]+n[8]+n[10]+n[10]
# print(n1)
# print(n[0:3])
# sw = '''The story of Knights of the Old Republic takes place almost 4,000 years before the formation of the Galactic Empire, where Darth Malak, a Dark Lord of the Sith, has unleashed a Sith armada against the Republic. The player character, as a Jedi, must venture to different planets in the galaxy to defeat Malak. Players choose from three character classes (Scout, Soldier or Scoundrel) and customize their characters at the beginning of the game, and engage in round-based combat against enemies. Through interacting with other characters and making plot decisions, players can earn Light Side and Dark Side Points, and the alignment system will determine whether the player's character aligns with the light or dark side of the Force.'''
# print(sw[-6:-1])
# print(sw[-6:])
# print(sw[:9])
# print(sw[:])
# # s = sw[:]  рассмотрим в классах, касается списков
# s = "Hello World!" # итерируемыми, не изменяемими
# #    0123456789
# #   -   987654321
# #len(sw)
# for i in range(len(sw)):
#     print(sw[i])
#
# a = "Abrakadabra"
# for i in range(len(a)):
#     if i%2!=0:
#         print(a[i])
#
# Задание 1 Пользователь вводит с клавиатуры строку. Произведите поворот строк и полученный результат выведите на экран.
s = "Abrakadabra"#str(input("Enter string : "))
for i in range(1, len(s) + 1):
     print(s[-i], end = "")
print()
print(s.count("a"))
s = "Abrakadabra"
print(s.find("a"))
print(s.rfind("a"))
sw = '''The story of Knights of the Old Republic takes place almost 4,000 years before the formation of the Galactic Empire, where Darth Malak, a Dark Lord of the Sith, has unleashed a Sith armada against the Republic. The player character, as a Jedi, must venture to different planets in the galaxy to defeat Malak. Players choose from three character classes (Scout, Soldier or Scoundrel) and customize their characters at the beginning of the game, and engage in round-based combat against enemies. Through interacting with other characters and making plot decisions, players can earn Light Side and Dark Side Points, and the alignment system will determine whether the player's character aligns with the light or dark side of the Force.'''
print(sw.find("Sith"))
print(sw.rfind("Sith"))
s = "Abrakadabra"
print(s.isalpha())
print(s.isdigit())
# Задание 2 Пользователь вводит с клавиатуры строку. Посчитайте количество букв, цифр в строке. Выведите оба количества на экран.
s = str(input("Enter word : "))
dig = 0
letter = 0
for i in range(len(s)):
    if s[i].isdigit():
        dig +=1
    elif s[i].isalpha():
        letter += 1

print(dig, letter)
a = " "
print()