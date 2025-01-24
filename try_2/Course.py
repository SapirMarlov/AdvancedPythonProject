class Course:
    def __init__(self, name: str, course_id: int, student_list: list):
        """
        Initializes a Course object with the provided attributes.
        :param name: The name of the course.
        :param course_id: The unique ID of the course.
        :param student_list: A list of students enrolled in the course.
        """
        self.name = name
        self.course_id = course_id
        self.student_list = student_list  # List of students enrolled in the course

    ################################################################################################################################

    # Getter and Setter for name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 2:
            self._name = value
        else:
            raise ValueError("Course name must be a string with more than 2 characters.")

    ################################################################################################################################

    # Getter and Setter for course_id
    @property
    def course_id(self):
        return self._course_id

    @course_id.setter
    def course_id(self, value):
        if isinstance(value, int) and value > 0:
            self._course_id = value
        else:
            raise ValueError("Course ID must be a positive integer.")

    ################################################################################################################################

    # Getter and Setter for student_list
    @property
    def student_list(self):
        return self._student_list

    @student_list.setter
    def student_list(self, value):
        if isinstance(value, list):
            self._student_list = value
        else:
            raise ValueError("Student list must be a list.")

    ################################################################################################################################

    # __str__ method
    def __str__(self):
        student_names = ', '.join([student.name for student in self.student_list])  # Assuming student objects have a 'name' attribute
        return f"Course(Name: {self.name}, ID: {self.course_id}, Students: {student_names})"
