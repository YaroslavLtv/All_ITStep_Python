import random
random_list = []
minimum_num = 0
maximum_num = 0
number_of_negative = 0
number_of_positive = 0
number_of_zero = 0
for i in range(10):
    random_list.append(random.randint(-20, 99))
print(f"List of random numbers: {random_list}")

for num in random_list:
    if num > maximum_num:
        maximum_num = num
    elif num == 0:
        number_of_zero += 1
    elif num < minimum_num:
        minimum_num = num

    if num < 0:
        number_of_negative += 1
    elif num > 0:
        number_of_positive += 1

print(f"Maximum number is: {str(maximum_num).rjust(22, ' ')}\n"
      f"Minimum number is: {str(minimum_num).rjust(22, ' ')}\n"
      f"The number of negative numbers: {str(number_of_negative).rjust(8, ' ')}\n"
      f"The number of positive numbers: {str(number_of_positive).rjust(8, ' ')}\n"
      f"Number of zero's: {str(number_of_zero).rjust(22, ' ')}")
