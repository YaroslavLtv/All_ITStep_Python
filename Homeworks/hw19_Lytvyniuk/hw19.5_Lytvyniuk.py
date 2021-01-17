import random
length_of_list = int(input("Enter a length of lists: "))
minimum_num_in_list = int(input("Enter a minimum number in random lists: "))
maximum_num_in_list = int(input("Enter a maximum number in random lists: "))


def random_lists(min_num, max_num, length):
    my_list_1 = []
    my_list_2 = []
    for i in range(length):
        my_list_1.append(random.randint(min_num, max_num))
        my_list_2.append(random.randint(min_num, max_num))
    print(f"Here is two random generated lists:\n1-st: {my_list_1}\n2-nd: {my_list_2}")
    return my_list_1, my_list_2


def concat_lists(user_lists):
    new_list = user_lists[0][:] + user_lists[1][:]
    return new_list


print(f"Here is elements of two "
      f"random lists:\n{concat_lists(random_lists(minimum_num_in_list, maximum_num_in_list, length_of_list))}")
