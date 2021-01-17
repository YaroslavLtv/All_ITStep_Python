class Book:
    name = "default_name"
    year = 0
    publisher = "default_publisher"
    genre = "default_genre"
    author = "some_author"
    price = 0
    country_index = "978"
    publisher_index = "617-12"
    count_of_books = 0

    @staticmethod
    def change_publisher_index(new_publisher_index):
        Book.publisher_index = new_publisher_index

    def __init__(self, name, year, publisher):
        self.country_index = Book.country_index
        self.publisher_index = Book.publisher_index
        self.name = name
        self.year = year
        self.publisher = publisher
        Book.count_of_books += 1
        self.s_n = Book.count_of_books
        self.isbn = "ISBN" + " " + self.country_index + "-" + Book.publisher_index + "-" + str(self.s_n)

    def input_genre(self, genre):
        self.genre = genre

    def input_author(self, author):
        self.author = author

    def input_price(self, price):
        self.price = price

    def change_country_index(self, new_country_index):
        self.country_index = new_country_index

    def show_info(self):
        print(f"Book name: {self.name}\nYear: {self.year}\nPublisher: {self.publisher}")
        print(f"Genre: {self.genre}\nAuthor: {self.author}\nPrice: {self.price}\nISBN: {self.isbn}")


book_1 = Book("surgeon", 2001, "KSM")
book_2 = Book("Body Double", 2004, "KSM")
book_1.input_genre("A Novel")
book_1.input_author("Tess Gerritsen")
book_1.input_price(100)
book_2.input_genre("A Novel")
book_2.input_author("Tess Gerritsen")
book_2.input_price(110)
book_1.show_info()
print()
book_2.show_info()
print()
Book.change_publisher_index("966-948")
book_1.input_price(115)
book_1.show_info()
print()
book_2.show_info()

book_3 = Book("One of us is lying", 2004, "KM-Books")
book_3.input_genre("A Novel")
book_3.input_author("Karen M. McManus")
book_3.input_price(120)
print()
book_3.show_info()