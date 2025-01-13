from User import User
from typing import List


# מחלקת תלמיד (Student) - תורשת מ-User
class Student(User):
    def __init__(self, name: str, user_id: int, schedule: List[str], grades: List[int] = None):
        super().__init__(name, user_id, role="Student")
        self.schedule = schedule
        self.grades = grades if grades else []

    def login(self):
        print(f"Student {self.name} logged in.")

    def create_user(self):
        print(f"Student {self.name} is creating a new user.")

    def update_user_info(self):
        print(f"Student {self.name} is updating user information.")

    def view_schedule(self):
        print(f"Student {self.name}'s schedule: {self.schedule}")

    def view_grades(self):
        print(f"Student {self.name}'s grades: {self.grades}")

    def add_grade(self, grade: int):
        self.grades.append(grade)

    def update_schedule(self, new_schedule: List[str]):
        self.schedule = new_schedule
        print(f"Student {self.name}'s schedule has been updated.")

    def request_leave(self, course: str):
        print(f"Student {self.name} has requested leave from the {course} course.")
