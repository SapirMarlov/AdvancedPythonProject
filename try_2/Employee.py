from Person import Person, State
from enum import Enum


class Seniority(Enum):
    JUNIOR = "junior"
    SENIOR = "senior"
    VETERAN = "veteran"
    EXPERT = "expert"
    MASTER = "master"


class Employee(Person):
    def __init__(self, name, e_id, age, phone_number, status: State, salary, seniority: Seniority):
        """
        Initializes an Employee object with the provided attributes.
        :param name: The name of the employee.
        :param id: The ID of the employee.
        :param age: The age of the employee.
        :param phone_number: The phone number of the employee.
        :param status: The status of the employee (must be an instance of State).
        :param salary: The salary of the employee (must be a positive number).
        :param seniority: The seniority level of the employee (instance of Seniority Enum).
        """
        super().__init__(name, e_id, age, phone_number, status)
        self._salary = salary
        self._seniority = seniority

    ################################################################################################################################

    # Getter and Setter for salary
    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        """
        Validates and sets the salary. It must be a positive number.
        """
        if isinstance(value, (int, float)) and value > 0:
            self._salary = value
        else:
            raise ValueError("Salary must be a positive number.")

    ################################################################################################################################

    # Getter and Setter for seniority
    @property
    def seniority(self):
        return self._seniority

    @seniority.setter
    def seniority(self, value):
        """
        Validates and sets the seniority. It must be an instance of Seniority Enum.
        """
        if isinstance(value, Seniority):
            self._seniority = value
        else:
            raise ValueError("Seniority must be an instance of Seniority Enum.")

    ################################################################################################################################

    # __str__ method
    def __str__(self):
        base_str = super().__str__()  # Call to the __str__ of the Person class
        return f"{base_str}, Salary: {self.salary}, Seniority: {self.seniority.value}"
