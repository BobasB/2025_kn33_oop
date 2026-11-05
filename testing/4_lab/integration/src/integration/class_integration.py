

class Student:
    def __init__(self, name: str, birthday: int, city: str):
        self.name = name
        self.birthday = birthday
        self.city = city


    @property
    def get_name(self):
        return self.name

    @property
    def get_age(self):
        return self.age

class Group:
    def __init__(self, group_name: str):
        self.group_name = group_name
        self.students = []

    def add_student(self, student: Student):
        self.students.append(student)
    
    @property
    def get_group_name(self):
        return self.group_name

    def get_students(self):
        list_student_table = [f"Name: {student.get_name}, Age: {student.get_age}" for student in self.students]
        return list_student_table
