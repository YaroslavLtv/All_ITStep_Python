user_number = 0

while user_number != 7:
    user_number = int(input("Enter a number: "))
    if user_number > 0 and user_number != 7:
        print("Number is positive")
    elif user_number < 0:
        print("Number is negative")
    elif user_number == 0:
        print("Number is equal to zero")
    elif user_number == 7:
        print("Number is positive")
        print("Good bye!")
