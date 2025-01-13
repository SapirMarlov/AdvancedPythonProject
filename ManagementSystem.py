from Manager import Manager
from Parent import Parent
from Student import Student
from Teacher import Teacher
from Employee import Employee
from Course import Course
from WaitQueue import WaitQueue
from Task import Task

# מחלקת מערכת ניהול (ManagementSystem)
class ManagementSystem:
    def __init__(self):
        self.users = []
        self.courses = []
        self.tasks = []


