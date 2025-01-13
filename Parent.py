from User import User
# מחלקת הורה (Parent) - תורשת מ-User
class Parent(User):
    def __init__(self, name: str, user_id: int, child_name: str):
        super().__init__(name, user_id, role="Parent")
        self.child_name = child_name
        self.registration_status = "Not Registered"

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
