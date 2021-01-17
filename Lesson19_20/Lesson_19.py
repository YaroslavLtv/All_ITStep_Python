# pole = [0, "1", "2", "3", "4", "5", "6", "7", "8", "9"]
# print(pole)
# print("\n", pole[1], pole[2], pole[3], "\n", pole[4], pole[5], pole[6], "\n", pole[7], pole[8], pole[9])
# pole_2 = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
# print(pole_2[0])
# print(pole_2[1])
# print(pole_2[2])
#
# for elem in pole:
#     print(elem, end=" ")
# print()
# for i in range(len(pole)):
#     print(pole[i], end=" ")
# print("\n")
#
# print(pole_2[0][0], pole_2[0][1], pole_2[0][2])
# print(pole_2[1][0], pole_2[1][1], pole_2[1][2], )
# print(pole_2[2][0], pole_2[2][1], pole_2[2][2], )

# for i in range(len(pole_2)):
#     for j in range(len(pole_2[i])):
#         print(pole_2[i][j], end=" ")
#     print()
#
# pole_2[1][1] = "x"

# for i in range(len(pole_2)):
#     for j in range(len(pole_2[i])):
#         print(pole_2[i][j], end=" ")
#     print()

# pole_2 = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
# for i in range(len(pole_2)):
#     for j in range(len(pole_2[i])):
#         pole_2[i][j] = "X"
#
#         print(pole_2[i][j], end=" ")
#     print()
#
# a = [1, 2, 3]
# b = a[:]
# print(a, b)
# a.append(4)
# print(a, b)

# Tic Tac Toe
pole = [0, '1', '2', '3', '4', '5', '6', '7', '8', '9']
pole_bot = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

print(f"{pole[1]} {pole[2]} {pole[3]}\n"
      f"{pole[4]} {pole[5]} {pole[6]}\n"
      f"{pole[7]} {pole[8]} {pole[9]}\n")

count_number = 0
player_symbol = 'X'
bot_symbol = "O"
winner = "*"
turn = 'X'
choice = ''
while count_number < 9:
    # X turn
    flag = True
    while flag:
        choice = str(input("Enter number of cell : "))
        for i in range(len(pole)):
            if choice == pole[i]:
                pole_bot.remove(pole[i])
                pole[i] = turn
                flag = False
                break

    # Check of winner
    if pole[1] != '1':
        if pole[1] == pole[2] == pole[3]:
            winner = pole[1]
        elif pole[1] == pole[4] == pole[7]:
            winner = pole[1]
        elif pole[1] == pole[5] == pole[9]:
            winner = pole[1]
    if pole[2] != '2':
        if pole[2] == pole[5] == pole[8]:
            winner = pole[2]
    if pole[3] != '3':
        if pole[3] == pole[5] == pole[7]:
            winner = pole[3]
        elif pole[3] == pole[6] == pole[9]:
            winner = pole[3]
    if pole[4] != '4':
        if pole[4] == pole[5] == pole[6]:
            winner = pole[4]
    if pole[7] != '7':
        if pole[7] == pole[8] == pole[9]:
            winner = pole[7]
    # Counter of step
    count_number = count_number + 1
    if count_number >= 9:
        break
    elif winner != '*':
        break

    # Write board

    print(f"{pole[1]} {pole[2]} {pole[3]}\n"
          f"{pole[4]} {pole[5]} {pole[6]}\n"
          f"{pole[7]} {pole[8]} {pole[9]}\n")
    # Change turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

    import random

    # O turn
    flag1 = True
    while flag1:
        choice = str(random.choice(pole_bot))
        for i in range(len(pole)):
            if choice == pole[i]:
                pole_bot.remove(pole[i])
                pole[i] = turn
                flag1 = False
                break

    # Counter of step
    count_number = count_number + 1
    if count_number >= 9:
        break
    elif winner != '*':
        break

    # Write board
    print(f"{pole[1]} {pole[2]} {pole[3]}\n"
          f"{pole[4]} {pole[5]} {pole[6]}\n"
          f"{pole[7]} {pole[8]} {pole[9]}\n")

    # Check of winner
    if pole[1] != '1':
        if pole[1] == pole[2] == pole[3]:
            winner = pole[1]
        elif pole[1] == pole[4] == pole[7]:
            winner = pole[1]
        elif pole[1] == pole[5] == pole[9]:
            winner = pole[1]
    if pole[2] != '2':
        if pole[2] == pole[5] == pole[8]:
            winner = pole[2]
    if pole[3] != '3':
        if pole[3] == pole[5] == pole[7]:
            winner = pole[3]
        elif pole[3] == pole[6] == pole[9]:
            winner = pole[3]
    if pole[4] != '4':
        if pole[4] == pole[5] == pole[6]:
            winner = pole[4]
    if pole[7] != '7':
        if pole[7] == pole[8] == pole[9]:
            winner = pole[7]
    if turn == 'O':
        turn = 'X'
    else:
        turn = 'O'
if winner == '*':
    print("Toe")
else:
    print(f'{winner} won the game !')