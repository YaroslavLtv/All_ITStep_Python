fill_the_list = True
my_list = []
while fill_the_list:
    entered_symbol = input("Enter a number to fill the list or press Enter to continue: ")
    if entered_symbol:
        my_list.append(int(entered_symbol))
    else:
        fill_the_list = False
    print(my_list)

num_to_delete = int(input("Enter a number to search and delete: "))


def items_to_delete(user_list, user_num):
    my_list_temp = []
    deletes = 0
    for num in user_list:
        if num != user_num:
            my_list_temp.append(num)
        else:
            deletes += 1
    user_list = my_list_temp[:]
    print(f"List without deleted numbers: {user_list}\nProgram makes: {deletes} deletes")

items_to_delete(my_list, num_to_delete)
