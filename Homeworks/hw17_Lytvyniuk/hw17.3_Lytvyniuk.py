number = int(input("Enter dimensions from [0] to [10]: "))
my_list = []
for i in range(number):
    my_list.append([])
    for j in range(number):
        my_list[i].append(abs(j-i))

for i in range(len(my_list)):
    for j in range(len(my_list)):
        print(my_list[i][j], end="  ")
    print()