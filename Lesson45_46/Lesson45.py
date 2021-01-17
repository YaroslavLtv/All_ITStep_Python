exercise = True
while exercise:
    exercise = input("Enter number of exercise or press enter to exit: ")
    '''1. Напишите программу, которая получает длины двух катетов в 
    прямоугольном треугольнике и выводит его площадь. Каждое число записано 
    в отдельной строке.'''
    if exercise == "1":
        side_1 = int(input("Enter first side of triangle: "))
        side_2 = int(input("Enter second side of triangle: "))
        triangle_area = (side_1*side_2)/2
        print(f"The area of triangle equals to: {triangle_area}")
    if exercise == "2":
        '''2. В школе решили набрать три новых математических класса. 
        Так как занятия по математике у них проходят в одно и то же время, 
        было решено выделить кабинет для каждого класса и купить в них новые парты. 
        За каждой партой может сидеть не больше двух учеников. Известно количество учащихся 
        в каждом из трёх классов. Сколько всего нужно закупить парт чтобы их хватило на 
        всех учеников? Программа получает на вход три натуральных числа: количество учащихся 
        в каждом из трех классов.'''
        students_1 = int(input("Enter number of students in first class: "))
        students_2 = int(input("Enter number of students in second class: "))
        students_3 = int(input("Enter number of students in third class: "))

        def calc_desks(num_of_students):
            school_desk = num_of_students // 2
            if num_of_students % 2 >= 0.5:
                school_desk += 1
            return school_desk
        sum_of_desks = calc_desks(students_1) + calc_desks(students_2) + calc_desks(students_3)
        print(f"{sum_of_desks} school desks is needed")
    if exercise == "3":
        '''3. Даны три целых числа. Определите, сколько среди них совпадающих. 
        Программа должна вывести одно из чисел: 3 (если все совпадают), 
        2 (если два совпадает) или 0 (если все числа различны).'''
        counter = 0
        list_of_numbers = []
        for i in range(3):
            user_number = int(input("Enter number: "))
            list_of_numbers.append(user_number)

        for i in range(len(list_of_numbers)):
            if list_of_numbers[-i] == list_of_numbers[-i-1]:
                counter += 1

        if counter == 0:
            print("All numbers is different")
        elif counter == 1:
            print("Here is two similar numbers")
        else:
            print("All numbers the same")

    if exercise == "4":
        '''4. Дано натуральное число. Требуется определить, является ли год с данным номером 
        високосным. Если год является високосным, то выведите YES, иначе выведите NO. Напомним, 
        что в соответствии с григорианским календарем, год является високосным, если его номер 
        кратен 4, но не кратен 100, а также если он кратен 400.'''
        users_year = int(input("Enter a year: "))
        if users_year % 4 == 0 or users_year % 400 == 0:
            if users_year % 100 != 0:
                print("Yes")
        else:
            print("No")
    if exercise == "5":
        '''5. Дано положительное действительное число X. 
        Выведите его первую цифру после десятичной точки.'''
        user_num = input("Enter a number with float point: ")
        num_after_point = user_num.split(".", 1)
        print(num_after_point[1][0])
    if exercise == "6":
        '''6. Факториалом числа n называется произведение 1 × 2 × ... × n. Обозначение: n!'''
        user_number = int(input("Enter a number: "))
        factorial = 1
        for i in range(1, user_number):
            factorial *= i + 1
        print(f"factorial of number ({user_number})! is {factorial}")
