from dataclasses import asdict

from sphinx.cmd.build import make_main
from sqlalchemy import false

from Task import Task ,TaskStatus
from Payment import Payment
from General_Worker import General_Worker
from Teacher import Teacher
from Queue_wait import Queue_wait
from Employee import Employee, Seniority
from Person import State
from Course import Course
from Student import Students , Registered_Status
from Parent import Parent
class Manager(Employee):
    def __init__(self, name, m_id, age, phone_number, status: State, salary, seniority: Seniority, worker_list: list, teacher_list: list):
        """
        Initializes a Manager object with the provided attributes.
        :param name: The name of the manager.
        :param id: The ID of the manager.
        :param age: The age of the manager.
        :param phone_number: The phone number of the manager.
        :param status: The status of the manager (must be an instance of State).
        :param salary: The salary of the manager (must be a positive number).
        :param seniority: The seniority level of the manager (must be an instance of Seniority).
        :param worker_list: A list of workers under the manager.
        :param teacher_list: A list of teachers under the manager.
        """
        super().__init__(name, m_id, age, phone_number, status, salary, seniority)
        self.worker_list = worker_list  # List of workers
        self.teacher_list = teacher_list  # List of teachers

    ################################################################################################################################

    # Getter and Setter for worker_list
    @property
    def worker_list(self):
        return self._worker_list

    @worker_list.setter
    def worker_list(self, value):
        """
        Validates that worker_list is a list.
        """
        if isinstance(value, list):
            self._worker_list = value
        else:
            raise ValueError("worker_list must be a list.")

    ################################################################################################################################

    # Getter and Setter for teacher_list
    @property
    def teacher_list(self):
        return self._teacher_list

    @teacher_list.setter
    def teacher_list(self, value):
        """
        Validates that teacher_list is a list.
        """
        if isinstance(value, list):
            self._teacher_list = value
        else:
            raise ValueError("teacher_list must be a list.")

    ################################################################################################################################

    def create_report_income_outcome(self, year, income, outcome):
        """
        Creates a financial report for a given year.
        :param year: The year for the report.
        :param income: Total income for the year.
        :param outcome: Total outcome (expenses) for the year.
        """
        # checked success
        report = {
                    "year": year,
        "income": income,
        "outcome": outcome,
        "profit": income - outcome,  # רווח = הכנסות - הוצאות
        "net_income": income - outcome,  # הכנסות נטו = הכנסות - הוצאות
        "margin (%)": (income - outcome) / income * 100 if income != 0 else 0,  # שיעור הרווח מתוך הכנסות
        "roi (%)": (income - outcome) / outcome * 100 if outcome != 0 else 0,  # ROI - תשואה על השקעה
        "expense_to_income_ratio (%)": (outcome / income) * 100 if income != 0 else 0  # יחס הוצאות להכנסות
         }

        # עיצוב תצוגת הדוח
        max_key_length = max(len(key) for key in report.keys())
        max_value_length = max(len(str(value)) for value in report.values())
        total_width = max_key_length + max_value_length + 7  # 7 כולל רווחים וסימנים נוספים
        border = "+" + "-" * total_width + "+"

        # הדפסת הדוח
        title = f"Financial Report for {year}"
        print(border)
        print(f"| {title.center(total_width - 2)} |")
        print(border)

        for key, value in report.items():
            print(f"| {key.ljust(max_key_length)} - {str(value).rjust(max_value_length)} |")

        print(border)


    def assign_task_to_general_employee(self, n_general_employee, task):
        """
        Assigns a task to a general employee.
        :param general_employee: The employee to whom the task will be assigned.
        :param task: The task to be assigned.
        """
        # checked success
        if n_general_employee not in self.worker_list:
            raise ValueError(f"{n_general_employee.name} is not in the worker list.")
        if isinstance(n_general_employee,General_Worker):
            if task not in n_general_employee.tasks_list:
                n_general_employee.tasks_list.append(task)
                print(f"Task '{task}' assigned to {n_general_employee.name}.")
                return True
            else:
                print(f"Task '{task}' already exists for {n_general_employee.name}.")
                return False
        else:
            raise ValueError("The provided employee is not a General_Worker.")

    def create_teacher(self, teacher, teacher_list):
        """
        Adds a new teacher to the teacher list.
        :param teacher: The teacher object to be added.
        :param teacher_list: The list of existing teachers.
        """
        # checked success
        if teacher not in teacher_list:
            teacher_list.append(teacher)
            print(f"Teacher {teacher.name} added to the list.")
        else:
            print(f"Teacher {teacher.name} already exists in the list.")

    def create_student(self, student, student_list):
        """
        Adds a new student to the student list.
        :param student: The student object to be added.
        :param student_list: The list of existing students.
        """
        # checked success
        if student not in student_list:
            student_list.append(student)
            print(f"Student {student.name} added to the list.")
        else:
            print(f"Student {student.name} already exists in the list.")

    def create_parent(self, parent, parent_list):
        """
        Adds a new parent to the parent list.
        :param parent: The parent object to be added.
        :param parent_list: The list of existing parents.
        """
        # checked success
        if parent not in parent_list:
            parent_list.append(parent)
            print(f"Parent {parent.name} added to the list.")
        else:
            print(f"Parent {parent.name} already exists in the list.")

    def create_general_employee(self, general_employee, general_employee_list):
        """
        Adds a new general employee to the general employee list.
        :param general_employee: The general employee object to be added.
        :param general_employee_list: The list of existing general employees.
        """
        # checked success
        if general_employee not in general_employee_list:
            general_employee_list.append(general_employee)
            print(f"General employee {general_employee.name} added to the list.")
        else:
            print(f"General employee {general_employee.name} already exists in the list.")

    def create_course(self, course, course_list):
        """
        Adds a new course to the course list.
        :param course: The course object to be added.
        :param course_list: The list of existing courses.
        """
        # checked success
        if course not in course_list:
            course_list.append(course)
            print(f"Course {course.name} added to the list.")
            return True
        else:
            print(f"Course {course.name} already exists in the list.")
            return False

    def assign_teacher_to_course(self, teacher, course):
        """
        Assigns a teacher to a course.
        :param teacher: The teacher object.
        :param course: The course object.
        """
        # קודם כל נוודא שהמורה הוא אובייקט מסוג Teacher
        if not isinstance(teacher, Teacher):
            raise TypeError(f"{teacher} is not a valid teacher object.")
        # נוודא שהקורס הוא אובייקט מסוג Course
        if not isinstance(course, Course):
            raise TypeError(f"{course} is not a valid course object.")
        # נוודא שהמורה ברשימת המורים
        if teacher not in self.teacher_list:
            print(ValueError(f"{teacher.name} is not in the teacher list."))
            return False
        # אם המורה כבר הוקצה לקורס, לא נוסיף אותו שוב
        if course in teacher.course_list:
            print(f"{teacher.name} is already assigned to course {course.name}.")
            return False
        # נוסיף את הקורס לרשימת הקורסים של המורה
        teacher.course_list.append(course)
        print(f"{teacher.name} assigned to course {course.name}.")
        return True


    def manage_queue(self, queue_list):
        """
        Displays and manages the queues of courses.
        :param queue_list: List of queues for courses.
        """
        # checked success
        print(queue_list)
        if (isinstance(queue_list,list)):
            for queues in queue_list:
                if isinstance(queues,Queue_wait):
                    print(f'Queue ID : {queues.id} , for course {queues.course_of_queue.name} , length : {len(queues.queue)}')
                else:
                    print(f'Queue ID : {queues} is not defined')
        else:
            print('queue_list must be a list')

    def add_queue(self, queue,queue_list):
        queue_list.append(queue)
        print(f'Queue with ID {queue.id} added to the list')


    ################################################################################################################################

    # __str__ method
    def __str__(self):
        base_str = super().__str__()  # Call to the __str__ of the Employee class
        workers_str = ', '.join(str(worker) for worker in self.worker_list)  # Convert list of workers to string
        teachers_str = ', '.join(str(teacher) for teacher in self.teacher_list)  # Convert list of teachers to string
        return f"{base_str}, Workers: [{workers_str}], Teachers: [{teachers_str}]"



################################################################################################################################
################################################################################################################################

    def login(self, teacher_list, student_list, course_list, general_worker_list, queue_list, parent_list, task_list):
        while True:
            try:
                print("\n")
                print('='*188)
                print("\n--- * Manager Menu * ---")
                print("1. Create Teacher")
                print("2. Create Student")
                print("3. Create Parent")
                print("4. Create General Employee")
                print("5. Create Course")
                print("6. Assign Teacher to Course")
                print("7. Manage Queues")
                print("8. add queue")
                print("9. Assign Task to General Employee")
                print("!. create a finance report")
                print("0. Exit")
                choice = input("Enter your choice: ")

                #creat teacher
                if choice == '1':
                    print(">>> Creating a new Teacher...")
                    name = input("Enter teacher's name: ")
                    t_id = int(input("Enter teacher's ID: "))
                    age = int(input("Enter teacher's age: "))
                    phone_number = input("Enter teacher's phone number: ")
                    status = State.state_teacher
                    salary = float(input("Enter teacher's salary: "))
                    seniority = 0
                    while seniority not in ['1','2','3','4','5']:
                        seniority = input("Enter teacher's seniority level (junior:1 senior:2 veteran:3 expert:4 Master:5): ")
                    if seniority=='1' :    seniority=Seniority.JUNIOR
                    elif seniority=='2' :  seniority=Seniority.SENIOR
                    elif seniority == '3': seniority = Seniority.VETERAN
                    elif seniority == '4': seniority = Seniority.EXPERT
                    elif seniority == '5': seniority = Seniority.MASTER
                    new_teacher = Teacher(name, t_id, age, phone_number, status, salary, seniority, [], [])
                    self.create_teacher(new_teacher, teacher_list)

                #create student
                elif choice == '2':
                    print(">>> Creating a new Student...")
                    name = input("Enter student's name: ")
                    s_id = int(input("Enter student's ID: "))
                    age = int(input("Enter student's age: "))
                    phone_number = input("Enter student's phone number: ")
                    status = State.state_student
                    new_student = Students(name, s_id, age, phone_number, status, {},Registered_Status.REGISTERED)
                    self.create_student(new_student, student_list)
                    print(student_list)

                #create parent
                elif choice == '3':
                    print("Creating a new Parent...")
                    name = input("Enter parent's name: ")
                    p_id = int(input("Enter parent's ID: "))
                    age = int(input("Enter parent's age: "))
                    phone_number = input("Enter parent's phone number: ")
                    status = State.state_parent
                    child_name = input("Enter your child name with , between : ")
                    child_name = child_name.split(",")
                    income = float(input("Enter your income: "))
                    outcome = float(input("Enter a outcome of the pay:"))
                    payment = Payment(income, outcome)
                    new_parent = Parent(name, p_id, age, phone_number, status,payment,child_name)
                    self.create_parent(new_parent, parent_list)
                    print(parent_list)
                #create general employees
                elif choice == '4':
                    print("Creating a new General Employee...")
                    name = input("Enter general employee's name: ")
                    ge_id = int(input("Enter general employee's ID: "))
                    age = int(input("Enter general employee's age: "))
                    phone_number = input("Enter general employee's phone number: ")
                    status = State.state_general_worker
                    salary = float(input("Enter general employee's salary: "))
                    seniority = 0
                    while seniority not in ['1', '2', '3', '4', '5']:
                        seniority = input(
                            "Enter teacher's seniority level (junior:1 senior:2 veteran:3 expert:4 Master:5): ")
                    if seniority == '1':
                        seniority = Seniority.JUNIOR
                    elif seniority == '2':
                        seniority = Seniority.SENIOR
                    elif seniority == '3':
                        seniority = Seniority.VETERAN
                    elif seniority == '4':
                        seniority = Seniority.EXPERT
                    elif seniority == '5':
                        seniority = Seniority.MASTER
                    new_general_employee = General_Worker(name, ge_id, age, phone_number, status, salary,seniority,[])
                    self.create_general_employee(new_general_employee, general_worker_list)
                #create course
                elif choice == '5':
                    print("Creating a new Course...")
                    name = input("Enter course name: ")
                    c_id = int(input("Enter course ID: "))
                    course_size_ = int(input("Enter course size: "))
                    new_course = Course(name, c_id, course_size_, [])
                    self.create_course(new_course, course_list)
                #assign teacher to new course
                elif choice == '6':
                    print("Assigning a Teacher to a Course...")
                    teacher_name = input("Enter teacher's name: ")
                    teacher = next((t for t in teacher_list if t.name == teacher_name), None)#next->got first object
                    if not teacher:
                        print(f"Teacher {teacher_name} not found in teacher list.")
                        continue
                    course_name = input("Enter course name: ")
                    course = next((c for c in course_list if c.name == course_name), None)
                    if not course:
                        print(f"Course {course_name} not found in course list.")
                        continue
                    self.assign_teacher_to_course(teacher, course)
                #manage queues ok but need first add course and then add queue of course
                elif choice == '7':
                    print("Managing Queues...")
                    self.manage_queue(queue_list)
                #add queue ok
                elif choice == '8':
                    print("add queue...")
                    queue_id = int(input("Enter queue ID: "))
                    course_id = int(input("Enter course ID: "))
                    course = next((c for c in course_list if c.course_id == course_id), None)
                    if not course:
                        print(f"Course with ID {course_id} not found in course list.")
                        continue
                    queue = Queue_wait(id=queue_id, course_of_queue=course,queue=[])
                    self.add_queue(queue,queue_list)
                elif choice == '9':
                    print("Assigning Task to General Employee...")
                    general_employee_id = input("Enter general employee's id: ")
                    general_employee = next((ge for ge in general_worker_list if int(ge.id) == int(general_employee_id)), None)
                    if not general_employee:
                        print(f"General employee {general_employee_id} not found in general employee list.")
                        continue
                    task_id = int(input("Enter task ID : "))
                    task_description = input("Enter task description: ")
                    status = '0'
                    while status not in ['1','2','3']:
                        status = input("Enter task status (wait:1 execution:2 complete:3): ")
                    if status == '1' : status= TaskStatus.WAIT
                    if status == '2': status= TaskStatus.EXECUTION
                    if status == '3': status= TaskStatus.COMPLETE
                    task = Task(task_id, task_description, status)
                    task_list.append(task)
                    general_employee.task_list.append(task)
                elif choice == '!':
                    self.create_report_income_outcome(2025,70000,20000)

                elif choice == '0':
                    print("Exiting Manager Menu...")
                    break

                else:
                    print("Invalid choice. Please try again.")
            except  Exception as e:
                print(f"Error: {e}")
