# Це інтеграційний тест для перевірки роботи SQL-запитів у нашому додатку. 
# Він використовує бібліотеку pytest для організації тестів та перевірки результатів.

import pytest
from integration.sql_main import SQLMain
from integration.class_integration import Student

### НАПИСАТИ ТЕСТИ ДЛЯ КЛАСУ SQLMain
@pytest.fixture
def sql_main(tmp_path):
    """
    Фікстура для створення об'єкта SQLMain перед кожним тестом
    Щей використовуємо тимчасову базу даних для тестування.
    """
    return SQLMain(db_path = f"{tmp_path}/test_db.db")

@pytest.mark.parametrize("student", [
    Student(name="Аліна", birthday=2000, city="Київ"),
    Student(name="Марія", birthday=1999, city="Львів"),
    Student(name="Володимир", birthday=2001, city="Одеса")
])
def test_add_student(sql_main, student):
    """
    Тест для перевірки додавання студента до бази даних.
    """
    #ми добавили леше одного студента
    sql_main.add_student(student)
    
    # Перевірка, що студент був доданий
    students = sql_main.list_students_as_table()
    assert len(students) == 1

# План інтеграційного тестування:
# 1. Тестування додавання студентів до бази даних через фікстури.
# 2. Перевірити що у базі даних є цей студент після додавання.
# 3. Дадаємо ще одного студента і перевіряємо що їх вже два.
# 4. Видаляємо тепер двох студентів.
# 5. Перевіряємо що база даних порожня.
# як бачимо інтеграційний тест - це сукупність дій та операцій

@pytest.fixture
def sql_main_with_students(sql_main):
    """
    Фікстура для створення об'єкта SQLMain з попередньо доданими студентами.
    """
    students = [
        Student(name="Аліна", birthday=2000, city="Київ"),
        Student(name="Марія", birthday=1999, city="Львів"),
        Student(name="Володимир", birthday=2001, city="Одеса")
    ]
    for student in students:
        sql_main.add_student(student)
    return sql_main

def test_integration_add_and_delete_students(sql_main_with_students):
    """
    Інтеграційний тест для перевірки додавання та видалення студентів.
    - фікстура буде давати базу яка вже заповнена студентами
    - будемо додавати студентві та видаляти для перевірки правильності операцій
    """
    # Перевірка, що студенти були додані (база даних не порожня)
    initial_students = sql_main_with_students.list_students_as_table()
    number_of_initial_students = len(initial_students)
    assert number_of_initial_students > 0  # Перевірка, що студенти були додані

    # 2. Додаємо ще одного студента
    new_student = Student(name="Олександр", birthday=2002, city="Харків")
    sql_main_with_students.add_student(new_student)
    current_students = sql_main_with_students.list_students_as_table()
    assert len(current_students) == number_of_initial_students + 1  # Перевір
    
    # 3. Видаляємо двох студентів
    sql_main_with_students.delete_student(1)
    sql_main_with_students.delete_student(2)
    current_students = sql_main_with_students.list_students_as_table()
    assert len(current_students) == number_of_initial_students - 1  # Перевірка, що студентів стало менше на 1

    # 4. Видаляємо всіх решта студентів
    for student in current_students:
        # Отримуємо ID студента з рядка таблиці (припускаємо, що ID є в рядку)
        student_id = int(student.split('|')[0].split(':')[1].strip())
        sql_main_with_students.delete_student(student_id)
    
    # 5. Перевірка, що база даних порожня
    students_after_deletion = sql_main_with_students.list_students_as_table()
    assert len(students_after_deletion) == 0
