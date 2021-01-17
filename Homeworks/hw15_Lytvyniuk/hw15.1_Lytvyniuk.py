calc = True

while calc:
    num_1 = 0
    num_2 = 0
    result = 0
    user_string = input("Enter your mathematical expression or print [e] to exit: ")

    for symbol in user_string:
        if symbol == "+":
            num_1 = float(user_string[:user_string.index(symbol)])
            num_2 = float(user_string[user_string.index(symbol) + 1:])
            result = num_1 + num_2
            print(f"{user_string} = {result}")
        elif symbol == "-":
            num_1 = float(user_string[:user_string.index(symbol)])
            num_2 = float(user_string[user_string.index(symbol) + 1:])
            result = num_1 - num_2
            print(f"{user_string} = {result}")
        elif symbol == "*":
            num_1 = float(user_string[:user_string.index(symbol)])
            num_2 = float(user_string[user_string.index(symbol) + 1:])
            result = num_1 * num_2
            print(f"{user_string} = {result}")
        elif symbol == "/":
            num_1 = float(user_string[:user_string.index(symbol)])
            num_2 = float(user_string[user_string.index(symbol) + 1:])
            if num_2 != 0:
                result = num_1 / num_2
                print(f"{user_string} = {result}")
        elif user_string == "e":
            calc = False


