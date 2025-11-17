from enum import Enum

class BookState(Enum):
    AVAILABLE = "Доступна"
    BORROWED = "Позичена"
    RESERVED = "Зарезервована"
    LOST = "Втрачена"

class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published
        self.state = BookState.AVAILABLE

    @property
    def description(self):
        return f"Назва: '{self.title}',\n Автор: {self.author},\n Опубліковано в {self.year_published}."
    
    def __str__(self):
        return f"Книга: '{self.title}'"
