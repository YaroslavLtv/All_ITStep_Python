# numbers = []
# num = ""
# while True:
#     num = input("Enter number or [e] to exit: ")
#     if num == "e":
#         break
#     if not num.isdigit():
#         continue
#
#     numbers.append(int(num))
# find = int(input("Enter number to find:"))
# count = 0
# for number in numbers:
#     if number == find:
#         count += 1
# print(count)

# numbers = []
# num = ""
# all_sum = 0
# count = 0
# while True:
#
#     num = input("Enter number or [e] to exit: ")
#     if num == "e":
#         break
#     if not num.isdigit():
#         continue
#
#     numbers.append(int(num))
#
#     count += 1
#
# for i in range(len(numbers)):
#     all_sum = all_sum + numbers[i]
# print(f"Summ {all_sum} average {all_sum / count}")

import random
f = int(input("Enter start of range: "))
t = int(input("Enter end of range: "))
c = int(input("Enter count of numbers: "))
sum_of_negative = 0
sum_of_even = 0
sum_of_odd = 0
sum_of_div_3 = 0
maximum = 0
minimum = 0
numbers = []

for i in range(c):
    numbers.append(random.randint(f, t))
print(numbers)

for i in range(len(numbers)):
    if numbers[i] < 0:
        sum_of_negative += numbers[i]
    elif numbers[i] % 2 == 0:
        sum_of_even += numbers[i]
    elif numbers[i] % 2 != 0:
        sum_of_odd += numbers[i]
    elif i % 3 == 0:
        sum_of_div_3 += numbers[i]
    if numbers[i] > maximum:
        maximum = numbers[i]
    if numbers[i] < minimum:
        minimum = numbers[i]
if numbers.index(minimum) < numbers.index(maximum):
    five_list = numbers[numbers.index(minimum):numbers.index(maximum) + 1]
else:
    five_list = numbers[numbers.index(maximum):numbers.index(minimum) + 1]  # Numbers[2:5]
print(five_list)
five_mult = 1
for num in five_list:
    five_mult *= num
print(five_mult)
print(f"sum of negative numbers {sum_of_negative}, sum of even numbers {sum_of_even}, "
      f"sum of odd numbers {sum_of_odd}, sum of numbers divided by 3 {sum_of_div_3} ")


