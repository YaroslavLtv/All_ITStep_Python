# '''Есть три кортежа целых чисел необходимо найти элементы, которые уникальны для каждого списка.'''
# a = (1, 2, 4)
# b = (1, 3, 5)
# c = (1, 2, 6)
# # 4, 3, 5, 6
#
# l = [1, 1, 2, 3, 5, 8]
# print(l[l[4]])
#
# def user_login(name=input("Enter your name: ")):
#     if name == "Yaroslav":
#         print("Hello")

# Files
# s = "Hello World"
# s.replace("W", "w")
# f = open("test.txt", "rt")
# print(f.read())
# f.close()

# r - read можливість зчитування, якщо ні, - то помилка

# w - write можливість запису, якщо файл існує, його вміст буде перезаписано,
# якщо не існує такий файл, Python його створить

# a - append можливість запису, якщо файл існує, його допише

# x - xwrite можливість запису, створення нових файлів якщо не існує, якщо існує - помилка

# + - відкривання на читання і запис

# t - працювати як з текстом
# b - працювати з бінарними даними

# f = open("test.txt", "wt")
# f.write("Hello Yarek")
#
# f.close()
#
# f = open("test.txt", "at")
# f.write(", Hello my frend")
#
# f.close()

# f = open("test.txt", "xt")
# f.write(", Hello my XXX")
#
# f.close()

# f = open("test.txt", "rt+")
# f.write(", Hello my XXX")
#
# f.close()

f = open("test.txt", "rb+")
print(f.read())
f.close()

