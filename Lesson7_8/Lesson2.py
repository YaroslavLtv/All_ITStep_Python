# WHILE
# a = 0
# while a < 10:
#     print(a)
#     a = a + 1
#
# for i in range(10):
#     print(i)

# a = 0
# while a < 10:
#     print(a)
#     a = a + 1

# a = 0
# while True:
#     print(a)
#     a = a + 1

# work = True
# a = 0
# while work:
#     print(a)
#     a = a + 1
#     work = not bool(input("Press any key to continue: "))


# # Task1
# symbol = "*"
# n1 = 5
# n2 = 3
# for i in range(n2):
#     print(n1*symbol)

# Task3
# symbol = "*"
# n = 10
#
# for i in range(n):
#     if i == 0 or i == n-1:
#         print(n * symbol)
#     else:
#         print(symbol + (n - 2) * ' ' + symbol)

# Task4
# symbol = "*"
# height = 10
# width = 8
# for i in range(height):
#     if i == 0 or i == height-1:
#         print(width * symbol)
#     else:
#         print(symbol + (width - 2) * ' ' + symbol)

# summa = 0
# n = -1
# while n != 0:
#     n = int(input("Enter number: "))
#     summa += n
# print(summa)


# summa = 0
# n = -1
# average = 0
# iterations = 0
# while n != 0:
#     n = int(input("Enter number: "))
#     summa += n
#     iterations += 1
#     if n == 0:
#         iterations += -1
#         average = summa / iterations
# print(average, summa)


# n = -1
# iterations = 0
# max_number = 0
# iteration = 0
#
# while n != 0:
#     n = int(input("Enter number: "))
#     iterations += 1
#     if n > max_number:
#         max_number = n
#         iteration = iterations
# print(f"Maximum number vas {max_number}, on {iteration} iteration")

n = 100
while n != 0:
    a = int(input("Enter number: "))
    if n >= a:
        n = n - a
print(n)


