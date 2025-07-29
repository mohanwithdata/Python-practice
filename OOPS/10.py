class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        print(f"Book Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year: {self.year}")

title = input("Enter the book title: ")
author = input("Enter the author name: ")
year = input("Enter the year of publication: ")

book = Book(title, author, year)

book.info()