import hw_functions
fill_the_list = True
my_list = [25, 22, 21, 11, 55, 58, 84, 89, 99, 45, 125, 101, 97, 2, 3, 7, 11, 11, 15, 58, 88]
while fill_the_list:
    entered_symbol = input("Enter a number to fill the list or press Enter to continue: ")
    if entered_symbol:
        my_list.append(int(entered_symbol))
    else:
        fill_the_list = False
    print(my_list)

num_to_find = int(input("Enter a number to search: "))
sort_method = input("Enter method of sort:\n[b] - bubble sort\n[s] - selection sort\n[i] - insertion sort\n"
                    "[h] - heapify sort\n[m] - merge sort\n[q] - quick sort\n[t] - timsort: ")
search_method = input("Enter a search method:\n[l] - linear\n[b] - binary: ")

if sort_method == "b":
    hw_functions.bubble_sort(my_list)
elif sort_method == "s":
    hw_functions.selection_sort(my_list)
elif sort_method == "i":
    hw_functions.insertion_sort(my_list)
elif sort_method == "h":
    hw_functions.heap_sort(my_list)
elif sort_method == "m":
    hw_functions.merge_sort(my_list)
elif sort_method == "q":
    hw_functions.quick_sort(my_list)
elif sort_method == "t":
    my_list.sort()

if search_method == "l":
    print(my_list)
    print(f"index of searched num is: {hw_functions.linear_search(num_to_find, my_list)}")
elif search_method == "b":
    print(my_list)
    print(f"index of searched num is: {hw_functions.binary_search(my_list, num_to_find, 0, len(my_list))}")
