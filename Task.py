# מחלקת משימה (Task)
class Task:
    def __init__(self, description: str, status: str):
        self.description = description
        self.status = status

    def update_status(self, status: str):
        self.status = status
        print(f"Task '{self.description}' status updated to {self.status}.")

    def display_task_info(self):
        print(f"Task Description: {self.description}, Status: {self.status}")

    def assign_task_to_employee(self, employee: GeneralEmployee):
        print(f"Task '{self.description}' has been assigned to employee {employee.name}.")

    def complete_task(self):
        self.status = "Completed"
        print(f"Task '{self.description}' has been completed.")
