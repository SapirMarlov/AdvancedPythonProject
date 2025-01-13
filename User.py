from abc import ABC, abstractmethod

# מחלקת משתמש (User) - מחלקה אבסטרקטית
class User(ABC):
    def __init__(self, name: str, user_id: int, role: str):
        self.name = name
        self.user_id = user_id
        self.role = role

    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def create_user(self):
        pass

    @abstractmethod
    def update_user_info(self):
        pass
