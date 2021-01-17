# import pickle
#
# import json
# simple = {"name": "Yaroslav", "is_student": True, "age": 33, "l": [1, 2, 3, 4, 5]}
# print(simple, simple.__sizeof__())
# print(json.dumps(simple), json.dumps(simple).__sizeof__())
#
# json.dump(simple, open("simple.test", "wb"))

# class A:
#     def __str__(self):
#         return "Hello World"
#
# a = A()
#
# s = pickle.dumps(a)
# print(s)
# print(pickle.loads(s))

# try except else finally
a = 5
b = 0
try:
    print(a/b)
except ZeroDivisionError:
    print("Divide on Zero")
except ArithmeticError:
    print("Math error")
except TypeError:
    print("TypeError")
except BaseException:
    print("Something go wrong")
except:
    print("Oooops...")


number = 0
while number != 20:
    try:
        number = input("Enter number: ")
        number = int(number)
    except:
        continue
print(number)