# import random
# import time
#
# numbers = [11, 2, 13, 4, 15, 6, 17, 8]
# letters = "abcdefghijkl"
# numbers.sort()
# print(numbers)
# print(numbers[0], "min")
# print(numbers[-1], "max")
#
#
# def random_list(quantity_of_nums, range_from, range_to):
#     n = []
#     for i in range(quantity_of_nums):
#         a = random.randint(range_from, range_to)
#         n.append(a)
#     return n
#
#
# def find_equals_index(user_list, num_to_find):
#     for i in range(len(user_list)):
#         if user_list[i] == num_to_find:
#             return i
#     return -1
#
#
# print(find_equals_index(random_list(10, -5, 20), -3))
# l = random_list(100, 1, 100)


# Bubble sort
numbers = [1, 19, 2, 17, 3, 18, 4, 20, 5, 11]
a = len(numbers)
while True:
    a = 1
    flag = True
    while True:
        if numbers[-a] < numbers[-(a+1)]:
            c = numbers[-a]
            numbers[-a] = numbers[-(a+1)]
            numbers[-(a+1)] = c
            flag = False
        a = a + 1
        if a >= len(numbers):
            break
    if flag:
        break
print(numbers)