# Question
<img width="985" alt="Screenshot 2025-02-24 at 2 11 48 PM" src="https://github.com/user-attachments/assets/4ebb0b5f-fe7f-4eb8-838a-b78a4ae561fa" />


# Code

```.python
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}")

class Library:
    def __init__(self):
        self.books = []  # List to store Book objects

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def show_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("\nBooks in the Library:")
            for book in self.books:
                book.display_info()

# Example Usage:
book1 = Book("1984", "George Orwell", "978-0451524935")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "978-0061120084")

library = Library()
library.add_book(book1)
library.add_book(book2)

library.show_books()

```
# Evidence

<img width="1343" alt="Screenshot 2025-02-24 at 9 02 12 PM" src="https://github.com/user-attachments/assets/bb37fce9-b9d5-4572-970b-53e70384b850" />

# UML Diagram

![Screenshot 2025-02-24 at 9 02 55 PM](https://github.com/user-attachments/assets/7ed9d3ca-4424-4c6c-9fe4-203e686c48d4)




