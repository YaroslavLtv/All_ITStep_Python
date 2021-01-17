def bubble_sort(user_list):
    while True:
        a = 1
        flag = True
        while True:
            if user_list[-a] < user_list[-(a + 1)]:
                c = user_list[-a]
                user_list[-a] = user_list[-(a + 1)]
                user_list[-(a + 1)] = c
                flag = False
            a = a + 1
            if a >= len(user_list):
                break
        if flag:
            break


def binary_search(user_list, searched_element, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if searched_element == user_list[mid]:
        return mid
    if searched_element < user_list[mid]:
        return binary_search(user_list, searched_element, start, mid-1)
    else:
        return binary_search(user_list, searched_element, mid+1, end)


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

bubble_sort(my_list)

index_of_searched_num = binary_search(my_list, num_to_find, 0, len(my_list))

if binary_search(my_list, num_to_find, 0, len(my_list)) == -1:
    print("There is no searched number in this list")
else:
    print(f"Your's number is on {index_of_searched_num} position in your's list: {my_list}")
