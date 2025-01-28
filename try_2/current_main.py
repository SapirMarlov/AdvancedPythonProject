
from Course import Course
from Student import Students,Registered_Status
from Teacher import Teacher
from Parent import Parent
from General_Worker import General_Worker
from Task import Task , TaskStatus
from Manager import Manager
from Payment import Payment
from Employee import Employee, Seniority
from Queue_wait import Queue_wait

from Person import Person , State

from AdvancedPythonProject.Sql_Con.sql import sql
import pandas as pd


sql_ = sql()
class system():
    def __init__(self):
        self.students = []
        self.teachers = []
        self.parents = []
        self.general_workers = []
        self.courses = []
        self.queues = []
        self.managers = []
        self.tasks = []
        self.payments = []
        self.employees = []
        self.sql = sql()
        self.Manager_avi = Manager('Avi',3141592,55,"0524738477",State.state_manager,250000,Seniority.MASTER,[],[])

    def login(self):
        while True:
            print("\n")
            print('=' * 188)
            print("Welcome to the Academy Management System!")
            print("Please choose your login option:")
            print("1. Login as Manager")
            print("2. Login as Student")
            print("3. Login as Teacher")
            print("4. Login as Parent")
            print("5. Login as General Employee")
            print("0. Exit")
            choice = input("Enter your choice: ")

            # Manager login
            if choice == '1':
                self.Manager_avi.login(self.teachers,self.students,self.courses,self.general_workers,self.queues,self.parents,self.tasks)
                #did 1-3 in login function of manager and check it word
            # Student login
            elif choice == '2':
                # Placeholder for student login functionality
                pass

            # Teacher login
            elif choice == '3':
                # Placeholder for teacher login functionality
                pass

            # Parent login
            elif choice == '4':
                # Placeholder for parent login functionality
                pass

            # General Employee login
            elif choice == '5':
                # Placeholder for general employee login functionality
                pass

            # Exit
            elif choice == '0':
                print("Thank you for using the Academy Management System. Goodbye!")
                print('updated...')
                self.__str__()
                #here , need to call to function add_data_to_sql method
                break

            # Invalid choice
            else:
                print("Invalid choice. Please try again.")
    def __str__(self):
        st=''
        # הדפסת סטודנטים
        print(f'Students ({len(self.students)}):')
        for student in self.students:
            print(student.__str__())
        print('='*180)
        # הדפסת מורים
        print(f'Teachers ({len(self.teachers)}):')
        for teacher in self.teachers:
            print(teacher.__str__())
        print('=' * 180)
        # הדפסת הורים
        print(f'Parents ({len(self.parents)}):')
        for parent in self.parents:
            print(parent.__str__())
        print('=' * 180)
        # הדפסת עובדים כלליים
        print(f'General Workers ({len(self.general_workers)}):')
        for worker in self.general_workers:
            print(worker.__str__())
        print('=' * 180)
        # הדפסת קורסים
        print(f'Courses ({len(self.courses)}):')
        for course in self.courses:
            print(course.__str__())
        print('=' * 180)
        # הדפסת תורים
        print(f'Queues ({len(self.queues)}):')
        for queue in self.queues:
            print(queue.__str__())
        print('=' * 180)
        # הדפסת מנהלים
        print(f'Managers ({len(self.managers)}):')
        for manager in self.managers:
            print(manager.__str__())
        print('=' * 180)
        # הדפסת משימות
        print(f'Tasks ({len(self.tasks)}):')
        for task in self.tasks:
            print(task.__str__())
        print('=' * 180)
        # הדפסת תשלומים
        print(f'Payments ({len(self.payments)}):')
        for payment in self.payments:
            print(payment.__str__())
        print('=' * 180)
        # הדפסת עובדים
        print(f'Employees ({len(self.employees)}):')
        for employee in self.employees:
            print(employee.__str__())
        print('=' * 180)
    def add_data_to_sql(self,new_dataFrame_table_name, current_df_of_table_name):
        #i think not need the parameter because its gone after then user finished
        #so will enter the dataFrames

        df_students = pd.DataFrame([student.__dict__ for student in self.students])
        df_courses = pd.DataFrame([course.__dict__ for course in self.courses])
        df_teachers = pd.DataFrame([teacher.__dict__ for teacher in self.teachers])
        df_general_employees = pd.DataFrame([worker.__dict__ for worker in self.general_workers])
        df_managers = pd.DataFrame([manager.__dict__ for manager in self.managers])
        df_parents = pd.DataFrame([parent.__dict__ for parent in self.parents])
        df_queues = pd.DataFrame([queue.__dict__ for queue in self.queues])

        # חשוב: אסור שיהיה רווח בשם של הטבלאות !!!!!!!!!
        dictionary_all = {
            'Course': "_course_id INT AUTO_INCREMENT PRIMARY KEY,_course_size INT,_name VARCHAR(100) NOT NULL,_student_list TEXT",

            'general_worker': "_id INT AUTO_INCREMENT PRIMARY KEY,_name VARCHAR(100) NOT NULL,_age INT NOT NULL,_phone_number VARCHAR(10),_status TEXT ,_salary INT ,_seniority TEXT ,_tasks_list TEXT",

            'Manager': "_id INT AUTO_INCREMENT PRIMARY KEY,_name VARCHAR(100) NOT NULL,_age INT NOT NULL,_phone_number VARCHAR(15),_status TEXT,_salary INT NOT NULL,_seniority TEXT,_worker_list TEXT,_teacher_list TEXT",

            'Parent': "_id INT AUTO_INCREMENT PRIMARY KEY,_name VARCHAR(100) NOT NULL,_age INT NOT NULL,_phone_number VARCHAR(15),_status TEXT,_payment TEXT, _childrenList TEXT",

            'Student': "_id INT AUTO_INCREMENT PRIMARY KEY,_name VARCHAR(100) NOT NULL,_age INT NOT NULL,_phone_number VARCHAR(15),_status TEXT,_grade_course TEXT,_registered TEXT",

            'Teacher': "_id INT AUTO_INCREMENT PRIMARY KEY,_name VARCHAR(100) NOT NULL,_age INT NOT NULL,_phone_number VARCHAR(15),_status TEXT,_salary INT,_seniority TEXT,_course_list TEXT,_student_list TEXT",

            'Wait_Queue': "_id INT AUTO_INCREMENT PRIMARY KEY,_course_of_queue TEXT,_queue TEXT"

        }
        for key, val in dictionary_all.items():
            sql_.create_table(key, val)

        all_df_in_school = [df_students, df_teachers, df_courses, df_general_employees, df_managers, df_parents,
                            df_queues]
        tableName = ['Student', 'Teacher', 'Course', 'general_worker', 'Manager', 'Parent', 'Wait_Queue']

        for i, df_item in enumerate(all_df_in_school):
            table_name = tableName[i]
            sql_.add_df_to_table(table_name, df_item)
        sql_.add_df_to_table(new_dataFrame_table_name, current_df_of_table_name)


def main():
    system_school=system()
    system_school.login()
main()
