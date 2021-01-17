
class Human:
    name = "no_named"
    date_of_birth = "date"
    tel = "phone_number"
    city = "city_name"
    country = "country_name"
    address = "address"
    job = "no_job"

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"name: {self.name}, phone:{self.phone}"

    def change_country(self, country):
        self.country = country

    def change_address(self, address):
        self.address = address

    def change_city(self, city):
        self.city = city


class Man(Human):
    gender = "male"

    def __str__(self):
        return f"name: {self.name}, gender: {self.gender}"


class Woman(Human):
    gender = "female"


sten = Man("Sten", "+380671112233")
print(sten)

jenny = Woman("Jenny", "+380501112233")
print(jenny, jenny.gender)

print(sten)


class City:
    name = "city_name"
    region = "city_region"
    country = "country_of_city"
    population = "city_population"
    postal_code = "postal_code"
    tel_code = "tel_code"

    def __init__(self, name, region, country):
        self.name = name
        self.region = region
        self.country = country

    def __str__(self):
        if self.name:
            return f"City name: {self.name}\nCity Region: {self.region}"
        else:
            return "No name"

    def change_postal_code(self, postal_code):
        self.postal_code = postal_code


class Industrial(City):
    family = "produce"
    count_of_factories = 4
    length_of_roads = 1
    capacity_of_workers = 50

    def __init__(self, count_of_factories, length_of_roads, capacity_of_workers):
        self.count_of_factories = count_of_factories
        self.length_of_roads = length_of_roads
        self.capacity_of_workers = capacity_of_workers

    def change_fields(self, count_of_factories):
        if self.count_of_factories:
            self.count_of_factories = count_of_factories


class Resort(City):
    family = "rest"
    count_of_hotels = 5
    count_of_swim_pools = 2
    count_of_courts = 1

    def __init__(self, count_of_hotels, count_of_swim_pools, count_of_courts):
        self.count_of_hotels = count_of_hotels
        self.count_of_swim_pools = count_of_swim_pools
        self.count_of_courts = count_of_courts

    def change_fields(self, count_of_swim_pools):
        if self.count_of_swim_pools:
            self.count_of_swim_pools = count_of_swim_pools


dnipro = Industrial(3, 2, 4)

dnipro.change_fields(5)
print(dnipro.count_of_factories)


class RealCity(Industrial, Resort):
    def building(self, amount):
        if self.family == "produce":
            self.count_of_factories = self.count_of_factories + amount
        elif self.family == "rest":
            self.count_of_hotels = self.count_of_hotels + amount


lviv = RealCity(10, 850, 20000)
print(lviv.family, lviv.count_of_hotels, lviv.count_of_factories, lviv.length_of_roads)
lviv.family = "rest"

lviv.building(15)
print(lviv.family, lviv.count_of_hotels, lviv.count_of_factories, lviv.length_of_roads)