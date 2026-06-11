# Lab 8: Object-Oriented Programming Review Challenge

from book import Book
import csv

def create_inventory():
    """
    Read books from csv file, create and return a list of Book objects.
    """
    books = []
    with open("../data/booklist.csv") as csvfile:
        reader = csv.reader(open("../data/booklist.csv"))
        for row in reader:
            if reader.line_num == 1:
                continue
            else:
                Boo = Book(row[0], row[1], row[2], row[3], row[4], row[5])
                books.append(Boo)
    return books


def print_inventory(books):
    """
    Print every book in the inventory.
    """
    for book in books:
        print (book)


def total_inventory(books):
    """
    Return the total number of all books in inventory.
    """


def find_by_author(books, author):
    """
    Return a list of books written by the specified author.
    """
    author_list = []
    for book in books:
        if book.author == author:
            author_list.append(book)
    return author_list



def find_low_stock(books, threshold):
    """
    Return a list of books whose quantity is less than or equal to threshold.
    """
    low_list = []
    for book in books:
        if book.stock < threshold:
            low_list.append(book)
    return low_list


def print_books(books):
    """
    Print a list of books.
    """
    for book in books:
        print(book)


def main():
    inventory = create_inventory()

    print("Full Inventory")
    print("--------------")
    print_inventory(inventory)

    print()
    print("Total inventory:", total_inventory(inventory))

    print()
    print("Books by Octavia Butler")
    print("-----------------------")
    print_books(find_by_author(inventory, "Octavia Butler"))

    print()
    print("Low Stock Books")
    print("---------------")
    print_books(find_low_stock(inventory, 3))

    print()
    print("Sorted by Title")
    print("---------------")
    sorted_books = sorted(inventory)
    print_books(sorted_books)


main()
