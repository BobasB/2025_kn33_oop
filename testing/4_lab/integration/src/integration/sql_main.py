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

    def delete_student(self, student_id: int):
        """
        Видаляє студента з бази даних за його ID.

        :param student_id: ID студента для видалення.
        """
        self.cursor.execute('DELETE FROM students WHERE id = ?', (student_id,))
        self.connection.commit()

    def list_students_as_table(self):
        """
        Повертає список студентів з бази даних.

        :return: Список студентів у форматі "ID: {id} | Імя: {name} | Дата народження: {birthday} |".
        """
        self.cursor.execute('SELECT id, name, birthday FROM students')
        students = self.cursor.fetchall()
        return [f"ID: {id} | Імя: {name} | Дата народження: {birthday} |" for id, name, birthday in students]

    def get_student_record_by_id(self, student_id: int):
        """
        Повертає студента з бази даних за його ID.

        :param student_id: ID студента для пошуку.
        :return: Студент у форматі "ID: {id} | Імя: {name} | Дата народження: {birthday} |" або None, якщо студент не знайдений.
        """
        self.cursor.execute('SELECT id, name, birthday FROM students WHERE id = ?', (student_id,))
        student = self.cursor.fetchone()
        if student:
            student_id, name, birthday = student
            return f"ID: {student_id} | Імя: {name} | Дата народження: {birthday} |"
        return None