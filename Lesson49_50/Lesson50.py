# class Country:
#     name = "default_country"
#     capital = "default"
#     population = 0
#     continent = "Eurasia"
#     tel_code = "+380"
#     cities = []
#
#     def __init__(self, name, capital, population):
#         self.name = name
#         self.capital = capital
#         self.population = population
#
#     def add_cities(self, city):
#         self.cities.append(city)
#
#     def change_name(self, name):
#         self.name = name
#
#     def output(self):
#         print(f"name: {self.name}, capital: {self.capital}")
#
#
# ukraine = Country("Ukraine", "Kyiv", 39)
# ukraine.add_cities("Kyiv")
# ukraine.add_cities("Lviv")
# print(ukraine.cities)

class Country:
    countries = {}

    @staticmethod
    def all_countries(name, capital):
        Country.countries[name] = capital

    # Тут при ініціалізації створюються поля (name, capital, cities)
    # в кожному новому об'єкті (в класі вони наперед не визначені)
    def __init__(self, name_1, capital_1):
        self.name = name_1
        self.capital = capital_1
        # Тут ми в класі прописуємо всі створені раніше
        # об'єкти-країни з їхніми столицями, тому в кожній крайні, старій
        # і новоствореній будуть всі інші країни зі столицями
        Country.countries[name_1] = capital_1
        self.cities = {}

    def new_city(self, city_name, population):
        self.cities[city_name] = population


ukraine = Country("Ukraine", "Kyiv")
poland = Country("Poland", "Warszaw")
ukraine.new_city("Odesa", 2000000)
ukraine.new_city("Lviv", 1300000)
print(ukraine.cities)
print(Country.countries)
ukraine.countries = "no"  # В такому випадку поле countries в об'єкті ukraine обнуляться (лише в об'єкті ukraine)
usa = Country("USA", "WashingtonDC")
print(poland.countries)
print(ukraine.countries)
print(usa.countries)


class Factions:
    numerator = 0
    denominator = 0

    def __init__(self, meat):
        # "2/5"
        self.numerator = int(meat[:meat.find('/')])
        self.denominator = int(meat[meat.find('/')+1:])

    def change_numerator(self, numerator):
        self.numerator = numerator

    def change_denominator(self, denominator):
        self.denominator = denominator

    def divide(self):
        result = self.numerator / self.denominator
        return result


h = Factions(str(input("Enter faction: ")))
print(h.divide())
