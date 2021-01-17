# TicTacToe

# Create board and game
game = True
table = "Name      Moves\n"
while game:
    cell_1 = '1'
    cell_2 = '2'
    cell_3 = '3'
    cell_4 = '4'
    cell_5 = '5'
    cell_6 = '6'
    cell_7 = '7'
    cell_8 = '8'
    cell_9 = '9'

    print(f"{cell_1} {cell_2} {cell_3}\n"
          f"{cell_4} {cell_5} {cell_6}\n"
          f"{cell_7} {cell_8} {cell_9}\n")

    count_number = 0
    player_symbol = 'X'
    bot_symbol = "O"
    winner = "*"
    turn = 'X'
    choice = ''
    player1 = ""

    while not player1:
        player1 = input("Enter your name: ")
    player2 = "Computer"
    while count_number < 9:
        # X turn
        while True:
            choice = str(input("Enter number of cell : "))
            if choice == cell_1:
                cell_1 = turn
                break
            elif choice == cell_2:
                cell_2 = turn
                break
            elif choice == cell_3:
                cell_3 = turn
                break
            elif choice == cell_4:
                cell_4 = turn
                break
            elif choice == cell_5:
                cell_5 = turn
                break
            elif choice == cell_6:
                cell_6 = turn
                break
            elif choice == cell_7:
                cell_7 = turn
                break
            elif choice == cell_8:
                cell_8 = turn
                break
            elif choice == cell_9:
                cell_9 = turn
                break
            # Check of winner
            if cell_1 != '1':
                if cell_1 == cell_2 == cell_3:
                    winner = cell_1
                elif cell_1 == cell_4 == cell_7:
                    winner = cell_1
                elif cell_1 == cell_5 == cell_9:
                    winner = cell_1
            if cell_2 != '2':
                if cell_2 == cell_5 == cell_8:
                    winner = cell_2
            if cell_3 != '3':
                if cell_3 == cell_5 == cell_7:
                    winner = cell_3
                elif cell_3 == cell_6 == cell_9:
                    winner = cell_3
            if cell_4 != '4':
                if cell_4 == cell_5 == cell_6:
                    winner = cell_4
            if cell_5 != '5':
                if cell_4 == cell_5 == cell_6:
                    winner = cell_5
            if cell_6 != '6':
                if cell_3 == cell_6 == cell_9:
                    winner = cell_6
            if cell_7 != '7':
                if cell_7 == cell_8 == cell_9:
                    winner = cell_7

        # Counter of step
        count_number = count_number + 1
        if count_number >= 9:
            break
        elif winner != '*':
            break

        # Write board
        print(f"{cell_1} {cell_2} {cell_3}\n"
              f"{cell_4} {cell_5} {cell_6}\n"
              f"{cell_7} {cell_8} {cell_9}\n")

        # Change turn
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

        import random
        # O turn
        while True:
            choice = str(random.randint(1, 9))
            if choice == cell_1:
                cell_1 = turn
                break
            elif choice == cell_2:
                cell_2 = turn
                break
            elif choice == cell_3:
                cell_3 = turn
                break
            elif choice == cell_4:
                cell_4 = turn
                break
            elif choice == cell_5:
                cell_5 = turn
                break
            elif choice == cell_6:
                cell_6 = turn
                break
            elif choice == cell_7:
                cell_7 = turn
                break
            elif choice == cell_8:
                cell_8 = turn
                break
            elif choice == cell_9:
                cell_9 = turn
                break
        # Counter of step
        count_number = count_number + 1
        if count_number >= 9:
            break
        elif winner != '*':
            break

        # Write board
        print(f"{cell_1} {cell_2} {cell_3}\n"
              f"{cell_4} {cell_5} {cell_6}\n"
              f"{cell_7} {cell_8} {cell_9}\n")

        # Change turn
        if turn == 'O':
            turn = 'X'
        else:
            turn = 'O'

        # Check of winner
        if cell_1 != '1':
            if cell_1 == cell_2 == cell_3:
                winner = cell_1
            elif cell_1 == cell_4 == cell_7:
                winner = cell_1
            elif cell_1 == cell_5 == cell_9:
                winner = cell_1
        if cell_2 != '2':
            if cell_2 == cell_5 == cell_8:
                winner = cell_2
        if cell_3 != '3':
            if cell_3 == cell_5 == cell_7:
                winner = cell_3
            elif cell_3 == cell_6 == cell_9:
                winner = cell_3
        if cell_4 != '4':
            if cell_4 == cell_5 == cell_6:
                winner = cell_4
        if cell_5 != '5':
            if cell_4 == cell_5 == cell_6:
                winner = cell_5
        if cell_6 != '6':
            if cell_3 == cell_6 == cell_9:
                winner = cell_6
        if cell_7 != '7':
            if cell_7 == cell_8 == cell_9:
                winner = cell_7

    if winner == '*':
        print("Toe")
    else:
        print(f'{winner} won the game !')
    if winner and winner != '*':
        if winner == "X":
            table = table + f"{player1.ljust(10, ' ')}{str(count_number // 2).ljust(10, ' ')}\n"
        else:
            table = table + f"{player2.ljust(10, ' ')}{str(count_number // 2).ljust(10, ' ')}\n"
        game = not input("Press [Enter] to continue or Any key to exit: ")
print(table)