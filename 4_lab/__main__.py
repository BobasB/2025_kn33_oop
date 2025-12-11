from book import Book
from library import Library
from student import Student, StudentActions

if __name__ == "__main__":
    # Приклад використання
    library = Library("Бібліотека ІТ Коледжу")
    
    for name in ["Посібник Python", "Вивчення JavaScript", "Основи C++", "Введення в Java",
                 "Розробка на C#", "Програмування на Ruby"]:
        book = Book(title=name, author="Не вказано", year_published=2025)
        library.add_book(book)

    print("Всі книги в бібліотеці:")
    library.display_books()

    for name in ["Маркіян", "Юрій", "Анна"]:
        student = Student(first_name=name, last_name="Прізвище")
        library.register_reader(student)
    
    print("\nЗареєстровані читачі:")
    library.display_readers()


    # Симулюємо роботу бібліотеки впродовж 30 днів
    import random
    for day in range(1, 31):
        print(f"\n--- День {day} ---")
        student = random.choice(library.readers)
        book = random.choice(library.books)
        action = random.choice(list(StudentActions))
        if action == StudentActions.BORROW:
            student.borrow_book(book)
        elif action == StudentActions.RETURN:
            student.return_book()
