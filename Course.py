from typing import List
from Teacher import Teacher
from Student import Student

# מחלקת קורס (Course)
class Course:
    def __init__(self, name: str, teacher: Teacher, students: List[Student]):
        self.name = name
        self.teacher = teacher
        self.students = students

    def add_student(self, student: Student):
        self.students.append(student)
        print(f"Student {student.name} added to course {self.name}.")

    def check_availability(self):
        print(f"Checking availability for course {self.name}.")

    def manage_registration(self):
        print(f"Managing registration for course {self.name}.")

    def update_course_schedule(self, new_schedule: str):
        print(f"Course {self.name}'s schedule has been updated to {new_schedule}.")

    def cancel_course(self):
        print(f"Course {self.name} has been cancelled.")
