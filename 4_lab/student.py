from book import Book, BookState
from enum import Enum

class StudentActions(Enum):
    BORROW = "взяв"
    RETURN = "повернув"

class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = id(self)  # Унікальний номер студентського квитка
        self.borrowed_books: list[Book] = []

    def borrow_book(self, book: Book):
        if book.state != BookState.AVAILABLE:
            print(f"{self.first_name} не може взяти книгу '{book.title}', Бо взята {book.borrower.first_name}.")
            return
        book.set_who_borrowed(self)
        self.borrowed_books.append(book)
        print(f"{self.first_name} взяв книгу '{book.title}'.")
    
    def return_book(self):
        if not self.borrowed_books:
            print(f"{self.first_name} не має книг для повернення.")
            return
        book = self.borrowed_books.pop()
        book.set_release_borrower()
        print(f"{self.first_name} повернув книгу '{book.title}'.")
    
    def __str__(self):
        return f"Студент: {self.first_name} {self.last_name} (ID: {self.student_id})"
