# d = {}
# d = dict()
# d = {"a": 1, "b": 2}
# d["c"] = 3
# print(d)
#
# for a in d:
#     print(a, d[a])
#
# print(d.values())
# print(d.keys())
# print(d.items())
#
# dk = list(d.keys())
# dv = list(d.values())
# print(dk, dv)
#
# d1 = {}
# for i in range(len(dk)):
#     d1[dk[i]] = dv[i]
#
# print(d1)
#
# d2 = d.copy()
# print(d)
# print(d2)
#
# syn = {'red':'bordo', 'buy':'shop','goodbye':'bye'}
# s = 'buy'
# # print(s in syn)
# if s in syn:
#     print(syn[s])
# else:
#     for key in syn:
#         if syn[key] == s:
#             print(key)

# eng_ukr = {'dog': 'пес', 'cat': 'кіт', 'fish': 'риба'}
# user_word = input("Enter word to translate: ")
#
# if user_word in eng_ukr:
#     print(eng_ukr[user_word])
# else:
#     for key in eng_ukr:
#         if eng_ukr[key] == user_word:
#             print(key)

countries = {'Ukraine': ['Kyiv', 'Lviv', 'Rivne'], 'Poland': ['Warsaw', 'Krakow']}
in_country = input("Enter country name: ")
add_city = input("Enter a name of city: ")

# for country in countries:
#     print(country)
#     for city in countries[country]:
#         print(city, end=" ")
#     print()

for country in countries:
    if in_country == country:
        countries[country].append(add_city)
print(countries)