from Student import Student
from Teacher import Teacher

students = []
teachers = []

def addstudent():
    name = input("Student Name:")
    surname = input("Student Surname:")
    studentid= input("Student ID:")
    student = Student(name,surname,studentid)
    students.append(student)
   

def addteacher():
    name = input("Teacher Name:")
    surname = input("Teacher Surname:")
    profession = input("Teacher Profession:")
    teacher = Teacher(name,surname,profession)
    teachers.append(teacher)
    

def printstudents():
    for student in students:
        print("Student List:\n",student)

def printteachers():
    for teacher in teachers:
        print("Teacher List:\n",teacher)


while True:
    
    print("1- Add new student\n2- Add new teacher\n3- Show student list\n4- Show teacher list\nQ- Quit")
    
    choice = input("Choose(1/2/3/4/q):")
    
    if  choice == "q":
        break
    elif choice == "1":
        addstudent()
         print("New student was added!")
    elif choice == "2":
        addteacher()
        print("New teacher was added!")
    elif choice == "3":
        printstudents()
    elif choice == "4":
        printteachers()
    else:
        print("PLease enter a valid key")
        continue
