from User import User
# מחלקת מנהל (Admin) - תורשת מ-User
class Manager(User):
    def __init__(self, name: str, user_id: int):
        super().__init__(name, user_id, role="Admin")

    def login(self):
        print(f"Admin {self.name} logged in.")

    def create_user(self):
        print(f"Admin {self.name} is creating a new user.")

    def update_user_info(self):
        print(f"Admin {self.name} is updating user information.")

    def create_course(self):
        print(f"Admin {self.name} is creating a new course.")

    def assign_teacher(self):
        print(f"Admin {self.name} is assigning a teacher to a course.")

    def manage_students(self):
        print(f"Admin {self.name} is managing students.")

    def manage_financial_reports(self):
        print(f"Admin {self.name} is managing financial reports.")

    def generate_reports(self):
        print(f"Admin {self.name} is generating reports.")
