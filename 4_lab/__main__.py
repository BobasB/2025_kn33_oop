from book import Book

if __name__ == "__main__":
    # Приклад використання
    book_shelf = []
    for name in ["Посібник Python", "Вивчення JavaScript", "Основи C++"]:
        book = Book(title=name, author="Не вказано", year_published=2025)
        book_shelf.append(book)

    for book in book_shelf:
        print(book.description)
