def random_password(length, letter=True, number=True, special_sym=True):
    import random
    letter_list = "abcdefghijklmn"
    number_list = "0123456789"
    symbol_list = "!@#$%^&"
    p = ""
    for i in range(length):
        b = random.randint(0, 2)
        if b == 2:
            if letter:
                a = random.randint(0, len(letter_list) - 1)
                p = p + letter_list[a]
        elif b:
            if number:
                a = random.randint(0, len(number_list) - 1)
                p = p + number_list[a]
        else:
            if special_sym:
                a = random.randint(0, len(symbol_list)-1)
                p = p + symbol_list[a]
    return p

# print(random_password(10))
#
# list_of_passwords = []
# for i in range(20):
#     list_of_passwords.append(random_password(10))
# print(list_of_passwords)


def pass_list_builder(quantity, length=15):
    list_of_passwords = []
    for i in range(quantity):
        list_of_passwords.append(random_password(length))
    return list_of_passwords


print(pass_list_builder(5, 20))
