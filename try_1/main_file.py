from ManagementSystem import ManagementSystem
from Student import Student
from Course import Course
from WaitQueue import WaitQueue
from Employee import Employee
from Manager import Manager
from Parent import Parent
from Task import Task ,TaskStatus
from Teacher import Teacher

from AdvancedPythonProject.Sql_Con.sql import sql

import pandas as pd

def main():
    systemMenegement = ManagementSystem()
    #list for objects
    student_list = []
    teacher_list = []
    manager_list = []
    parent_list = []
    course_list = []
    task_list = []
    wait_queue_list = []
    employee_list = []

    # יצירת אובייקטים של סטודנטים
    Student_Mor = Student(name="Mor Levi",age=20 ,user_id=1, schedule=["Mathematics", "Physics"], grades={1: 85, 2: 90})
    Student_Oren = Student(name="Oren Cohen",age=22, user_id=2, schedule=["Chemistry", "Biology"], grades={3: 88, 4: 91})
    Student_Adi = Student(name="Adi Katz",age=26, user_id=3, schedule=["Computer Science", "Mathematics"], grades={5: 92, 1: 89})
    Student_Tal = Student(name="Tal Mizrahi",age=34, user_id=4, schedule=["Physics", "Biology"], grades={2: 84, 4: 93})
    Student_Roni = Student(name="Roni Bar",age=19, user_id=5, schedule=["Computer Science", "Chemistry"], grades={5: 95, 3: 87})

    # יצירת אובייקטים של מורים (Teacher)
    Teacher_Smith = Teacher(name="Smith", age=25, user_id=12, courses=[1], students=[Student_Adi , Student_Mor])
    Teacher_Brown = Teacher(name="Brown", age=31, user_id=13, courses=[2, 4], students=[Student_Tal , Student_Tal, Student_Roni])
    Teacher_Bonn = Teacher(name="Bonn", age=27, user_id=14, courses=[3, 5], students=[Student_Adi,Student_Oren,Student_Roni,Student_Tal])

    # יצירת אובייקטים של קורסים עם idים בין 1 ל-5
    Course_Math = Course(course_id=1, name="Mathematics", teacher=Teacher_Smith, students=[Student_Mor , Student_Tal , Student_Adi])
    Course_Physics = Course(course_id=2, name="Physics", teacher=Teacher_Smith, students=[Student_Oren , Student_Roni , Student_Adi , Student_Tal])
    Course_Chemistry = Course(course_id=3, name="Chemistry", teacher=Teacher_Brown, students=[Student_Adi,Student_Mor,Student_Roni])
    Course_Biology = Course(course_id=4, name="Biology", teacher=Teacher_Bonn, students=[Student_Mor,Student_Adi,Student_Tal,Student_Roni])
    Course_ComputerScience = Course(course_id=5, name="Computer Science", teacher=Teacher_Bonn, students=[Student_Adi,Student_Tal,Student_Roni,Student_Mor])

    # יצירת אובייקטים של WaitQueue עבור כל קורס
    WaitQueue_Math = WaitQueue(course=Course_Math , student_in_list=[Student_Adi])
    WaitQueue_Physics = WaitQueue(course=Course_Physics , student_in_list=[Student_Tal])
    WaitQueue_Chemistry = WaitQueue(course=Course_Chemistry, student_in_list=[Student_Mor])
    WaitQueue_Biology = WaitQueue(course=Course_Biology, student_in_list=[Student_Oren])
    WaitQueue_ComputerScience = WaitQueue(course=Course_ComputerScience, student_in_list=[])

    # יצירת אובייקטים של משימות (Task)
    Task_Task1 = Task(task_id=1, description="Prepare classrooms for Passover cleaning",status=TaskStatus.NOT_COMPLETED)
    Task_Task2 = Task(task_id=2, description="Check cleaning supplies for Passover", status=TaskStatus.IN_PROGRESS)
    Task_Task3 = Task(task_id=3, description="Schedule classroom cleaning before Passover",status=TaskStatus.NOT_COMPLETED)
    Task_Task4 = Task(task_id=4, description="Ensure all classrooms are cleaned after Passover",status=TaskStatus.NOT_COMPLETED)
    Task_Task5 = Task(task_id=5, description="Organize materials for Passover holiday", status=TaskStatus.COMPLETED)

    # יצירת אובייקטים של עובדים (Employee)
    Employee_Jack = Employee(name="Jack Taylor",age=44, user_id=6, tasks=[Task_Task1 , Task_Task5])
    Employee_Maya = Employee(name="Maya Davis",age=34, user_id=7, tasks=[Task_Task2])

    # יצירת אובייקטים של מנהלים (Manager)
    Manager_John = Manager(name="John Wilson",age=55, user_id=8, task_for_employee=[Task_Task1 , Task_Task2 , Task_Task3 , Task_Task4 , Task_Task5] , income=50000 , outcome=13400)


    # יצירת אובייקטים של הורים (Parent)
    Parent_Alice = Parent(name="Alice Johnson",age=45, user_id=10, child_name="Mor Levi", child_id=1)
    Parent_Bob = Parent(name="Bob Lee",age=40, user_id=11, child_name="Oren Cohen", child_id=2)


    # הדפסת כל האובייקטים

    print(Student_Mor.__str__())
    print(Student_Oren.__str__())
    print(Student_Adi.__str__())
    print(Student_Tal.__str__())
    print(Student_Roni.__str__())

    print("="*180)
    print(Course_Math.__str__())
    print(Course_Physics.__str__())
    print(Course_Chemistry.__str__())
    print(Course_Biology.__str__())
    print(Course_ComputerScience.__str__())

    print("=" * 180)
    print(WaitQueue_Math.__str__())
    print(WaitQueue_Physics.__str__())
    print(WaitQueue_Chemistry.__str__())
    print(WaitQueue_Biology.__str__())
    print(WaitQueue_ComputerScience.__str__())

    print("=" * 180)
    print(Task_Task1.__str__())
    print(Task_Task2.__str__())
    print(Task_Task3.__str__())
    print(Task_Task4.__str__())
    print(Task_Task5.__str__())

    print("=" * 180)
    print(Employee_Jack.__str__())
    print(Employee_Maya.__str__())

    print("=" * 180)
    print(Manager_John.__str__())

    print(Parent_Alice.__str__())
    print(Parent_Bob.__str__())

    print(Teacher_Smith.__str__())
    print(Teacher_Brown.__str__())
    sql_ = sql()
    sql_.create_db("university_db")
    sql_.db_name = "university_db"
    dictionary_all = {
        'Course': "_courseId INT AUTO_INCREMENT PRIMARY KEY,_name VARCHAR(100) NOT NULL,_teacher VARCHAR(2000) NOT NULL,_students VARCHAR(2000)",

        'Employee': "_user_id INT AUTO_INCREMENT PRIMARY KEY,_name VARCHAR(100) NOT NULL,_age INT NOT NULL,_role TEXT NOT NULL,_tasks TEXT",

        'Manager': "_user_id INT AUTO_INCREMENT PRIMARY KEY,_name VARCHAR(100) NOT NULL,_age INT NOT NULL,_role TEXT NOT NULL,_task_for_employee VARCHAR(2222),_income INT NOT NULL,_outcome INT NOT NULL",

        'Parent': "_user_id INT AUTO_INCREMENT PRIMARY KEY,_name VARCHAR(100) NOT NULL,_age INT NOT NULL,_role TEXT NOT NULL,_child_name VARCHAR(100) NOT NULL,_child_id INT NOT NULL,_registration_status TEXT ",

        'Student': "_user_id INT AUTO_INCREMENT PRIMARY KEY,_name VARCHAR(100) NOT NULL,_age INT NOT NULL,_role TEXT ,_schedule TEXT,_grades TEXT",

        'Teacher': "_user_id INT AUTO_INCREMENT PRIMARY KEY,_name VARCHAR(100) NOT NULL,_age INT NOT NULL,_role TEXT NOT NULL,_courses TEXT,_students TEXT",

        'Task': "_task_id INT AUTO_INCREMENT PRIMARY KEY,_description VARCHAR(255) NOT NULL,_status VARCHAR(50) DEFAULT 'NOT_COMPLETED'",

        'WaitQueue': "_course VARCHAR(200), _students_in_waitlist VARCHAR(200), PRIMARY KEY (_course, _students_in_waitlist)"
    }
    for key,val in dictionary_all.items():
        sql_.create_table(key, val)


    # הוספה של אובייקטים לרשימות המתאימות כמילון
    # סטודנטים
    student_list.append(Student_Mor.__dict__)
    student_list.append(Student_Oren.__dict__)
    student_list.append(Student_Adi.__dict__)
    student_list.append(Student_Tal.__dict__)
    student_list.append(Student_Roni.__dict__)

    # מורים
    teacher_list.append(Teacher_Smith.__dict__)
    teacher_list.append(Teacher_Brown.__dict__)
    teacher_list.append(Teacher_Bonn.__dict__)

    # קורסים
    course_list.append(Course_Math.__dict__)
    course_list.append(Course_Physics.__dict__)
    course_list.append(Course_Chemistry.__dict__)
    course_list.append(Course_Biology.__dict__)
    course_list.append(Course_ComputerScience.__dict__)

    # תורי המתנה
    wait_queue_list.append(WaitQueue_Math.__dict__)
    wait_queue_list.append(WaitQueue_Physics.__dict__)
    wait_queue_list.append(WaitQueue_Chemistry.__dict__)
    wait_queue_list.append(WaitQueue_Biology.__dict__)
    wait_queue_list.append(WaitQueue_ComputerScience.__dict__)

    # משימות
    task_list.append(Task_Task1.__dict__)
    task_list.append(Task_Task2.__dict__)
    task_list.append(Task_Task3.__dict__)
    task_list.append(Task_Task4.__dict__)
    task_list.append(Task_Task5.__dict__)

    # עובדים
    employee_list.append(Employee_Jack.__dict__)
    employee_list.append(Employee_Maya.__dict__)

    # מנהלים
    manager_list.append(Manager_John.__dict__)

    # הורים
    parent_list.append(Parent_Alice.__dict__)
    parent_list.append(Parent_Bob.__dict__)

    df_student = pd.DataFrame(student_list)
    df_teacher = pd.DataFrame(teacher_list)
    df_course = pd.DataFrame(course_list)
    df_wait_queue = pd.DataFrame(wait_queue_list)
    df_task = pd.DataFrame(task_list)
    df_employee = pd.DataFrame(employee_list)
    df_manager = pd.DataFrame(manager_list)
    df_parent = pd.DataFrame(parent_list)

    all_df_in_school = [df_student,df_teacher,df_course,df_wait_queue,df_task,df_employee,df_manager,df_parent]
    tableName =        ['Student' , 'Teacher', 'Course', 'WaitQueue', 'Task', 'Employee', 'Manager', 'Parent']
    #sql_.add_df_to_table('Student', df_student)

    for i,df_item in enumerate(all_df_in_school):
        table_name = tableName[i]
        sql_.add_df_to_table(table_name, df_item)


    print(df_wait_queue.columns)





if __name__ == "__main__":
    main()
