from typing import Dict, List

from Employee import Employee, Seniority
from Person import State
from Task import Task

# הגדרת המחלקה General_Worker שמרשת מ-Employee
class General_Worker(Employee):

    def __init__(self, name, g_id, age, phone_number, status: State, salary, seniority: Seniority, tasks_list:List[Task]):
        """
        Initializes a General Worker object with the provided attributes.
        :param name: The name of the worker.
        :param id: The ID of the worker.
        :param age: The age of the worker.
        :param phone_number: The phone number of the worker.
        :param status: The status of the worker (must be an instance of State).
        :param salary: The salary of the worker (must be a positive number).
        :param seniority: The seniority level of the worker (must be an instance of Seniority).
        :param tasks_list: A dictionary where the keys are task names and the values are TaskStatus.
        """
        super().__init__(name, g_id, age, phone_number, status, salary, seniority)
        self.tasks_list = tasks_list  # Dictionary of tasks with task status as values

    ################################################################################################################################

    # Getter and Setter for tasks_list
    @property
    def tasks_list(self):
        return self._tasks_list

    @tasks_list.setter
    def tasks_list(self, value):
        """
        Validates that tasks_list is a dictionary where keys are strings and values are instances of TaskStatus.
        """
        if (isinstance(value, list)):
            self._tasks_list = value
        else:
            raise ValueError(
                "tasks_list must be a dictionary where keys are strings and values are instances of TaskStatus.")

    ################################################################################################################################
    def login(self):
        print('hello , login from general worker')
        pass
    def change_task_status_of_task(self,task, new_task_status):
        if task not in self._tasks_list:
            print(f"Task '{task}' does not exist in the tasks list.")
            return False
        for task_ in self._tasks_list:
            if task_ == task:
                print(f' --- task.description : {task_.description} --- ')
                print(f'before change : {task_.status}')
                task_.status=new_task_status
                print(f'after change : {task_.status}')
                return True

        print(f"Task '{task}' not found.")
        return False
    def problem_report(self):
        pass
    ################################################################################################################################

    # __str__ method
    def __str__(self):
        base_str = super().__str__()  # Call to the __str__ of the Employee class
        return f"{base_str}, Tasks: [{self.tasks_list.__str__()}]"

    # this method is for getting the tasks