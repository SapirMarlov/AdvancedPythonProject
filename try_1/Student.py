from User import User, UserRole
from typing import List, Dict

# מחלקת תלמיד (Student) - תורשת מ-User
class Student(User):
    def __init__(self, name: str,age:int, user_id: int, schedule: List[str], grades: Dict[int, int] = None):
        super().__init__(name, age, user_id, role=UserRole.STUDENT)
        self.schedule = schedule
        self.grades = grades if grades else {} # this grades has key=courseID and value=grade

    ####################### Start OF GETTERS AND SETTERS #############################################################

    # גטר עבור schedule
    @property
    def schedule(self):
        return self._schedule

    # סטר עבור schedule
    @schedule.setter
    def schedule(self, schedule: List[str]):
        if not all(isinstance(item, str) for item in schedule):
            raise ValueError("Schedule items must be strings.")
        self._schedule = schedule

    # גטר עבור grades
    @property
    def grades(self):
        return self._grades

    # סטר עבור grades
    @grades.setter
    def grades(self, grades: Dict[int, int]):
        if not all(isinstance(course_id, int) and isinstance(grade, int) and 0 <= grade <= 100 for course_id, grade in grades.items()):
            raise ValueError("Grades must be a dictionary where the key is a course ID and the value is an integer grade between 0 and 100.")
        self._grades = grades

    ####################### END OF GETTERS AND SETTERS #############################################################

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

    def add_grade(self, course_id: int, grade: int):
        if 0 <= grade <= 100:
            self.grades[course_id] = grade
            print(f"Added grade {grade} for course {course_id} for student {self.name}.")
        else:
            print("Grade must be between 0 and 100.")

    def update_schedule(self, new_schedule: List[str]):
        self.schedule = new_schedule
        print(f"Student {self.name}'s schedule has been updated.")

    def request_leave(self, course: str):
        print(f"Student {self.name} has requested leave from the {course} course.")

    ####################### Start OF STR METHOD #############################################################

    # __str__: מייצרת תיאור מובן של התלמיד
    def __str__(self):
        user_str = super().__str__()  # פונה ל-__str__ של User
        schedule_str = ", ".join(self.schedule) if self.schedule else "No schedule assigned"
        grades_str = ", ".join([f"Course {course_id}: {grade}" for course_id, grade in self.grades.items()]) if self.grades else "No grades available"
        return f"Student [ {user_str}, Schedule: {schedule_str}, Grades: {grades_str} ]"
