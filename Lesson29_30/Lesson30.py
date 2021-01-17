import lesson29_functions


filling = True
list_of_nums = []
while filling:
    filling = input("Enter a number to fill in the list or press Enter to continue: ")
    if filling != "":
        list_of_nums.append(int(filling))
        print(list_of_nums)
    elif filling == "":
        filling = False

sort = True
list_not_sorted = list_of_nums[:]
while sort:
    sort = str(input("Enter sort type: "))
    if sort == "selection":
        lesson29_functions.selection_sort(list_not_sorted)
        print(list_not_sorted)
        list_not_sorted = list_of_nums[:]
    elif sort == "insertion":
        lesson29_functions.insertion_sort(list_not_sorted)
        print(list_not_sorted)
        list_not_sorted = list_of_nums[:]
    elif sort == "merge":
        lesson29_functions.merge_sort(list_not_sorted)
        print(list_not_sorted)
        list_not_sorted = list_of_nums[:]
    elif sort == "quick":
        lesson29_functions.quick_sort(list_not_sorted)
        print(list_not_sorted)
        list_not_sorted = list_of_nums[:]
    elif sort == "none":
        print(list_of_nums)