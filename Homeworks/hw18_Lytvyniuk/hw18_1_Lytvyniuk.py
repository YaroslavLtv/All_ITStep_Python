home_work = True
while home_work:
    home_work = input("Enter a number from [1] to [7] to check homework, or type [e] to exit:")
    if home_work == "1":
        # Task 1
        def format_text():
            string = f"'Don't compare yourself with anyone in this world...\n" \
                f"if you do so, you are insulting yourself.'\n" \
                f"\t\t\t\t\t\t\t\t\t\tBill Gates"
            return string
        print(format_text())
    elif home_work == "2":
        # Task 2
        input_num1 = int(input("Enter first number: "))
        input_num2 = int(input("Enter last number: "))

        def even_nums(num1, num2):
            print(f"Even numbers of range: {num1} - {num2}:")
            if num1 > num2:
                for i in range(num2, num1):
                    if i % 2 == 0:
                        print(i)
            else:
                for i in range(num1, num2):
                    if i % 2 == 0:
                        print(i)
        even_nums(input_num1, input_num2)

    elif home_work == "3":
        # Task 3
        n = int(input("Enter width and height of square: "))
        s = " " + input("Enter a symbol: ") + " "
        logic = input("Press [Enter] to write not filled square, or press [Eny Key] + [Enter] to fill square: ")

        def line(width=6, symbol=" * ", logical_statement=False):
            if not logical_statement:
                for i in range(0, width, 1):
                    if i == 0 or i == width - 1:
                        print(symbol * width)
                    else:
                        print(symbol + ("   " * (width - 2)) + symbol)
            else:
                for i in range(0, width, 1):
                    print(symbol * width)
        line(n, s, bool(logic))

    elif home_work == "4":
        # Task 4
        input_num_1 = int(input("Enter first number: "))
        input_num_2 = int(input("Enter second number: "))
        input_num_3 = int(input("Enter third number: "))
        input_num_4 = int(input("Enter fourth number: "))

        def quad_min(num1, num2, num3, num4):
            min_num = num1
            list_of_arguments = [num1, num2, num3, num4]
            for i in range(len(list_of_arguments)):
                if list_of_arguments[i] < min_num:
                    min_num = list_of_arguments[i]
            return min_num

        print(f"The minimum number is: ", end=" ")
        print(quad_min(input_num_1, input_num_2, input_num_3, input_num_4))
    elif home_work == "5":
        # Task 5
        input_num_1 = int(input("Enter first number: "))
        input_num_2 = int(input("Enter second number: "))

        def sum_of_nums(num1, num2):
            sum_of_range = 0
            if num1 > num2:
                for i in range(num2, num1 + 1):
                    sum_of_range = sum_of_range + i
                return sum_of_range
            else:
                for i in range(num1, num2 + 1):
                    sum_of_range = sum_of_range + i
                return sum_of_range
        print(f"Sum of range {input_num_1} - {input_num_2} is: {sum_of_nums(input_num_1, input_num_2)}")
    elif home_work == "6":
        # Task 6
        input_num_1 = input("Enter a number: ")

        def digits_in_number(number):
            iterations = 0
            for i in range(len(number)):
                if number[i].isdigit():
                    iterations += 1
            return iterations
        print(f"In entered number {input_num_1} is {digits_in_number(input_num_1)} digits")
    elif home_work == "7":
        # Task 7
        input_num_1 = input("Enter a number: ")

        def is_palindrome(number):
            reversed_str = ""
            for i in range(1, len(number) + 1):
                reversed_str = reversed_str + number[-i]
            print(reversed_str)
            if reversed_str == number:
                return True
            else:
                return False
        print(f"Entered number or string is palindrome? {is_palindrome(input_num_1)}")
    elif home_work == "e":
        home_work = False
