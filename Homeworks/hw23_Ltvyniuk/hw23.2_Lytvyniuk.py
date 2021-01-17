user_tuple_1 = (1, 2, 3, 5, 10, 11, 12)
user_tuple_2 = (4, 2, 5, 7, 10, 11)
user_tuple_3 = (3, 2, 7, 5, 11, 10, 13, 15)

list_of_duplicates = []
final_list_of_duplicates = []
flag = True

for nums in user_tuple_3:
    for num in user_tuple_2:
        if nums != num:
            print(nums)
            flag = True
        elif nums == num:
            flag = False
            break
    if flag:
        list_of_duplicates.append(nums)
        list_of_duplicates.append(num)
    print(list_of_duplicates)

for nums in list_of_duplicates:
    for num in user_tuple_1:
        if nums != num:
            flag = True
        elif nums == num:
            flag = False
            break
    if flag:
        final_list_of_duplicates.append(nums)
        final_list_of_duplicates.append(num)

final_list_of_duplicates.sort()
final_list_of_duplicates_2 = []

for i in range(len(final_list_of_duplicates)):
    if final_list_of_duplicates[-i] != final_list_of_duplicates[-i-1]:
        final_list_of_duplicates_2.append(final_list_of_duplicates[-i])

print(f"the same numbers in each of 3 tuples is: {final_list_of_duplicates_2}")