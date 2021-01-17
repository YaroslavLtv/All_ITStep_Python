user_number_1 = int(input("Enter first number in range: "))
user_number_2 = int(input("Enter second number in range: "))

even_numbers = 0
odd_numbers = 0
multiple_of_nine = 0

current_iteration_even = 0
current_iteration_odd = 0
current_iteration_multi_nine = 0

aver_even_numbers = 0
aver_odd_numbers = 0
aver_multiple_of_nine = 0

for i in range(user_number_1, user_number_2 + 1):

    if i % 2 == 0:
        even_numbers = even_numbers + i
        current_iteration_even += 1
    elif i % 2 != 0:
        odd_numbers = odd_numbers + i
        current_iteration_odd += 1

    if i % 9 == 0:
        multiple_of_nine = multiple_of_nine + i
        current_iteration_multi_nine += 1

aver_even_numbers = even_numbers / current_iteration_even
aver_odd_numbers = odd_numbers / current_iteration_odd
aver_multiple_of_nine = multiple_of_nine / current_iteration_multi_nine

print(f"\nsumma of even numbers: {even_numbers}, \n"
      f"summa of odd numbers: {odd_numbers}, \n"
      f"summa of numbers multiples of nine: {multiple_of_nine}, ")
print(f"average of even numbers: {aver_even_numbers}, \n"
      f"average of odd numbers: {aver_odd_numbers}, \n"
      f"average of numbers multiples of nine: {aver_multiple_of_nine}")
