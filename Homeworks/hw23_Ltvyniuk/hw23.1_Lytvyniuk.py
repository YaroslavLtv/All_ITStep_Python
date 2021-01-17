user_tuple_1 = (1, 2, 3, 5, 10, 11, 12)
user_tuple_2 = (4, 2, 5, 7, 10, 11)
user_tuple_3 = (3, 2, 7, 5, 11, 10, 13, 15)

list_of_duplicates = []
final_list_of_duplicates = []
for nums in user_tuple_3:
    for num in user_tuple_2:
        if nums == num:
            list_of_duplicates.append(nums)

for nums in list_of_duplicates:
    for num in user_tuple_1:
        if nums == num:
            final_list_of_duplicates.append(nums)

print(f"the same numbers in each of 3 tuples is: {final_list_of_duplicates}")
