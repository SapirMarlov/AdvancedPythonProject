from typing import List
from User import User, UserRole
from Task import Task

# מחלקת עובד כללי (GeneralEmployee) - תורשת מ-User
class Employee(User):
    def __init__(self, name: str,age : int, user_id: int, tasks: List[Task]):
        super().__init__(name, age, user_id=user_id, role=UserRole.EMPLOYEE)
        self._tasks = tasks  # רשימת משימות של העובד

    ####################### Start OF GETTERS AND SETTERS #############################################################

    # גטר עבור tasks
    @property
    def tasks(self):
        return self._tasks

    # סטר עבור tasks
    @tasks.setter
    def tasks(self, tasks: List[str]):
        if not all(isinstance(task, Task) for task in tasks):
            raise ValueError("Each task must be a string.")
        self._tasks = tasks

    ####################### END OF GETTERS AND SETTERS #############################################################

    def login(self):
        print(f"General Employee {self.name} logged in.")

    def create_user(self):
        print(f"General Employee {self.name} is creating a new user.")

    def update_user_info(self):
        print(f"General Employee {self.name} is updating user information.")

    def update_task_status(self, task: str, status: str):
        print(f"General Employee {self.name} updated task '{task}' status to {status}.")

    def report_maintenance_issues(self):
        print(f"General Employee {self.name} is reporting maintenance issues.")

    def maintain_equipment(self, equipment: str):
        print(f"General Employee {self.name} is maintaining the {equipment}.")

    ####################### Start OF STR METHOD #############################################################

    # __str__: מייצרת תיאור מובן של העובד, כולל המשימות
    def __str__(self):
        user_str = super().__str__()  # פונה ל-__str__ של User
        tasks_str = ", ".join([str(task) for task in self.tasks]) if self.tasks else "No tasks assigned"
        return f"Employee [ {user_str}, Tasks: {tasks_str} ]"