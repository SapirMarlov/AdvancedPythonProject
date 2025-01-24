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

from AdvancedPythonProject.Sql_Con import sql

import pandas as pd
stu_state = State.st1
Students_miki = Students('Miki',1,19,"0526573644" , stu_state, {1:88,2:88},Registered_Status.UNREGISTERED )
Students_ron = Students('Ron', 2, 21, "0526758492", stu_state, {3:92, 1:85}, Registered_Status.REGISTERED)
Students_noa = Students('Noa', 3, 20, "0526583945", stu_state, {1:78, 3:91}, Registered_Status.UNREGISTERED)
Students_avi = Students('Avi', 4, 22, "0526738541", stu_state, {5:95, 2:88}, Registered_Status.REGISTERED)
Students_david = Students('David', 5, 24, "0526789524", stu_state, {1: 91, 7: 84}, Registered_Status.UNREGISTERED)
Students_ronit = Students('Ronit', 6, 25, "0526892345", stu_state, {5: 83, 4: 90}, Registered_Status.REGISTERED)
Students_sara = Students('Sara', 7, 19, "0526958794", stu_state, {4: 75, 5: 89}, Registered_Status.UNREGISTERED)
#student in queue
Students_or_in_queue = Students('Or', 55550, 24, "0527788277", stu_state, {1: 100, 7: 56}, Registered_Status.UNREGISTERED)
Students_ori_in_queue = Students('Ori', 55551, 25, "0523092900", stu_state, {5: 55, 4: 55}, Registered_Status.REGISTERED)
Students_mosh_in_queue = Students('Mosh', 55552, 19, "0522918377", stu_state, {4: 80, 5: 0 , 6:100 }, Registered_Status.REGISTERED)

course_size = 10
course_math = Course('Math' , 1 ,course_size, [Students_avi,Students_miki,Students_noa])
course_bio = Course('Bio' , 2 , course_size,[Students_miki,Students_ron])
course_english = Course('English' , 3 , course_size, [Students_david,Students_sara,Students_ronit,Students_noa])
course_economics = Course('Economics' , 4 , course_size, [Students_ronit,Students_david,Students_avi,Students_miki,Students_noa])
course_law = Course('law' , 5 , course_size, [Students_ron,Students_avi,Students_miki,Students_noa])

queue_math = Queue_wait([Students_or_in_queue,Students_ori_in_queue],id=99990,course_of_queue=course_math)
queue_bio = Queue_wait([Students_mosh_in_queue,Students_ori_in_queue],course_bio,id=99991)
queue_english = Queue_wait([Students_or_in_queue,Students_ori_in_queue,Students_mosh_in_queue.id],course_english,id=99992)
queue_economics = Queue_wait([Students_or_in_queue,Students_ori_in_queue],course_economics,id=99993)
queue_law = Queue_wait([Students_or_in_queue,Students_avi,Students_miki],course_law,id=99994)

teacher_state = State.st5
teacher_ben = Teacher('Ben',41,24,"0524534566",teacher_state,4500,Seniority.MASTER,course_list=[course_bio,course_english],student_list=[Students_noa , Students_miki])
teacher_sara = Teacher('Sara', 42, 32, "0524534568", teacher_state, 5200, Seniority.EXPERT, course_list=[course_math], student_list=[Students_ron, Students_avi])
teacher_lior = Teacher('Lior', 43, 38, "0524534569", teacher_state, 4800, Seniority.SENIOR, course_list=[course_english,course_math], student_list=[Students_ron, Students_miki])
teacher_yaron = Teacher('Yaron', 44, 25, "0524534570", teacher_state, 4600, Seniority.JUNIOR, course_list=[course_economics, course_law], student_list=[Students_noa, Students_avi])

task_clean = Task(99,'clean class',TaskStatus.WAIT)
task_organize = Task(100, 'organize office', TaskStatus.EXECUTION)
task_report = Task(101, 'prepare report', TaskStatus.COMPLETE)
task_train = Task(102, 'conduct training', TaskStatus.WAIT)
task_manage = Task(103, 'manage team', TaskStatus.EXECUTION)
task_prepare = Task(104, 'prepare materials', TaskStatus.COMPLETE)
task_file = Task(105, 'file documents', TaskStatus.WAIT)
task_design = Task(106, 'design presentation', TaskStatus.EXECUTION)
task_research = Task(107, 'research topic', TaskStatus.COMPLETE)
task_present = Task(109, 'present report', TaskStatus.EXECUTION)
task_update = Task(110, 'update database', TaskStatus.COMPLETE)


general_worker_state = State.st2
generalEmployee_don = General_Worker('Don',11,40,"0540022563",general_worker_state,8000, seniority=Seniority.SENIOR , tasks_list=[task_research , task_update]  )
generalEmployee_ron = General_Worker('Ron', 12, 35, "0540022564",general_worker_state, 7500, seniority=Seniority.JUNIOR, tasks_list=[task_present,task_file])
generalEmployee_noa = General_Worker('Noa', 13, 29, "0540022565", general_worker_state, 9000, seniority=Seniority.MASTER, tasks_list=[task_train,task_update])
generalEmployee_avi = General_Worker('Avi', 14, 45, "0540022566", general_worker_state, 8500, seniority=Seniority.SENIOR, tasks_list=[task_clean])
generalEmployee_maya = General_Worker('Maya', 15, 38, "0540022567", general_worker_state, 7700, seniority=Seniority.EXPERT, tasks_list=[task_report,task_train])

manager_state = State.st3
manager_avi = Manager('Avi',21,55,"0501191822",manager_state,16000,Seniority.SENIOR,worker_list=[generalEmployee_avi],teacher_list=[teacher_sara])


payment1 = Payment(12000,3000)
payment2 = Payment(25000,6000)

parent_state = State.st4
Parent_mimi = Parent('Mimi',31,34,"0554256577",parent_state,payment=payment1,childrenList=['emily','moshe'])
Parent_ronit = Parent('Ronit', 40, 42, "0554786543", parent_state,payment=payment2, childrenList=['david', 'sara'])


students_list = pd.DataFrame([Students_noa.__dict__, Students_miki.__dict__, Students_ron.__dict__, Students_avi.__dict__, Students_david.__dict__, Students_ronit.__dict__, Students_sara.__dict__])
courses_list = pd.DataFrame([course_math.__dict__, course_bio.__dict__, course_english.__dict__, course_economics.__dict__, course_law.__dict__])
teachers_list = pd.DataFrame([teacher_ben.__dict__, teacher_sara.__dict__, teacher_lior.__dict__, teacher_yaron.__dict__])
general_workers_list = pd.DataFrame([generalEmployee_don.__dict__, generalEmployee_ron.__dict__, generalEmployee_noa.__dict__, generalEmployee_avi.__dict__, generalEmployee_maya.__dict__])
managers_list = pd.DataFrame([manager_avi.__dict__])
parents_list = pd.DataFrame([Parent_mimi.__dict__, Parent_ronit.__dict__])
queue_wait_list = pd.DataFrame([queue_bio.__dict__, queue_law.__dict__, queue_math.__dict__, queue_english.__dict__,queue_economics.__dict__])




sql_ = sql.sql()
sql_.create_db("university_dataBase_data")
sql_.db_name = "university_dataBase_data"

#חשוב: אסור שיהיה רווח בשם של הטבלאות !!!!!!!!!
dictionary_all = {
    'Course': "_course_id INT AUTO_INCREMENT PRIMARY KEY,_course_size INT,_name VARCHAR(100) NOT NULL,_student_list TEXT",

    'general_worker': "_id INT AUTO_INCREMENT PRIMARY KEY,_name VARCHAR(100) NOT NULL,_age INT NOT NULL,_phone_number VARCHAR(10),_status TEXT ,_salary INT ,_seniority TEXT ,_tasks_list TEXT",

    'Manager': "_id INT AUTO_INCREMENT PRIMARY KEY,_name VARCHAR(100) NOT NULL,_age INT NOT NULL,_phone_number VARCHAR(15),_status TEXT,_salary INT NOT NULL,_seniority TEXT,_worker_list TEXT,_teacher_list TEXT",

    'Parent': "_id INT AUTO_INCREMENT PRIMARY KEY,_name VARCHAR(100) NOT NULL,_age INT NOT NULL,_phone_number VARCHAR(15),_status TEXT,_payment TEXT, _childrenList TEXT",

    'Student': "_id INT AUTO_INCREMENT PRIMARY KEY,_name VARCHAR(100) NOT NULL,_age INT NOT NULL,_phone_number VARCHAR(15),_status TEXT,_grade_course TEXT,_registered TEXT",

    'Teacher': "_id INT AUTO_INCREMENT PRIMARY KEY,_name VARCHAR(100) NOT NULL,_age INT NOT NULL,_phone_number VARCHAR(15),_status TEXT,_salary INT,_seniority TEXT,_course_list TEXT,_student_list TEXT",

    'Wait_Queue': "_id INT AUTO_INCREMENT PRIMARY KEY,_course_of_queue TEXT,_queue TEXT"

}
for key,val in dictionary_all.items():
    sql_.create_table(key, val)


all_df_in_school = [students_list,teachers_list,courses_list,general_workers_list , managers_list , parents_list,queue_wait_list ]
tableName =        ['Student' , 'Teacher', 'Course', 'general_worker' , 'Manager' , 'Parent', 'Wait_Queue']

for i, df_item in enumerate(all_df_in_school):
    table_name = tableName[i]
    sql_.add_df_to_table(table_name, df_item)


student_add_meni = Students('Meni',8,19 , "0524565766",stu_state,{1:88,3:99,5:94},Registered_Status.REGISTERED)
student_add_toni = Students('Toni',9,19, "0524019726",stu_state,{1:70,3:88,5:100},Registered_Status.REGISTERED)
course_add_python = Course('Python',6,course_size,[Students_miki,Students_ron,Students_avi,Students_noa,student_add_toni])
course_add_java = Course('Java',7,course_size,[Students_miki,Students_ron,Students_avi,Students_noa,student_add_toni])

df_students_add = pd.DataFrame([student_add_toni.__dict__, student_add_meni.__dict__])
df_course_add = pd.DataFrame([course_add_python.__dict__, course_add_java.__dict__])


sql_.add_df_to_table(table_name='Student',df_vals=df_students_add)
sql_.add_df_to_table(table_name='Course',df_vals=df_course_add)

sql_.update_col_by_id(table_name='general_worker',col_name_update='_salary',col_name_where='_id',update_val=8898,id=11)
sql_.del_col_by_id(table_name='general_worker',col_name_where='_id',id=15)

