from classes.Person import Person
from classes.Student import Student
from classes.Staff import Staff

class School(Student, Staff):
    def __init__(self, name):
        self.name = name
        self.staff = Staff.all_staff()
        self.students = Student.all_students()

