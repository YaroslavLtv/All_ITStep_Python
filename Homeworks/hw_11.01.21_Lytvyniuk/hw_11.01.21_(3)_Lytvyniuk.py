class Stadium:
    name = "default_name"
    year = 0
    country = "default_country"
    city = "default_city"
    capacity = 0

    def __init__(self, name, year, country):
        self.name = name
        self.year = year
        self.country = country

    def input_city(self, city):
        self.city = city

    def input_capacity(self, capacity):
        self.capacity = capacity

    def show_info(self):
        print(f"Stadium name: {self.name}\nYear of the stadium opening: {self.year}\nCountry: {self.country}")
        print(f"City: {self.city}\ncapacity: {self.capacity}\n")


name = input("Enter a name of stadium: ")
year = int(input("Enter a year of stadium opening: "))
country = input("Enter a country of stadium location: ")

new_stadium = Stadium(name, year, country)

edit = True
while edit:
    edit = input("To change a stadium parameters type:\n[c] - input city of location\n"
                 "[ca] - input capacity of stadium\n"
                 "\tTo see info about stadium:\n\t[i] - stadium info\n"
                 "or press [Enter] to exit: ")
    if edit == "c":
        city = input("Type a location of stadium: ")
        new_stadium.input_city(city)
    elif edit == "ca":
        capacity = input("Type capacity of stadium: ")
        new_stadium.input_capacity(capacity)
    elif edit == "i":
        new_stadium.show_info()
