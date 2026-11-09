from .sql_main import SQLMain
from .class_integration import Student

if __name__ == "__main__":
    sql_main = SQLMain()

    for i in range(1, 6):
        student = Student(f"Студент {i}", 20 + i, f"Місто {i}")
        sql_main.add_student(student)
    students = sql_main.list_students()
    for student in students:
        print(student)
