from .sql_main import SQLMain
from .class_integration import Student

if __name__ == "__main__":
    sql_main = SQLMain()

    for i in range(1, 6):
        student = Student(f"Студент {i}", 20 + i, f"Місто {i}")
        sql_main.add_student(student)
    students = sql_main.list_students_as_table()
    for student in students:
        print(student)
    for student_id in range(1, 6):
        sql_main.delete_student(student_id)
    print("Студенти видалені.", len(sql_main.list_students_as_table()))

