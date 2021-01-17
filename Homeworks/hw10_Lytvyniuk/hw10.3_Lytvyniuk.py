user_number_1 = int(input("Enter first number of range: "))
user_number_2 = int(input("Enter second number of range: "))

for i in range(user_number_1, user_number_2 + 1):
    print(f"\n{i}")
    for j in range(1, 11):
        print(f"{i} * {j} = {i * j}")