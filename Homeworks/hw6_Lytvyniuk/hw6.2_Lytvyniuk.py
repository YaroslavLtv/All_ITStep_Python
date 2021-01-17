num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))
num_3 = int(input("Enter third number: "))

if num_1 == num_2 and num_1 == num_3:
    print(f"The answer is: 3 equal numbers")
elif num_1 == num_2 or num_1 == num_3 or num_2 == num_3:
    print(f"The answer is: 2 equal numbers")
else:
    print(f"The answer is: 0 equal numbers")