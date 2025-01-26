from Student import Students, Registered_Status
from Course import Course
from Person import Person, State
from Payment import Payment

class Parent(Person):
    def __init__(self, name, p_id, age, phone_number, status: State,payment:Payment, childrenList: list):
        """
        Initializes a Parent object with the provided attributes.
        :param name: The name of the parent.
        :param id: The ID of the parent.
        :param age: The age of the parent.
        :param phone_number: The phone number of the parent.
        :param status: The status of the parent (must be an instance of State).
        :param childrenList: A list of children (instances of Person).
        """
        super().__init__(name, p_id, age, phone_number, status)
        self.childrenList = childrenList  # Assign the list of children
        self.payment = payment # Assign the payment

    ################################################################################################################################

    # Getter and Setter for childrenList
    @property
    def childrenList(self):
        return self._childrenList

    @childrenList.setter
    def childrenList(self, value):
        """
        Validates that the childrenList is a list and each child is an instance of Person.
        """
        if isinstance(value, list) :
            self._childrenList = value
        else:
            raise ValueError("childrenList must be a list of Person instances.")

    @property
    def payment(self):
        return self._payment

    @payment.setter
    def payment(self, value):
        if not isinstance(value, Payment):
            raise ValueError("Payment must be an instance of Payment class.")
        self._payment = value

    ################################################################################################################################


    def register_child_to_course_if_course_not_full(self,course:Course,courseList,queueList , childName , child_id,age,phone_number,state):
        '''
        Registers a child to a course if the course is not full, or adds them to the waitlist if the course is full.
        :param course:
        :param courseList:
        :param queueList:
        :param childName:
        :param child_id:
        :param age:
        :param phone_number:
        :param state:
        :return:
        '''
        childName = childName.lower()
        student_child = Students(childName , child_id,age,phone_number,state,{},Registered_Status.REGISTERED)
        if childName not in self.childrenList:
            print(f'cant do that , you have not child name {childName}')
            return False
        if course in courseList:
            if len(course.student_list) < course.course_size:
                for course_in_list in courseList:
                    if course == course_in_list:
                        course_in_list.student_list.append(student_child)
                        print(f"Child {childName} has been registered to course {course.name}.")
                        return True
            else:
                for queue in queueList:
                    if course == queue.course:
                        queue.add_student_to_waitlist(student_child)
                        print(f"Child {childName} has been added to waitlist for course {course.name}.")
                        return True
                queueList.append(course)
                queueList[-1].add_student_to_waitlist(student_child)



    def show_child_info(self,childName,course_list):
        childName = childName.lower()
        for course in course_list:
            course_name = course.name
            for student in course.student_list:
                if student.name.lower() == childName:
                    print(f"Child {student.name} is in course {course_name}.")
                    print(student.__str__())
                    return True

    def show_place_in_queue(self,childName ,queueList):
        pass

    def payment_report(self):
        print(self.payment.create_pay_report())

    #################################################################################################################################
    # __str__ method
    def __str__(self):
        base_str = super().__str__()  # Call to the __str__ of the Person class
        children_names = ', '.join([child.name for child in self.childrenList])  # Get the names of all children
        return f"{base_str}, Children: {children_names}"
