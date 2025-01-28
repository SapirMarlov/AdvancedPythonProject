from Employee import Employee, Seniority
from Person import State

class Teacher(Employee):
    def __init__(self, name, t_id, age, phone_number, status: State, salary, seniority: Seniority, course_list: list, student_list: list):
        """
        Initializes a Teacher object with the provided attributes.
        :param name: The name of the teacher.
        :param id: The ID of the teacher.
        :param age: The age of the teacher.
        :param phone_number: The phone number of the teacher.
        :param status: The status of the teacher (must be an instance of State).
        :param salary: The salary of the teacher (must be a positive number).
        :param seniority: The seniority level of the teacher (must be an instance of Seniority).
        :param course_list: A list of courses taught by the teacher.
        :param student_list: A list of students taught by the teacher.
        """
        super().__init__(name, t_id, age, phone_number, status, salary, seniority)
        self.course_list = course_list  # List of courses
        self.student_list = student_list  # List of students

    ################################################################################################################################

    # Getter and Setter for course_list
    @property
    def course_list(self):
        return self._course_list

    @course_list.setter
    def course_list(self, value):
        """
        Validates that course_list is a list of strings (course names).
        """
        if isinstance(value, list) :
            self._course_list = value
        else:
            raise ValueError("course_list must be a list of strings (course names).")

    ################################################################################################################################

    # Getter and Setter for student_list
    @property
    def student_list(self):
        return self._student_list

    @student_list.setter
    def student_list(self, value):
        """
        Validates that student_list is a list.
        """
        if isinstance(value, list):
            self._student_list = value
        else:
            raise ValueError("student_list must be a list.")

    ################################################################################################################################
    def login(self):
        pass
    def show_student_in_course(self):
        for i in self._student_list:
            print(i.__str__())
        pass
    def assign_student_to_course(self,student):
        if student not in self._student_list:
            self._student_list.append(student)
            print(f"Student {student.name} assigned to courses of teacher {self.name}")
        else:
            print(f"Student {student.name} already assigned to courses of teacher {self.name}")

    def assign_grade_to_student(self,student,grade,course):
        if student not in self._student_list:
            print(f"Student {student.name} not found in the list of students assigned to teacher {self.name}")
            return False
        elif course not in self._course_list:
            print(f"Course {course} not found in the list of courses assigned to teacher {self.name}")
            return False
        else:
            if course not in self._course_list:
                student.grade_course[course.course_id] = grade
            else:
                student.grade_course[course.course_id]=[student.grade_course[course.course_id],grade]
            print(f"Grade {grade} assigned to student {student.name} in course {course.name}")
            return True
    def problem_report(self):
        pass
    ################################################################################################################################

    # __str__ method

    # __str__ method
    def __str__(self):
        base_str = super().__str__()  # Call to the __str__ of the Employee class
        return f'{base_str} , {self.course_list.__str__()} , {self.student_list.__str__()}'