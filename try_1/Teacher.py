from typing import List
from Student import Student
from User import User , UserRole


class Teacher(User):
    def __init__(self, name: str,age:int, user_id: int, courses: List[int], students: List[Student]):
        super().__init__(name,age, user_id, role=UserRole.TEACHER)
        self.courses = courses # id of courses
        self.students = students if students else [] # id of students

    ####################### Start OF GETTERS AND SETTERS #############################################################

    # גטר עבור courses
    @property
    def courses(self):
        return self._courses

    # סטר עבור courses
    @courses.setter
    def courses(self, courses: List[int]):
        if not all(isinstance(course, int) for course in courses):
            raise ValueError("Courses must be a list of integers representing course IDs.")
        self._courses = courses

    # גטר עבור students
    @property
    def students(self):
        return self._students

    # סטר עבור students
    @students.setter
    def students(self, students: List[Student]):
        if not all(isinstance(student, Student) for student in students):
            raise ValueError("Students must be a list of Student objects.")
        self._students = students

    ####################### END OF GETTERS AND SETTERS #############################################################

    # מתודת login
    def login(self):
        print(f"Teacher {self.name} logged in.")

    ####################### Start OF STR METHOD #############################################################

    # __str__: מייצרת תיאור מובן של המורה
    def __str__(self):
        user_str = super().__str__()  # פונה ל-__str__ של User
        courses_str = ", ".join(str(course) for course in self.courses) if self.courses else "No courses assigned"
        students_str = ", ".join(str(student) for student in self.students) if self.students else "No students assigned"
        return f"Teacher [ {user_str}, Courses: {courses_str}, Students: {students_str} ]"
