from book import Book, BookState
from student import Student

class Library:
    def __init__(self, name: str):
        self.name = name
        self.books: list[Book] = []
        self.readers: list[Student] = []

    def add_book(self, book: Book):
        """Add a book to the library."""
        self.books.append(book)

    def remove_book(self, book):
        """Remove a book from the library if it exists."""
        if book in self.books:
            self.books.remove(book)

    def list_books(self):
        """Return a list of all books in the library."""
        return self.books
    
    def list_available_books(self):
        """Return a list of all available books in the library."""
        return [book for book in self.books if book.state == BookState.AVAILABLE]
    
    def display_books(self):
        """Display all books in the library."""
        for book in self.books:
            print(book)
    
    def register_reader(self, reader: Student):
        """Register a new reader (student) in the library."""
        self.readers.append(reader)
    
    def display_readers(self):
        """Display all registered readers."""
        for reader in self.readers:
            print(reader)