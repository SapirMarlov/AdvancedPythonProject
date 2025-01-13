from Course import Course
from Student import Student
# מחלקת תור (Waitlist)
class WaitQueue:
    def __init__(self, course: Course):
        self.course = course
        self.students_in_waitlist = []

    def add_student_to_waitlist(self, student: Student):
        self.students_in_waitlist.append(student)
        print(f"Student {student.name} added to waitlist for {self.course.name}.")

    def update_waitlist_position(self, student: Student):
        position = self.students_in_waitlist.index(student) + 1
        print(f"Student {student.name} is in position {position} on the waitlist.")

    def notify_waitlisted_students(self):
        print(f"Notifying waitlisted students for course {self.course.name}.")

    def remove_student_from_waitlist(self, student: Student):
        self.students_in_waitlist.remove(student)
        print(f"Student {student.name} has been removed from the waitlist.")
