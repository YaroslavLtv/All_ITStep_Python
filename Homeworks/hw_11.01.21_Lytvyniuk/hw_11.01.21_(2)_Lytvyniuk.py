class Book:
    name = "default_name"
    year = 0
    publisher = "default_publisher"
    genre = "default_genre"
    author = "some_author"
    price = 0

    def __init__(self, name):
        self.name = name

