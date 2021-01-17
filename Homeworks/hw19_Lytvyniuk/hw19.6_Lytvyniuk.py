import random
length_of_list = int(input("Enter a length of list: "))
minimum_num_in_list = int(input("Enter a minimum number in random list: "))
maximum_num_in_list = int(input("Enter a maximum number in random list: "))
user_power = int(input("Enter a power for each item in random generated list: "))


def random_list(min_num, max_num, length):
    my_list = []
    for i in range(length):
        my_list.append(random.randint(min_num, max_num))
    print(f"Here is random generated list:\n{my_list}")
    return my_list


def my_pow(user_list, power):
    pow_list = []
    for i in range(len(user_list)):
        powered_num = 1
        for j in range(1, power + 1):
            powered_num = user_list[i] * powered_num
        pow_list.append(powered_num)
    print(f"The list with powered items: {pow_list}")
    return pow_list


my_test_list = random_list(minimum_num_in_list, maximum_num_in_list, length_of_list)
my_pow(my_test_list, user_power)
