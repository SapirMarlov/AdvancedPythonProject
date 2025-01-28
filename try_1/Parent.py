from User import User, UserRole
from enum import Enum

# הגדרת Enum עבור סטטוס הרישום
class RegistrationStatus(Enum):
    NOT_REGISTERED = "Not Registered"
    REGISTERED = "Registered"

# מחלקת הורה (Parent) - תורשת מ-User
class Parent(User):
    def __init__(self, name: str,age:int, user_id: int, child_name: str, child_id: int):
        super().__init__(name, age, user_id=user_id, role=UserRole.PARENT)
        self._child_name = child_name
        self._child_id = child_id
        self._registration_status = RegistrationStatus.NOT_REGISTERED

    ####################### Start OF GETTERS AND SETTERS #############################################################

    # גטר עבור child_name
    @property
    def child_name(self):
        return self._child_name

    # סטר עבור child_name
    @child_name.setter
    def child_name(self, child_name: str):
        if not isinstance(child_name, str) or len(child_name) <= 2:
            raise ValueError("Child name must be a string with more than 2 characters.")
        self._child_name = child_name

    # גטר עבור child_id
    @property
    def child_id(self):
        return self._child_id

    # סטר עבור child_id
    @child_id.setter
    def child_id(self, child_id: int):
        if not isinstance(child_id, int) or child_id <= 0:
            raise ValueError("Child ID must be a positive integer.")
        self._child_id = child_id

    # גטר עבור registration_status
    @property
    def registration_status(self):
        return self._registration_status

    # סטר עבור registration_status
    @registration_status.setter
    def registration_status(self, registration_status: RegistrationStatus):
        if not isinstance(registration_status, RegistrationStatus):
            raise ValueError("Registration status must be an instance of the RegistrationStatus Enum.")
        self._registration_status = registration_status

    ####################### END OF GETTERS AND SETTERS #############################################################

    def login(self):
        print(f"Parent {self.name} logged in.")

    def create_user(self):
        print(f"Parent {self.name} is creating a new user.")

    def update_user_info(self):
        print(f"Parent {self.name} is updating user information.")

    def register_child_for_course(self, course: str):
        print(f"Parent {self.name} is registering {self.child_name} for the {course} course.")

    def track_child_progress(self):
        print(f"Parent {self.name} is tracking {self.child_name}'s progress.")

    def manage_payments(self):
        print(f"Parent {self.name} is managing payments.")

    def view_report_cards(self):
        print(f"Parent {self.name} is viewing {self.child_name}'s report card.")

    ####################### Start OF STR METHOD #############################################################

    # __str__: מייצרת תיאור מובן של ההורה
    def __str__(self):
        user_str = super().__str__()  # פונה ל-__str__ של User
        return f"Parent [ {user_str}, Child: {self.child_name} (ID: {self.child_id}), Registration Status: {self.registration_status.value} ]"
