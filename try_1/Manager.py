from typing import List
from User import User, UserRole
from Task import Task

# מחלקת מנהל (Admin) - תורשת מ-User
class Manager(User):
    def __init__(self, name: str,age:int, user_id: int, task_for_employee: List[Task] ,income:int , outcome:int):
        super().__init__(name, age, user_id=user_id, role=UserRole.MANAGER)
        self._task_for_employee = task_for_employee  # רשימת משימות עבור העובד
        self._income = income
        self._outcome = outcome

    ####################### Start OF GETTERS AND SETTERS #############################################################

    # גטר עבור task_for_employee
    @property
    def task_for_employee(self):
        return self._task_for_employee

    # סטר עבור task_for_employee
    @task_for_employee.setter
    def task_for_employee(self, task_for_employee: List[Task]):
        if not all(isinstance(task, Task) for task in task_for_employee):
            raise ValueError("Each task must be an instance of Task.")
        self._task_for_employee = task_for_employee


    # גטר עבור income
    @property
    def income(self):
        return self._income

    # סטר עבור income
    @income.setter
    def income(self, income: int):
        if not isinstance(income, int) :
            raise ValueError("Income must be a non-negative integer.")
        self._income = income

    # גטר עבור outcome
    @property
    def outcome(self):
        return self._outcome

    # סטר עבור outcome
    @outcome.setter
    def outcome(self, outcome: int):
        if not isinstance(outcome, int) or outcome <= 0:
            raise ValueError("Outcome must be a positive integer greater than 0.")
        self._outcome = outcome
    ####################### END OF GETTERS AND SETTERS #############################################################

    def login(self):
        print(f"Admin {self.name} logged in.")

    def create_user(self):
        print(f"Admin {self.name} is creating a new user.")

    def update_user_info(self):
        print(f"Admin {self.name} is updating user information.")

    def create_course(self):
        print(f"Admin {self.name} is creating a new course.")

    def assign_teacher(self):
        print(f"Admin {self.name} is assigning a teacher to a course.")

    def manage_students(self):
        print(f"Admin {self.name} is managing students.")

    def manage_financial_reports(self):
        print(f"Admin {self.name} is managing financial reports.")

    def generate_reports(self):
        print(f"Admin {self.name} is generating reports.")

    ####################### Start OF STR METHOD #############################################################

    # __str__: מייצרת תיאור מובן של המנהל, כולל המשימות
    def __str__(self):
        user_str = super().__str__()  # פונה ל-__str__ של User
        tasks_str = ", ".join([str(task.description) for task in self.task_for_employee]) if self.task_for_employee else "No tasks assigned"
        return f"Manager [ {user_str}, Tasks: {tasks_str} ]"
