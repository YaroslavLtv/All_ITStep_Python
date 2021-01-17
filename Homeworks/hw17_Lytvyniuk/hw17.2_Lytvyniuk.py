new_list = []
inner_list_odd = []
inner_list_even = []
n = int(input("Enter width of board: "))
m = int(input("Enter height of board: "))
for i in range(n):
    if i % 2 == 0:
        inner_list_odd.append(".")
    else:
        inner_list_odd.append("*")
for i in range(n):
    if i % 2 == 0:
        inner_list_even.append("*")
    else:
        inner_list_even.append(".")

for i in range(m):
    if i % 2 == 0:
        new_list.append(inner_list_odd)
    else:
        new_list.append(inner_list_even)

for i in range(m):
    for j in range(n):
        print(new_list[i][j], end="  ")
    print()