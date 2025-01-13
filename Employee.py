from User import User
# מחלקת עובד כללי (GeneralEmployee) - תורשת מ-User
class Employee(User):
    def __init__(self, name: str, user_id: int, tasks: List[str]):
        super().__init__(name, user_id, role="GeneralEmployee")
        self.tasks = tasks

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
