filling = True
list_of_nums = []
while filling:
    filling = input("Enter a number to fill in the list or press Enter to continue: ")
    if filling != "":
        list_of_nums.append(int(filling))
        print(list_of_nums)
    elif filling == "":
        filling = False


def prime_numbers(user_list):
    quantity_of_primes = 0
    primes = []
    for num in user_list:
        prime_number = True
        for i in range(2, num):
            if num % i == 0:
                prime_number = False
        if prime_number:
            if num != 1 and num != 0:
                primes.append(num)
                quantity_of_primes += 1
    print(f"Quantity of prime numbers in the list: {quantity_of_primes}")
    return primes


print(f"The prime numbers in the list is: {prime_numbers(list_of_nums)}")
