# TicTacToe

# Create board and game
cell_1 = "1"
cell_2 = "2"
cell_3 = "3"
cell_4 = "4"
cell_5 = "5"
cell_6 = "6"
cell_7 = "7"
cell_8 = "8"
cell_9 = "9"

print(f"{cell_1} {cell_2} {cell_3}\n"
      f"{cell_4} {cell_5} {cell_6}\n"
      f"{cell_7} {cell_8} {cell_9}\n")

count_number = 0
player_symbol = "x"
bot_symbol = "o"
winner = "*"
turn = "x"
choice = ""

# x turn
for i in range(5):
    while True:
        choice = str(input("Enter number of cell: "))
        if choice == cell_1:
            cell_1 = turn
            break
        elif choice == cell_2:
            cell_2 == turn
            break
        elif choice == cell_3:
            cell_3 == turn
            break
        elif choice == cell_4:
            cell_4 == turn
            break
        elif choice == cell_5:
            
            cell_5 == turn
            break
        elif choice == cell_6:
            cell_6 == turn
            break
        elif choice == cell_7:
            cell_7 == turn
            break
        elif choice == cell_8:
            cell_8 == turn
            break
        elif choice == cell_9:
            cell_9 == turn
            break
    # Write board

    print(f"{cell_1} {cell_2} {cell_3}\n"
          f"{cell_4} {cell_5} {cell_6}\n"
          f"{cell_7} {cell_8} {cell_9}\n")

    #Change turn
