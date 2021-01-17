user_tuple_1 = (1, 2, 3, 5, 10, 11, 12)
user_tuple_2 = (4, 2, 5, 5, 10, 11)
user_tuple_3 = (3, 2, 7, 5, 11, 10, 13, 15)

for i in range(len(user_tuple_2)):
    if user_tuple_2[i] == user_tuple_1[i] == user_tuple_3[i]:
        print(f"element in tuple 1 is: {user_tuple_1[i]}, "
              f"element in tuple 2 is: {user_tuple_2[i]}, "
              f"element in tuple 3 is: {user_tuple_3[i]}")
