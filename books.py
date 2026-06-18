class Book:
    # Class variable to track total books created
    total_books = 0

    def __init__(self, book_id, title, author, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.copies = copies

        # Increase total_books whenever a new book object is created
        Book.total_books += 1

    def borrow_book(self):
        if self.copies > 0:
            self.copies -= 1
            print(f"You have borrowed '{self.title}'.")
        else:
            print(f"Sorry, '{self.title}' has no available copies.")

    def return_book(self):
        self.copies += 1
        print(f"You have returned '{self.title}'.")

    def display_book_info(self):
        print("\n--- Book Details ---")
        print(f"Book ID: {self.book_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Available Copies: {self.copies}")

    @classmethod
    def display_total_books(cls):
        print(f"\nTotal books registered in the system: {cls.total_books}")


# 1. Create at least four book objects
book1 = Book("B001", "Python Basics", "John Doe", 3)
book2 = Book("B002", "Data Structures", "Jane Smith", 2)
book3 = Book("B003", "Database Systems", "Mark Lee", 1)
book4 = Book("B004", "Networking", "Sarah Kim", 4)

# 2. Borrow and return books
book1.borrow_book()
book2.borrow_book()
book3.borrow_book()

book1.return_book()
book3.borrow_book()

# 3. Display details of all books
book1.display_book_info()
book2.display_book_info()
book3.display_book_info()
book4.display_book_info()

# 4. Display total books in system
Book.display_total_books()