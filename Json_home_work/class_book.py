class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Year: {self.year}")

    def change_year(self, new_year):
        self.year = new_year
        print(f"Year has been updated to {self.year}")