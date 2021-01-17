user_number_1 = int(input("Enter first number in range: "))
user_number_2 = int(input("Enter second number in range: "))
div_on_seven = ""
sum_div_on_five = 0
user_iterations = user_number_2
text_separator = " | "

# Display range of user numbers, numbers multiples of 7 in table

for i in range(user_number_1, user_number_2 + 1):
    print(f"{text_separator} {i} {text_separator} {user_iterations}", end="")
    user_iterations -= 1
    if i % 7 == 0:
        div_on_seven = i
    else:
        div_on_seven = ""
    print(f"{text_separator} {div_on_seven} {text_separator}")

# Determining the number multiples of 5
    if i % 5 == 0:
        sum_div_on_five += 1


print(f"numbers divided without reminder by the number 5 is: {sum_div_on_five}")

