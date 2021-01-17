class Book:
    name = "default_name"
    year = 0
    publisher = "default_publisher"
    genre = "default_genre"
    author = "some_author"
    price = 0

    def __init__(self, name, year, publisher):
        self.name = name
        self.year = year
        self.publisher = publisher

    def input_genre(self, genre):
        self.genre = genre

    def input_color(self, author):
        self.author = author

    def input_price(self, price):
        self.price = price

    def show_info(self):
        print(f"Book name: {self.name}\nYear: {self.year}\nPublisher: {self.publisher}")
        print(f"Genre: {self.genre}\nAuthor: {self.author}\nPrice: {self.price}")


name = input("Enter a name of book: ")
year = int(input("Enter a year of publishing: "))
publisher = input("Enter a publisher: ")

new_book = Book(name, year, publisher)

edit = True
while edit:
    edit = input("To change a book parameters type:\n[g] - input genre\n"
                 "[a] - input author\n"
                 "[p] - edit price\n"
                 "\tTo see info about book:\n\t[i] - book info\n"
                 "or press [Enter] to exit: ")
    if edit == "g":
        genre = input("Type a genre of a book: ")
        new_book.genre = genre
    elif edit == "a":
        author = input("Type author of a book: ")
        new_book.author = author
    elif edit == "p":
        price = int(input("Enter price of a book: "))
        new_book.price = price
    elif edit == "i":
        new_book.show_info()
