import sqlite3
from .class_integration import Student

class SQLMain:
    """
    Клас для запису студентів до бази даних SQLite.
    """
    def __init__(self, db_path: str = 'students.db'):
        """
        Ініціалізація об'єкта SQLMain.
        """
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        """
        Створює таблицю для збереження студентів у базі даних.
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                birthday INTEGER NOT NULL,
                city TEXT NOT NULL
            )
        ''')
        self.connection.commit()

    def add_student(self, student: Student):
        """
        Додає студента до бази даних.

        :param student: Об'єкт класу Student.
        """
        self.cursor.execute('''
            INSERT INTO students (name, birthday, city)
            VALUES (?, ?, ?)
        ''', (student.get_name, student.birthday, student.city))
        self.connection.commit()

    def list_students(self):
        """
        Повертає список студентів з бази даних.

        :return: Список студентів у форматі "Name: {name}, Age: {age}".
        """
        self.cursor.execute('SELECT name, birthday FROM students')
        students = self.cursor.fetchall()
        return [f"| Імя: {name} | Дата народження: {birthday} |" for name, birthday in students]
