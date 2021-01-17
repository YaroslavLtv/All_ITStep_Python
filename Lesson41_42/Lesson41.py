# Серіалізація і десеріалізація
photo = open("4.png", "rb")

my_photo = photo.read()

photo.close()

new_photo = open("11.png", "wb")
print(type(my_photo))
new_photo.write(my_photo)
new_photo.close()

simple = {"int_list": [1, 2, 3], "text": "string", "number": "3.44", "boolean": True}


import pickle

# pickle.dumps(simple) серіалізація в строку
# pickle.loads(simple) десеріалізація в строку
# pickle.dump(simple) серіалізація в файл
# pickle.load(simple) десеріалізація в файл

print(simple)
print(pickle.dumps(simple))

b_simple = pickle.dumps(simple)
print(simple.__sizeof__())
print(b_simple.__sizeof__())

print(pickle.loads(b_simple))

pickle.dump(simple, open("simple.pkl", "wb"))

x = pickle.load(open("simple.pkl", "rb"))
print(x)
