fill_the_list = True
my_list = []
while fill_the_list:
    entered_symbol = input("Enter a number to fill the list or press Enter to continue: ")
    if entered_symbol:
        my_list.append(int(entered_symbol))
    else:
        fill_the_list = False
    print(my_list)

num_to_find = int(input("Enter a number to search: "))


def find_number(user_num, user_list):
    for i in range(len(user_list)):
        if user_list[i] == user_num:
            print(f"the program found your number: {user_list[i]} by {i} index")


find_number(num_to_find, my_list)
