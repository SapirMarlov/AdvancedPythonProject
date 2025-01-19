from enum import Enum

# הגדרת אינאם עבור סטטוס המשימה
class TaskStatus(Enum):
    COMPLETED = "Completed"
    NOT_COMPLETED = "Not Completed"
    IN_PROGRESS = "In Progress"

# מחלקת משימה (Task)
class Task:
    def __init__(self, task_id: int, description: str, status: TaskStatus = TaskStatus.NOT_COMPLETED):
        self._task_id = task_id
        self._description = description
        self._status = status

    ####################### Start OF GETTERS AND SETTERS #############################################################

    # גטר עבור task_id
    @property
    def task_id(self):
        return self._task_id

    # סטר עבור task_id
    @task_id.setter
    def task_id(self, task_id: int):
        if not isinstance(task_id, int) or task_id <= 0:
            raise ValueError("Task ID must be a positive integer.")
        self._task_id = task_id

    # גטר עבור description
    @property
    def description(self):
        return self._description

    # סטר עבור description
    @description.setter
    def description(self, description: str):
        if len(description) <= 6 or isinstance(description, str):
            raise ValueError("Description must be more than 6 characters.")
        self._description = description

    # גטר עבור status
    @property
    def status(self):
        return self._status

    # סטר עבור status
    @status.setter
    def status(self, status: TaskStatus):
        if not isinstance(status, TaskStatus):
            raise ValueError("Status must be an instance of TaskStatus Enum.")
        self._status = status

    ####################### END OF GETTERS AND SETTERS #############################################################

    def update_status(self, status: TaskStatus):
        self.status = status
        print(f"Task '{self.description}' status updated to {self.status.value}.")

    def display_task_info(self):
        print(f"Task ID: {self.task_id}, Description: {self.description}, Status: {self.status.value}")

    def assign_task_to_employee(self, employee):
        print(f"Task '{self.description}' has been assigned to employee {employee.name}.")

    def complete_task(self):
        self.status = TaskStatus.COMPLETED
        print(f"Task '{self.description}' has been completed.")

    ####################### Start OF STR METHOD #############################################################

    # __str__: מייצרת תיאור מובן של המשימה
    def __str__(self):
        return f"Task [ID: {self.task_id}, Description: {self.description}, Status: {self.status.value}]"
