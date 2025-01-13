# מחלקת מורה (Teacher) - תורשת מ-User
from User import User


class Teacher(User):
    def __init__(self, name: str, user_id: int, courses: List[str]):
        super().__init__(name, user_id, role="Teacher")
        self.courses = courses
        self.students = []

    def login(self):
        print(f"Teacher {self.name} logged in.")

    def create_user(self):
        print(f"Teacher {self.name} is creating a new user.")

    def update_user_info(self):
        print(f"Teacher {self.name} is updating user information.")

    def assign_grades(self, student: Student, grade: int):
        student.add_grade(grade)
        print(f"Teacher {self.name} assigned grade {grade} to {student.name}.")

    def report_class_issues(self):
        print(f"Teacher {self.name} is reporting issues in the class.")

    def manage_attendance(self, student: Student, status: str):
        print(f"Teacher {self.name} recorded {student.name}'s attendance as {status}.")

    def update_course_material(self, course: str):
        print(f"Teacher {self.name} is updating the material for the {course} course.")
