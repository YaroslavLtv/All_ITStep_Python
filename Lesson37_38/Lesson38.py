# f = open("4.png", "rb")
# file1 = f.read()
# for i in range(1, 3):
#     f1 = open(f"4{i}.png", "wb")
#     f1.write(file1)
#     f1.close()
# f.close()


# my_dict = {"a": "1", "b": "2", "c": "3"}
# my_file = open("my_file", "wt+")
# for elem in my_dict:
#     my_file.write(elem)
#     my_file.write(my_dict[elem] + "\n")
# my_file.close()

my_dict = {"a": "1", "b": "2", "c": "3"}
my_file = open("my_file", "wt+")
for key in my_dict:
    my_file.write(f"{key} : {my_dict[key]}\n")
my_file.close()

# f = open("task7.txt", "rt")
# l = f.readlines()
# my_dict1 = {}
# for element in l:
#     a = element.find(":")
#     key = element[:a-1]
#     value = element[a+2:]
#     my_dict1[key] = value
# f.close()
# print(my_dict1)