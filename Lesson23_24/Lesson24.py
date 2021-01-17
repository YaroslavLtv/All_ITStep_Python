# Global

# num = [1, 2, 3]
# name = "Yarek"
#
# def add()
#     # Local
#     name = "Sten"
#     num.append(4)
#
# add()
#
# print(num)

x = 10
y = 20

def outer():
    global z
    z = 30
    a = 5
    def inner():
        nonlocal a
        x = 30
        a = 10
        print(f"x is {x}")
        print(f"z is {z}")
        print(f"y is {y}")
        print(len("abc"))
    inner()
    print(f"Nonlocal a = {a}")
outer()

print(f"x = {x}, y = {y}, z = {z}")