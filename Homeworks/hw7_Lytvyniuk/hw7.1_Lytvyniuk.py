
user_number_1 = int(input("Enter first number in range: "))
user_number_2 = int(input("Enter second number in range: "))

print(f"numbers divided without reminder by the number 7 in range from {user_number_1} to {user_number_2}: ")
for i in range(user_number_1, user_number_2 + 1):
    if i % 7 == 0:
        print(i)
