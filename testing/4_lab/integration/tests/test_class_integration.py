from integration.class_integration import Student, Group
import pytest

def test_student_initialization():
    """"
    Це є простий Юніт-тест для перевірки ініціалізації об'єкта класу Student. 
    """
    student = Student("Аліна", 20)
    assert student.get_name == "Аліна"
    assert student.get_age == 20


@pytest.fixture
def student_fixture():
    return Student("Аліна", 20)

def test_student_in_group(student_fixture):
    """
    Це є інтеграційний тест для перевірки взаємодії між класами Student та Group. 
    """
    group = Group("Group A")
    group.add_student(student_fixture)
    students_list = group.get_students()
    assert len(students_list) == 1
    assert students_list[0] == "Name: Аліна, Age: 20"