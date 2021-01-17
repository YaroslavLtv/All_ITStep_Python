import pickle
# notes = {"Yaroslav": {1: "a", 2: "b", 3: "c"}, "sten": {4: "a", 5: "b", 6: "c"}}
#
# pickle.dump(notes, open("notes.pkl", "wb"))
#
# x = pickle.load(open("notes.pkl", "rb"))
# print(x)

'''Задание 1
Есть некоторый словарь, который хранит названия
стран и столиц. Название страны используется в качестве
ключа, название столицы в качестве значения. Необходимо
реализовать: добавление данных, удаление данных, поиск
данных, редактирование данных, сохранение и загрузку
данных (используя упаковку и распаковку).'''

# notes = {}
# while True:
#     # CRUD
#     # pickle.dump(notes, open("notes.pkl", "wb"))
#     notes = pickle.load(open("notes.pkl", "rb"))
#     command = str(input("Enter command: "))
#     if command == "create":
#         country = str(input("Enter name of country: "))
#         capital = str(input("Enter name of capital: "))
#         notes[country] = capital
#     elif command == "read":
#         print(notes)
#     elif command == "update":
#         country = str(input("Enter name of country: "))
#         capital = str(input("Enter name of capital: "))
#         notes[country] = capital
#     elif command == "delete":
#         country = str(input("Enter name of country: "))
#         del notes[country]
#     pickle.dump(notes, open("notes.pkl", "wb"))
file_name = "notes.pkl"
# notes = {}
while True:
    # CRUD
    # pickle.dump(notes, open("notes.pkl", "wb"))
    notes = pickle.load(open(file_name, "rb"))
    command = str(input("Enter command: "))
    if command == "create":
        country = str(input("Enter name of country: "))
        capital = str(input("Enter name of capital: "))
        notes[country] = capital
    elif command == "read":
        print(notes)
    elif command == "update":
        country = str(input("Enter name of country: "))
        capital = str(input("Enter name of capital: "))
        notes[country] = capital
    elif command == "delete":
        country = str(input("Enter name of country: "))
        del notes[country]
    elif command == "create new":
        file_name = ""
        file_name = str(input("Enter name of file: "))

    pickle.dump(notes, open(file_name, "wb"))
