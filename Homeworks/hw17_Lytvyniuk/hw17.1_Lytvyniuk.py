number = int(input("Enter a odd number: "))
inner_list = []
outer_list = []
my_symbol = "."
for i in range(number):
    outer_list.append([my_symbol] * number)

for i in range(len(outer_list)):
    outer_list[i][i] = "*"
    outer_list[i][-i - 1] = "*"
    outer_list[i][len(outer_list) // 2] = "*"
    outer_list[len(outer_list) // 2][i] = "*"

for i in range(len(outer_list)):
    for j in range(len(outer_list)):
        print(outer_list[i][j], end="  ")
    print()
