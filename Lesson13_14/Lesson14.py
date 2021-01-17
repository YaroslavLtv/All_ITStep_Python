# symbol = "a"
# s = "Abrakadabra"
# print(s.count(symbol))
# count = 0
#
# for i in range(len(s)):
#     if s[i] == symbol:
#         count += 1
# print(f"{symbol} {count}")

# word = "bra"
# s = "Abrakadabra"
#
# print(s.count(word))
#
# sum = 0
# l = len(word)
#
# for i in range(len(s)):
#     if s[i:i+l] == word:
#         sum += 1
# print(word, sum)

s = "Abrakadabra"
word = "bra"
b = "xxxx"

sum = 0
l = len(word)

for i in range(len(s)):
    if s[i:i+l] == word:
        pre = s[:i]
        post = s[i+l:]
        s = pre + b + post
print(s)

s = "Abrakadabra"
word = "bra"
b = "xxxx"

print(s.replace(word, b))

# Password checker
# password = "AS12QW34"
# difficult = 0
# letter = 0
# digit = 0
#
# if len(password) >= 8:
#     difficult += 1
#
# for i in range(len(password)):
#     if password[i].isalpha() and letter != 1:
#         difficult += 1
#         letter += 1
#         if password[i].isupper():
#             difficult += 1
#         if password[i].islower():
#             difficult += 1
#
#     elif password[i].isdigit() and digit != 1:
#         digit += 1
#         difficult += 1
# if difficult <= 1:
#     print("Easy")
# elif difficult <= 2:
#     print("Normal")
# elif
