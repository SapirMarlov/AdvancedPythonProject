from Employee import Employee, Seniority
from Person import State

class Manager(Employee):
    def __init__(self, name, m_id, age, phone_number, status: State, salary, seniority: Seniority, worker_list: list, teacher_list: list):
        """
        Initializes a Manager object with the provided attributes.
        :param name: The name of the manager.
        :param id: The ID of the manager.
        :param age: The age of the manager.
        :param phone_number: The phone number of the manager.
        :param status: The status of the manager (must be an instance of State).
        :param salary: The salary of the manager (must be a positive number).
        :param seniority: The seniority level of the manager (must be an instance of Seniority).
        :param worker_list: A list of workers under the manager.
        :param teacher_list: A list of teachers under the manager.
        """
        super().__init__(name, m_id, age, phone_number, status, salary, seniority)
        self.worker_list = worker_list  # List of workers
        self.teacher_list = teacher_list  # List of teachers

    ################################################################################################################################

    # Getter and Setter for worker_list
    @property
    def worker_list(self):
        return self._worker_list

    @worker_list.setter
    def worker_list(self, value):
        """
        Validates that worker_list is a list.
        """
        if isinstance(value, list):
            self._worker_list = value
        else:
            raise ValueError("worker_list must be a list.")

    ################################################################################################################################

    # Getter and Setter for teacher_list
    @property
    def teacher_list(self):
        return self._teacher_list

    @teacher_list.setter
    def teacher_list(self, value):
        """
        Validates that teacher_list is a list.
        """
        if isinstance(value, list):
            self._teacher_list = value
        else:
            raise ValueError("teacher_list must be a list.")

    ################################################################################################################################

    # __str__ method
    def __str__(self):
        base_str = super().__str__()  # Call to the __str__ of the Employee class
        workers_str = ', '.join(str(worker) for worker in self.worker_list)  # Convert list of workers to string
        teachers_str = ', '.join(str(teacher) for teacher in self.teacher_list)  # Convert list of teachers to string
        return f"{base_str}, Workers: [{workers_str}], Teachers: [{teachers_str}]"

