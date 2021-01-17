# ctrl + alt + l
# name = str(input("Enter your name : "))
# age = int(input("Enter your age : "))
# color = str(input("Enter your favorite color : "))
# print("Hello ", name, "i see you big boy. You are ", age, "Years old.", color, " Is your favorite")
# print("Hello " + name + "i see you big boy. You are " + str(age) + "Years old." + color + " Is your favorite")
# print(f"Hello {name} i see you big boy. You are {age} Years old, {color} is your favorite color")

# Правила найменувань змінних
# camelCase Прийнято писати в JavaScript стандартом PEP
# snake_style прийнято стандартом PEP писати в Python
# simplestyle поганий приклад

# Назви змінних можна писати з ВЕЛИКОЇ букви, використовувати малі букви, цифри, нижнє підкреслення всередині назви

# user_age = int(input("Enter your age : "))

user_name = str(input("Enter your name : "))
user_pet = str(input(f"{user_name}, do you have a pet? Who is this? "))
color_of_pet = str(input(f"{user_name}, what color is your {user_pet} ?"))
print(f"O, it's good {user_name} i like {color_of_pet} {user_pet}'s")
