width_of_rectangle = int(input("Enter width of rectangle: "))
height_of_rectangle = int(input("Enter length of rectangle: "))
user_symbol = input("Enter a symbol: ")

for j in range(height_of_rectangle):
    print()
    for i in range(width_of_rectangle):
        print(f" {user_symbol} ", end="")
