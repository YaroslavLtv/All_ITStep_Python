# f = open("text.ltv", "rt+")
# # f.write("Hello!\n")
# print(f.read())
# f.close()

f = open("text.txt", "rt+")
# f.write("Hello!\n")
# print(f.read())
# for line in f:
#     print(line)
# print(f.readline(4))
# print(f.readlines())
# f.close()
#
# f = open("test.txt", "rt+")
# file2 = open("text2.txt", "at+")
# str_n = f.readlines()
# print(str_n)
# for i in range(len(str_n)):
#     file2.write(str_n[i])

# f = open("test.txt", "rt+")
# file2 = open("text2.txt", "wt+")
# str_n = f.readlines()
# print(str_n)
# for i in range(1, len(str_n) + 1):
#     file2.write(str_n[-i])

# f = open("test.txt", "rt+")
# file2 = open("text2.txt", "wt+")
# str_n = f.readlines()
# print(str_n)
# for i in range(len(str_n)):
#     if len(str_n[i]) >= 7:
#         file2.write(str_n[i])

# Варіант Коваленка А. +++
f1 = open("test2.txt", "rt")
f2 = open("result_file_4.txt", "at")

for line in f1:
    for word in line.split(' '):
        if len(word) > 7:
            f2.write(word + "\n")

f1.close()
f2.close()