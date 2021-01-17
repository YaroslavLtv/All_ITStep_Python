user_number_1 = int(input("Enter first number in range: "))
user_number_2 = int(input("Enter second number in range: "))

for i in range(user_number_1, user_number_2 + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("Fizz Buzz ")
    elif i % 3 == 0:
        print("Fizz ")
    elif i % 5 == 0:
        print("Buzz ")
    else:
        print(i)
