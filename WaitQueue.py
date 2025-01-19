from typing import List
from Course import Course
from Student import Student

# מחלקת תור (Waitlist)
class WaitQueue:
    def __init__(self, course: Course, student_in_list: List[Student] ):
        self.course = course
        self.students_in_waitlist = student_in_list if student_in_list else []

    ####################### Start OF GETTERS AND SETTERS #############################################################

    # גטר עבור course
    @property
    def course(self):
        return self._course

    # סטר עבור course
    @course.setter
    def course(self, course: Course):
        if not isinstance(course, Course):
            raise ValueError("Course must be an instance of Course.")
        self._course = course

    # גטר עבור students_in_waitlist
    @property
    def students_in_waitlist(self):
        return self._students_in_waitlist

    # סטר עבור students_in_waitlist
    @students_in_waitlist.setter
    def students_in_waitlist(self, students_in_waitlist: List[Student]):
        if not all(isinstance(student, Student) for student in students_in_waitlist):
            raise ValueError("Each student must be an instance of Student.")
        self._students_in_waitlist = students_in_waitlist

    ####################### END OF GETTERS AND SETTERS #############################################################

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

    ####################### Start OF STR METHOD #############################################################

    # __str__: מייצרת תיאור מובן של התור, כולל פרטי הקורס ורשימת הסטודנטים
    def __str__(self):
        students_str = ", ".join([student.name for student in self.students_in_waitlist]) if self.students_in_waitlist else "No students in waitlist"
        return f"WaitQueue [Course: {self.course.name}, Students in waitlist: {students_str}]"
