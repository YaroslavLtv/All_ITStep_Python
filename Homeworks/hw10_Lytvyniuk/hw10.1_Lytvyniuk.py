user_range_first = int(input("Enter a first number in range: "))
user_range_last = int(input("Enter a last number in range: "))

for num in range(user_range_first, user_range_last + 1):
    prime_number = True
    for i in range(2, num):
        if num % i == 0:
            prime_number = False
            # print(f"{num}, {i}, {prime}, ", end="")
    if prime_number:
        if num != 1 and num != 0:
            print(num)
