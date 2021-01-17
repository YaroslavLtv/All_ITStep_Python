# s = "Hello World"
#
# for i in range(len(s)):
#     print(s[i])
#
# for letter in s:
#     print(letter)

# ASCII
# symbol = "w"
# print(ord(symbol))
# print(chr(119))
#
# symbol = "W"
# print(ord(symbol))
for i in range(899, 1050):
    print(str(i).ljust(6, "-"), str(i))

# Caesar Ciper
#     print(chr(ord(symbol)+k), end="")
#     print()
#
# print(ord("a"))
# print(ord("z"))
# print(ord(" "))
# print(ord("A"))
# print(ord("Z"))

# protostring = "Hello World!"
# codestring = ""
# encoded_string = ""
# k = 3
# for symbol in protostring:
#     code = ord(symbol)
#     if code >= ord("a") and code <= ord("z"):
#         codestring = codestring + chr(code + k)
#     elif code >= ord("A") and code <= ord("Z"):
#         codestring = codestring + chr(code + k)
#     else:
#         codestring = codestring + symbol
#
# print(protostring, codestring)
#
# for coded_symbol in codestring:
#     encoded = ord(coded_symbol)
#     if encoded - k > ord("a") or encoded - k < ord("z"):
#         encoded_string = encoded_string + chr(encoded)
#     if encoded - k > ord("A") or encoded - k < ord("Z"):
#         encoded_string = encoded_string + chr(encoded)
#     else:
#         encoded_string = encoded_string + chr(encoded - k)
# print(encoded_string)
