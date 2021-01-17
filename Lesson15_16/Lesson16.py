text = '''
Пользоват2ель с клавиатуры вводит элементы списка
целых и некото1рое число. необходимо посчитать сколько р3аз данное число присутствует в сп7иске. Результат
выве5сти на экран.
'''
# text1 = ""
# for i in range(len(text)):
#     if i == 0 or (text[i - 2] == '.' and text[i - 1] == " "):
#         text1 = text1 + text[i].upper()
#     else:
#         text1 = text1 + text[i]
# print(text1)

is_digit = 0
for i in range(len(text)):
    if text[i].isdigit():
        is_digit += 1
print(is_digit)

symbols = 0
for letter in text:
    # if letter == "." or letter == "," or letter == ":" or letter == ";":
    if letter in ".,:;":
        symbols += 1
print(symbols)

login = "admin"
password = "admin123"
if login in password:
    print("Not Secure")
