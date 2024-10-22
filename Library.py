# Library Management System

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book_name, author, quantity):
        if book_name in self.books:
            print(f"{book_name} already exists. Use update_quantity() to update it.")
        else:
            self.books[book_name] = {'author': author, 'quantity': quantity}
            print(f"{book_name} by {author} added to the library.")

    def view_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print("\nAvailable Books:")
            for book_name, details in self.books.items():
                print(f"Book: {book_name}, Author: {details['author']}, Quantity: {details['quantity']}")

    def borrow_book(self, book_name):
        if book_name in self.books:
            if self.books[book_name]['quantity'] > 0:
                self.books[book_name]['quantity'] -= 1
                print(f"You have borrowed {book_name}.")
            else:
                print(f"{book_name} is out of stock.")
        else:
            print(f"{book_name} not found in the library.")

    def return_book(self, book_name):
        if book_name in self.books:
            self.books[book_name]['quantity'] += 1
            print(f"Thank you for returning {book_name}.")
        else:
            print(f"{book_name} does not belong to this library.")

    def update_quantity(self, book_name, quantity):
        if book_name in self.books:
            self.books[book_name]['quantity'] += quantity
            print(f"{book_name} quantity updated.")
        else:
            print(f"{book_name} not found in the library.")


# Example usage
library = Library()

# Adding books
library.add_book('Python Programming', 'John Smith', 5)
library.add_book('Data Science Essentials', 'Jane Doe', 3)

# Viewing books
library.view_books()

# Borrowing a book
library.borrow_book('Python Programming')

# Returning a book
library.return_book('Python Programming')

# Updating quantity
library.update_quantity('Data Science Essentials', 2)

# Final library view
library.view_books()