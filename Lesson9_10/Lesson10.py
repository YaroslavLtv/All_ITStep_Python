# black_cell = "*"
# white_cell = "_"
# width = 5
# height = 5
# board_width = 8
# board_height = 8
#
# for z in range(board_height // 2):
#     for j in range(height):
#         for i in range(board_width // 2):
#             print(width * black_cell, end="")
#             print(width * white_cell, end="")
#         print()
#     for j in range(height):
#         for i in range(board_width // 2):
#             print(width * white_cell, end="")
#             print(width * black_cell, end="")
#         print()

# Multiply

# import random
# score = 0
# game = True
# start = True
# hard_level = int(input("Enter one of 3 levels hard: "))
# points = 0
# users = ""
# new_user = input("Enter your name: ")
# if hard_level == 3:
#     points = 5
# elif hard_level == 2:
#     points = 10
# elif hard_level == 1:
#     points = 15
#
# while game:
#     while start:
#         n1 = random.randint(1, 12)
#         n2 = random.randint(1, 12)
#         result = n1 * n2
#         answer = int(input(f"Enter multiply {n1} * {n2} = "))
#         print(f"{points}, {score}")
#
#         if answer == result:
#             score += 1
#         else:
#
#             points -= 1
#
#         if points == 0:
#             start = False
#             users = users + "\n" + new_user + f" score {score}"
#             print(f"{users}")
#
# game = bool(input("Press enter to exit"))
#

import random
table = ''
while True:
    score = 0
    start = True
    login = str(input("Enter your login : "))
    hardness = str(input("Enter difficult level : [easy], [medium], [hard]"))
    while start:
        f = 1
        t = 10
        if hardness == "easy":
            f = 1
            t = 12
        elif hardness == "medium":
            f = 1
            t = 20
        elif hardness == "medium":
            f = 1
            t = 20
        n1 = random.randint(f, t)
        n2 = random.randint(f, t)
        result = n1 * n2
        answer = int(input(f"Enter multiply {n1} * {n2} = "))
        if answer == result:
            score += 1
        elif answer != result and hardness == 'hard':
            score -= 1
        start = bool(input("Press Enter to exit"))
    print(f'{login} your score {score}')
    table = table + f'{login} your score {score} with hardness {hardness}' + '\n'
    print(table)
