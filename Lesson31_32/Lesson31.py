my_tuple = (1, 2, 3, 4, 5, 6, 7)
print(my_tuple)
a, b, c, d = 1, 2, 3, 4
print(a)
data = ("Yaroslaw", "12345")
login, password = data
print(login)
print(password)

data = ([1, 2, 3, 4], ["a", "b", "c"])
data[0].append(5)
data[1].append("d")
data[0].remove(1)
print(data)

t = (1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c")
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d"]
print(l.__sizeof__(), t.__sizeof__())

# my_new_tuple = ("apple", "pineapple", "orange", "strawberry", "cranberry", "peach", "apple", "strawberryberry", "strawberry-new", "strawberryberry25")
# same = 0
# not_exactly_same = 0
# for j in range(len(my_new_tuple)):
#     for i in range(j + 1, len(my_new_tuple)):
#         if my_new_tuple[j] == my_new_tuple[i]:
#             same += 1
#         elif my_new_tuple[j] == my_new_tuple[i][:len(my_new_tuple[j])]:
#             not_exactly_same += 1
#
# print(same, not_exactly_same)

my_new_tuple = ("apple", "pineapple", "orange", "strawberry", "cranberry", "peach", "apple", "strawberryberry", "strawberry-new", "strawberryberry25")
same = 0
searched = "berry"
not_exactly_same = 0
# for j in range(len(my_new_tuple)):
#     for i in range(j + 1, len(my_new_tuple)):
#         if my_new_tuple[j] == my_new_tuple[i]:
#             same += 1
#         elif my_new_tuple[j] in my_new_tuple[i][:]:
#             not_exactly_same += 1
#
# print(same, not_exactly_same)

for fruit in my_new_tuple:
    if searched in fruit[:]:
        not_exactly_same += 1
print(not_exactly_same)

cars = ("Mercedes", "Volvo", "Volkswagen", "Alfa Romeo")
find = "Mercedes"
change = "Mercedes-Benz"
cars = list(cars)
for i in range(len(cars)):
    if cars[i] == find:
        cars[i] = change
cars = tuple(cars)
print(cars)



