filling = True
list_of_nums = []
while filling:
    filling = input("Enter a number to fill in the list or press Enter to continue: ")
    if filling != "":
        list_of_nums.append(filling)
        print(list_of_nums)
    elif filling == "":
        filling = False


def nums_multiplication(user_list):
    sum_of_multiplication = 1
    for nums in user_list:
        sum_of_multiplication = sum_of_multiplication * int(nums)
    return sum_of_multiplication


print(f"The sum of multiplication of the entered values is: {nums_multiplication(list_of_nums)}")
