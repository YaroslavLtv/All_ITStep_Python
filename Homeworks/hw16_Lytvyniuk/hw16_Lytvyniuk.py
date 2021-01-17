import random
random_list_1 = []
random_list_2 = []
third_list = []
for i in range(12):
    random_list_1.append(random.randint(-10, 20))
    random_list_2.append(random.randint(-99, 99))
print(f"First ist of random numbers: {random_list_1}\nSecond list of random numbers: {random_list_2}")

home_work = True
while home_work:
    home_work = input("To select an exercise, enter [1], [2], [3], [4], [5], or [e] to exit: ")
    if home_work == "1":
        # Elements of first and second random lists
        third_list = random_list_1 + random_list_2
        third_list.sort()
        print(f"List of all elements from two lists: {third_list}")
    elif home_work == "2":
        # Elements of first and second random lists without doubles
        for i in range(len(third_list)):
            for j in range(i + 1, len(third_list)):
                if third_list[i] == third_list[j]:
                    third_list[i] = "del"
        for element in third_list:
            if element == "del":
                third_list.remove(element)
        print(f"List of elements from first and second random lists without doubles: {third_list}")
    elif home_work == "3":
        # Generate a list containing elements common to the two random lists
        fourth_list = []
        for i in range(len(random_list_1)):
            for j in range(len(random_list_2)):
                if random_list_1[i] == random_list_2[j]:
                    fourth_list.append(random_list_1[i])
        print(f"Similar elements in first and second random lists: {fourth_list}")
    elif home_work == "4":
        # List containing only unique elements of each of the random lists
        for i in range(len(random_list_1)):
            for j in range(i + 1, len(random_list_1)):
                if random_list_1[i] == random_list_1[j]:
                    random_list_1[i] = "del"
        for element in random_list_1:
            if element == "del":
                random_list_1.remove(element)
        print(f"Random list one without doubles: {random_list_1}")

        for i in range(len(random_list_2)):
            for j in range(i + 1, len(random_list_2)):
                if random_list_2[i] == random_list_2[j]:
                    random_list_2[i] = "del"
        for element in random_list_2:
            if element == "del":
                random_list_2.remove(element)
        print(f"Random list two without doubles: {random_list_2}")
        unique_from_each_of_lists = random_list_1 + random_list_2
        print(f"Unique values from random list 1 and random list 2: {unique_from_each_of_lists} ")
    elif home_work == "5":
        # List containing only the minimum and maximum values of each of the random lists.
        max_value_1 = 0
        max_value_2 = 0
        min_value_1 = 0
        min_value_2 = 0

        for num in random_list_1:
            if num > max_value_1:
                max_value_1 = num
            elif min_value_1 > num:
                min_value_1 = num

        for num in random_list_2:
            if num > max_value_2:
                max_value_2 = num
            elif min_value_2 > num:
                min_value_2 = num

        max_and_min_of_two_lists = [max_value_1, max_value_2, min_value_1, min_value_2]

        print(f"The minimum and maximum values of each of the random lists: {max_and_min_of_two_lists}")
    elif home_work == "e":
        home_work = False
