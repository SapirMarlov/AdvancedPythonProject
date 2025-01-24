from abc import ABC, abstractmethod
from enum import Enum


# הגדרת Enum עבור תפקידי משתמש
class UserRole(Enum):
    STUDENT = "Student"
    TEACHER = "Teacher"
    MANAGER = "Manager"
    EMPLOYEE = "Employee"
    PARENT = "Parent"


# מחלקת משתמש (User) - מחלקה אבסטרקטית
class User(ABC):
    def __init__(self, name: str, age: int, user_id: int, role: UserRole):
        # שימוש ב-setters כדי להגדיר את הערכים
        self.name = name
        self.age = age
        self.user_id = user_id
        self.role = role

    ####################### Start OF GETTERS AND SETTERS #############################################################
        # גטר עבור name
    @property
    def name(self):
        return self._name

    # סטר עבור name
    @name.setter
    def name(self, name: str):
        if not isinstance(name, str) or len(name) <= 2:
            raise ValueError("Name must be a string with more than 2 characters.")
        self._name = name

    # גטר עבור age
    @property
    def age(self):
        return self._age

    # סטר עבור age
    @age.setter
    def age(self, age: int):
        if not (18 <= age <= 60):
            raise ValueError("Age must be between 18 and 60.")
        self._age = age

    # גטר עבור user_id
    @property
    def user_id(self):
        return self._user_id

    # סטר עבור user_id
    @user_id.setter
    def user_id(self, user_id: int):
        if not isinstance(user_id, int) or user_id <= 0:
            raise ValueError("User ID must be a positive integer.")
        self._user_id = user_id

    # גטר עבור role
    @property
    def role(self):
        return self._role

    # סטר עבור role
    @role.setter
    def role(self, role: UserRole):
        if not isinstance(role, UserRole):
            raise ValueError("Role must be an instance of the UserRole Enum.")
        self._role = role

    ####################### END OF GETTERS AND SETTERS #############################################################

    # מתודות אבסטרקטיות
    @abstractmethod
    def login(self):
        pass


    ####################### Start OF STR AND EQ METHODS #############################################################

    # __str__: מייצרת תיאור מובן של המשתמש
    def __str__(self):
        return f"User [ID: {self.user_id}, Name: {self.name}, Age: {self.age}, Role: {self.role.value}]"

    # __eq__: משווה שני משתמשים לפי user_id
    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return self.user_id == other.user_id
