
# Вводимо координати для знаходження першої клітинки
chess_cell_1_x = int(input("Enter coordinates on x axis of first cell (numbers from 1 to 8): "))
chess_cell_1_y = int(input("Enter coordinates on y axis of first cell (numbers from 1 to 8): "))

# Вводимо координати для знаходження другої клітинки
chess_cell_2_x = int(input("Enter coordinates on x axis of second cell (numbers from 1 to 8): "))
chess_cell_2_y = int(input("Enter coordinates on y axis of second cell (numbers from 1 to 8): "))

# Попередньо задаємо значення для змінних, в які потім запишемо колір клітинок
cell_1_is_colored = False
cell_2_is_colored = False

# Перевіряємо колір вибраної клітинки та перезаписуємо змінну з кольором для першої клітинки
if (chess_cell_1_x + chess_cell_1_y) % 2 == 0:
    cell_1_is_colored = False
else:
    cell_1_is_colored = True

# Перевіряємо колір вибраної клітинки та перезаписуємо змінну з кольором для другої клітинки
if (chess_cell_2_x + chess_cell_2_y) % 2 == 0:
    cell_2_is_colored = False
else:
    cell_2_is_colored = True

# print(cell_1_is_colored, cell_2_is_colored)

# Перевіряємо чи вибрані клітинки одного кольору, якщо так - виводимо YES, якщо ні - виводимо NO
if cell_1_is_colored == cell_2_is_colored:
    print("YES")
else:
    print("NO")
