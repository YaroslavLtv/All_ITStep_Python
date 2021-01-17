
run = True

while run:
    user_choice = input("Choose one of figure [a], [b], [c], [d], [e], [f], [g], [h], [i], [j], "
                        "[bonus] \nor type [exit] to exit from menu: ")
    width = 9
    height = 10
    offset = 0
    if user_choice == "a":
        # Figure A !!! (working fine)
        for i in range(height):

            for j in range(offset):
                print("   ", end="")
            offset += 1
            print(" * " * width)
            width -= 1

    if user_choice == "b":
        # Figure B !!! (working fine)
        width = 0
        for i in range(height):
            print(" * " * width)
            width += 1

    if user_choice == "c":
        # Figure C !!! (working fine)
        for i in range(height):

            for j in range(offset):
                print("   ", end="")
            offset += 1
            print(" * " * width)
            width -= 2

    # Figure C !!! (working fine)
    # height = 5
    # for i in range(height):
    #     offset += 1
    #     for j in range(offset):
    #         print(" = ", end="")
    #     print(" * " * width)
    #     width -= 2

    if user_choice == "d":
        # Figure D !!! (working fine)
        height = 5
        offset = 6
        width = 1
        for i in range(height):
            offset -= 1
            for j in range(offset):
                print("   ", end="")
            print(" * " * width)
            width += 2

    # Figure E !!! (working fine)
    # height = 5
    # for i in range(height):
    #     offset += 1
    #     for j in range(offset):
    #         print(" = ", end="")
    #     print(" * " * width)
    #     width -= 2
    #
    # height = 5
    # offset = 6
    # width = 1
    # for i in range(height):
    #     offset -= 1
    #     for j in range(offset):
    #         print(" = ", end="")
    #     print(" * " * width)
    #     width += 2

    if user_choice == "e":
        # Figure E !!! (working fine) SUPER-DUPER
        height = 5
        for i in range(height):
            offset += 1
            for j in range(offset):
                print("   ", end="")
            print(" * " * width + "   " * offset)
            width -= 2

        height = 5
        offset = 6
        width = 1
        for i in range(height):
            offset -= 1
            for j in range(offset):
                print("   ", end="")
            print(" * " * width + "   " * offset)
            width += 2

    if user_choice == "f":
        # Figure F !!! (working fine) SUPER-DUPER
        height = 5
        for i in range(height):
            offset += 1
            for j in range(offset):
                print(" * ", end="")
            print("   " * width + " * " * offset)
            width -= 2

        height = 5
        offset = 6
        width = 1
        for i in range(height):
            offset -= 1
            for j in range(offset):
                print(" * ", end="")
            print("   " * width + " * " * offset)
            width += 2

    if user_choice == "g":
        # Figure G !!! (working fine) SUPER-DUPER
        height = 5
        for i in range(height):
            offset += 1
            for j in range(offset):
                print(" * ", end="")
            print("   " * width)
            width -= 2

        height = 5
        offset = 6
        width = 1
        for i in range(height):
            offset -= 1
            for j in range(offset):
                print(" * ", end="")
            print("   " * width)
            width += 2

    if user_choice == "h":
        # Figure H !!! (working fine) SUPER-DUPER
        height = 5
        for i in range(height):
            offset += 1
            for j in range(offset):
                print("   ", end="")
            print("   " * width + " * " * offset)
            width -= 2

        height = 5
        offset = 6
        width = 1
        for i in range(height):
            offset -= 1
            for j in range(offset):
                print("   ", end="")
            print("   " * width + " * " * offset)
            width += 2

    if user_choice == "i":
        # Figure I !!! (working fine)
        for i in range(height):
            print(" * " * width)
            width -= 1

    # Figure B
    # for i in range(height):
    #     for j in range(width):
    #         print(" * ", end="")
    #     width += 1
    #     print(" * ")

    # Figure G
    # for i in range(height // 2):
    #     for j in range(width):
    #         print(" * ", end="")
    #     width += 1
    #     print(" * ")
    #
    # for i in range(height // 2 - 1):
    #     width -= 1
    #     for j in range(width - 1):
    #         print(" * ", end="")
    #     print(" * ")

    # Figure C
    # n = 5
    #
    # for i in range(5):
    #     for j in range(width):
    #         print("  ", end="")
    #     width += 1
    #     print("*   " * n)
    #     n -= 1

    if user_choice == "j":
        # Figure J (working fine) SUPER-DUPER
        width = 9
        offset = 0
        height = 5
        for i in range(height):
            offset += 1
            for j in range(offset):
                print("   ", end="")
            print("   " * width + " * " * offset)
            width -= 2

        height = 5
        offset = 6
        width = 1
        for i in range(height):
            offset -= 1
            for j in range(offset):
                print("   ", end="")
            print(" * " * width + " * " * offset)
            width += 2
    if user_choice == "bonus":
        width = 9
        offset = 0
        height = 5
        for i in range(height):
            offset += 1
            for j in range(offset):
                print(" - ", end="")
            print(" * " * width + " - " * offset)
            width -= 2

        height = 5
        offset = 6
        width = 1
        for i in range(height):
            offset -= 1
            for j in range(offset):
                print(" - ", end="")
            print(" * " * width + " - " * offset)
            width += 2

    if user_choice == "exit":
        run = False
