
# Enter the coordinate to find the first cell (letter and then number)
chess_cell_1_x = input("Enter a letter of first cell (a - h): ")
chess_cell_1_y = int(input("Enter a number of first cell (numbers from 1 to 8): "))

# Enter the coordinates to find the second cell (letter and then number)
chess_cell_2_x = input("Enter a letter of second cell (a - h): ")
chess_cell_2_y = int(input("Enter a number of second cell (numbers from 1 to 8): "))

# Check if cells with the same coordinates are selected. If so, the chess piece will remain in place.
if chess_cell_1_x == chess_cell_2_x and chess_cell_1_y == chess_cell_2_y:
    print("Stay in the same position")

# Check if the figure can move from the first to the second selected cells
elif chess_cell_1_x == chess_cell_2_x or chess_cell_1_y == chess_cell_2_y:
    print("YES, chess figure can move")
# In other cases, we display a message about the impossibility of moving the figure
# from the first to the second selected cells
else:
    print("NO, chess figure can not move")
