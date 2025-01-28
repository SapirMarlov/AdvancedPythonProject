from typing import List

from Student import Student
from Teacher import Teacher


# מחלקת קורס (Course)
class Course:
    def __init__(self, name: str ,course_id :int, teacher: Teacher, students: List[Student]):
        self._name = name  # course name
        self._teacher = teacher  # Teacher object
        self._students = students  # list of Student objects
        self.course_id = course_id  # Using setter while creating the object

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


    # getters for courseId
    @property
    def course_id(self):
        return self._courseId

    #setter for courseId
    @course_id.setter
    def course_id(self, course_id: int):
        if not isinstance(course_id, int) or course_id <= 0:
            raise ValueError("Course ID must be a positive integer.")
        self._courseId = course_id

    # ����ר עבו�� courseIdגטר עבור teacher
    @property
    def teacher(self):
        return self._teacher

    # סטר עבור teacher
    @teacher.setter
    def teacher(self, teacher: Teacher):
        if not isinstance(teacher, Teacher):
            raise ValueError("Teacher must be an instance of the Teacher class.")
        self._teacher = teacher

    # גטר עבור students
    @property
    def students(self):
        return self._students

    # סטר עבור students
    @students.setter
    def students(self, students: List[Student]):
        if not all(isinstance(student, Student) for student in students):
            raise ValueError("Each student must be an instance of the Student class.")
        self._students = students

    ####################### END OF GETTERS AND SETTERS #############################################################

    def add_student(self, student: Student):
        self.students.append(student)
        print(f"Student with ID {student.student_id} added to course {self.name}.")

    def check_availability(self):
        print(f"Checking availability for course {self.name}.")

    def manage_registration(self):
        print(f"Managing registration for course {self.name}.")

    def update_course_schedule(self, new_schedule: str):
        print(f"Course {self.name}'s schedule has been updated to {new_schedule}.")

    def cancel_course(self):
        print(f"Course {self.name} has been cancelled.")


################################################################################################################################
    #__str__ method
 # מתודת __str__ שמחזירה תיאור של הקורס
    def __str__(self):
        teacher_name = self.teacher.name if self.teacher else "No teacher assigned"
        student_names = [student.name for student in self.students] if self.students else "No students enrolled"
        return (f"Course [Course ID: {self.course_id} , "
                f"Course Name: {self.name} , "
                f"Teacher: {teacher_name} , "
                f"Enrolled Students: {', '.join(student_names)}]")
