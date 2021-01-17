working = True
while working:
    user_string = str(input("Enter a string: "))

    changed_user_string = user_string.lower().replace(" ", "")
    print(changed_user_string)

    inverted_string = ""
    for i in range(len(changed_user_string)):
        inverted_string = inverted_string + changed_user_string[-i - 1]
    print(inverted_string)

    if inverted_string == changed_user_string:
        print("Yes, it's palindrome")
    else:
        print("No, it is not a palindrome")

    working = not input("Please press [Enter] to continue or press Any Key to exit: ")