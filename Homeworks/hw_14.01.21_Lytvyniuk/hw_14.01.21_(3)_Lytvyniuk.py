class Stadium:
    capacity = 0

    @staticmethod
    def change_capacity(capacity):
        Stadium.capacity = capacity

    def __init__(self, name, year, country, city):
        self.city = city
        self.name = name
        self.year = year
        self.country = country

    def change_stadium_name(self, new_name):
        self.name = new_name

    def show_info(self):
        print(f"Stadium name: {self.name}\nYear of the stadium opening: {self.year}\nCountry: {self.country}")
        print(f"City: {self.city}\ncapacity: {self.capacity}\n")


