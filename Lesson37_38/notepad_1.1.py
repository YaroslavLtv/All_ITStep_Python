# ЗАПИСЬ МАССИВА В ФАЙЛ
# dictionary = {'a': '1', 'b': '2', 'c': '3'}
# f = open('task7.txt','at')
# for key in dictionary:
#     f.write(f'{key} : {dictionary[key}\n')
# f.close()
# ЧТЕНИЕ МАССИВА В ФАЙЛ
file_name = str(input("Enter file name: "))

a = open(f"{file_name}.txt", "at")
a.close()
while True:
    # Зчитування з текстового файлу в словник
    f = open(f"{file_name}.txt", 'rt')
    l = f.readlines()
    dictionary1 = {}
    for element in l:
        a = element.find(':')
        key = element[:a-1]
        value = element[a+2:-1]
        dictionary1[key] = value
    f.close()
    print(dictionary1)
    while True:
        # Робота зі словником записів
        # k = str(input("Enter key: "))
        # v = str(input("Enter value: "))
        # dictionary1[k] = v
        command = str(input("Enter a command: "))
        if command == "show":
            for key in dictionary1:
                print(f"{key} : {dictionary1[key]}")
        elif command == "create":
            k = str(input("Enter key: "))
            v = str(input("Enter value: "))
            dictionary1[k] = v
        elif command == "update":
            k = str(input("Enter key: "))
            v = str(input("Enter value: "))
            dictionary1[k] = v
        elif command == "delete":
            k = str(input("Enter key: "))
            del dictionary1[k]

        # Exit
        e = str(input("Press any key to continue: "))
        if not e:
            break

    # ЗАПИСЬ МАССИВА В ФАЙЛ
    f = open(f"{file_name}.txt", 'wt')
    for key in dictionary1:
        f.write(f'{key} : {dictionary1[key]}\n')
    f.close()

    # Exit all
    e = str(input("Enter any key to continue: "))
    if not e:
        break
