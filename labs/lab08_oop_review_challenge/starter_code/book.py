# Lab 8: OOP Review Challenge


class Book:
    def __init__(self, title, author, year, genre, pages, rating):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.pages = pages
        self.rating = rating
        self.stock = 0

    def add_stock(self, amount):
        """
        Increase quantity by amount.
        """
        self.stock += amount

    def sell_copies(self, amount):
        """
        Decrease quantity by amount if enough copies are available.

        Return True if the sale succeeds.
        Return False otherwise.
        """
        if self.stock >= amount:
            return True
        else:
            return False

    def __str__(self):
        return (f'{self.title} by {self.author} ({self.year}) - {self.genre}, {self.pages} pages, rating: {self.rating} Stock: {self.stock}')


    def __lt__(self, other):
        """
        Compare books alphabetically by title.
        """
        return self.title < other.title
