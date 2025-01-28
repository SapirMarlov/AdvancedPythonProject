from typing import Dict
from Course import Course
from Person import Person, State
from enum import Enum

class Registered_Status(Enum):
    REGISTERED = "registered"
    UNREGISTERED = "unregistered"

class Students(Person):
    def __init__(self, name, s_id, age, phone_number, status: State, grade_course: Dict[int, int], registered: Registered_Status):
        """
        Initializes a Student object with the provided attributes.
        :param name: The name of the student.
        :param id: The ID of the student.
        :param age: The age of the student.
        :param phone_number: The phone number of the student.
        :param status: The status of the student (must be an instance of State).
        :param grade_course: A dictionary mapping courses to grades.
        :param registered: The registration status of the student (must be an instance of Registered_Status).
        """
        super().__init__(name, s_id, age, phone_number, status)
        self.grade_course = grade_course  # Dictionary of courses and corresponding grades
        self.registered = registered  # Registered status

    ################################################################################################################################

    # Getter and Setter for grade_course
    @property
    def grade_course(self):
        return self._grade_course

    @grade_course.setter
    def grade_course(self, value):
        """
        Validates that grade_course is a dictionary where the keys are instances of Course
        and the values are integers or floats (grades).
        """
        if isinstance(value, dict) and all(isinstance(course_id, int) and isinstance(grade, (int, float)) for course_id, grade in value.items()):
            self._grade_course = value
        else:
            raise ValueError("grade_course must be a dictionary where the keys are instances of Course and the values are numbers (int or float).")

    ################################################################################################################################

    # Getter and Setter for registered
    @property
    def registered(self):
        return self._registered

    @registered.setter
    def registered(self, value):
        """
        Validates that registered is an instance of Registered_Status.
        """
        if isinstance(value, Registered_Status):
            self._registered = value
        else:
            raise ValueError("registered must be an instance of Registered_Status.")

    ################################################################################################################################
    def login(self):
        print('hello , login from student')
        pass

    def show_grade(self,list_courses):
        #print(f'grade of {self.name} [course_id,grade] - {self._grade_course.__str__()}')
        for key,val in self._grade_course.items():
            for course in list_courses:
                if course._course_id == key:
                    print(f'Student {self.name} grade in course {course.name} is {val}')
        return self.grade_course
    def show_place_in_queue(self,queueList):
        mon = 0
        for queue_ in queueList:
            for stu in queue_.queue:
                try:
                    if stu.name == self.name:
                        print(f"Student {self.name} is at position {queue_.queue.index(stu) + 1} found in queue of {queue_.course_of_queue.name}")
                        mon+=1

                except Exception as e:
                    #print(f"Error in show_place_in_queue: {e}")
                    continue
        if mon==0:
            print(f"Student {self.name} not found in queue of {queue_.course_of_queue.name}")
            return False
        else:
            return True



    ################################################################################################################################

    # __str__ method
    def __str__(self):
        base_str = super().__str__()  # Call to the __str__ of the Person class
        grade_course_str = ', '.join(f"{course}: {grade}" for course, grade in self.grade_course.items())  # Format course and grade pairs
        return f"{base_str}, Courses and Grades: [{grade_course_str}], Registration Status: {self.registered.value}"

