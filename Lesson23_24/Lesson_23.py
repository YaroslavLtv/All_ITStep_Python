# def average(a, b, c = 0, d = 0, e = 0):
#     # av = (a + b + c + d + e) / 5
#     av_list = [a, b, c, d, e]
#     iterations = 0
#     av = 0
#     for i in range(len(av_list)):
#         if av_list[i] != 0:
#             iterations += 1
#             av = av + av_list[i]
#     aver = av / iterations
#     return aver

# print(average(2, 2, 3))

# def sum_of_numbers(*args):
#     for arg in args:
#         print(arg)
# sum_of_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9)
#
# new_list = [1, 5, 10]
# def sum_of_numbers1(num_list = [], *numbers):
#     sum = 0
#     for number in num_list:
#         sum = number +  sum
#     for numbers in numbers:
#         sum = numbers + sum
#     return sum
# print(sum_of_numbers1(new_list, 1, 2, 3, 4, 6))

# def average_nums(*arguments):
#     iterations = 0
#     sum_of_elements = 0
#     for element in arguments:
#         if isinstance(element, int):
#             iterations += 1
#             sum_of_elements = sum_of_elements + element
#     return sum_of_elements / iterations
#
# print(average_nums(13, 2, 10, 5, "hello", "18"))

