# Задание 3 Пользователь вводит с клавиатуры строку и символ для поиска. Посчитайте сколько раз в строке встречается искомый символ. Полученное число выведите на экран.
symbol = 'a'
s = 'Abrakadabra'
print(s.count(symbol))
sum = 0
for i in range(len(s)):
    if s[i] == symbol:
        sum += 1
print(symbol, sum)
# Задание 4 Пользователь вводит с клавиатуры строку и слово для поиска. Посчитайте сколько раз в строке встречается искомое слово. Полученное число выведите на экран.
word = 'bra'
s = 'Abrakadabra'
print(s.count(word))
sum = 0
l = len(word)
for i in range(len(s)):
    if s[i:i+l] == word:
        sum += 1
print(word, sum)
# Пользователь вводит с клавиатуры строку, слово для поиска, слово для замены. Произведите в строке замену одного слова на другое. Полученную строку отобразите на экране.
s = "Abrakadabra"
word = "bra"
b = "xxx"#xxxxx
l = len(word)
for i in range(len(s)):
    if s[i:i+l] == word:
        pre = s[:i]
        post = s[i+l:]
        s = pre + b + post
print(s)
s = "Abrakadabra"
word = "bra"
b = "xxx"
print(s.replace(word,b))#более корректный
print("Abrakadabra".replace("bra","xxx"))
print(s)

#Password checker
password = "AS12qW34"
difficult = 0
uletter = 0
lletter = 0
digit = 0
if len(password) >= 8:
    difficult += 1
for i in range(len(password)):
    if password[i].isupper() and uletter != 1:
        uletter += 1
        difficult += 1
    elif password[i].islower() and lletter != 1:#islower
        lletter += 1
        difficult += 1
    elif password[i].isdigit() and digit != 1:
        digit += 1
        difficult += 1

if difficult <= 1:
    print("Easy")
elif difficult <= 2:
    print("Normal")
elif difficult <= 3:
    print("Good")
elif difficult <= 4:
    print("Strong")

#Good Bye

maximum = 0
minimum = 100
while True:
    num = int(input("Enter num : "))
    if num == 7:
        print("Good bye")
        break
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num

print(maximum,minimum)