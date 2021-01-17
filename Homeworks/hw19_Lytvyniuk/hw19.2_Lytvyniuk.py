filling = True
list_of_nums = []
while filling:
    filling = input("Enter a number to fill in the list or press Enter to continue: ")
    if filling != "":
        list_of_nums.append(filling)
        print(list_of_nums)
    elif filling == "":
        filling = False


def min_num(user_list):
    minimum_num = user_list[0]
    for num in user_list:
        if num < minimum_num:
            minimum_num = num
    return minimum_num


print(f"The minimum num of the entered values is: {min_num(list_of_nums)}")
