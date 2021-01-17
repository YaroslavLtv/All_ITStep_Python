user_number = 0
max_number = 0
min_number = 0
sum_of_numbers = 0

while user_number != 7:
    user_number = int(input("Enter a number: "))
    sum_of_numbers += user_number

    if user_number != 7:
        if sum_of_numbers == user_number:
            max_number = user_number
            min_number = user_number

        if user_number > max_number:
            max_number = user_number

        if user_number < min_number:
            min_number = user_number
        print(f"sum of entered number is: {sum_of_numbers}, "
              f"maximum of entered number is {max_number}, "
              f"minimum of entered number is: {min_number}")
    else:
        print("Good bye!")
