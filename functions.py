from studentClass import *

def show_menu():
    print("What would you like to do today?")
    print("-Add a student? enter 1")
    print("-Search for student? enter 2")
    print("-Edit student info? enter 3")
    print("-Remove a student? enter 4")
    print("-Print the student list? enter 5")
    print("-Save the data to a file? enter 6")
    return int(input())

def add(students,id,first_name,last_name,gpa,semester):
    students[id] = Student(id,first_name,last_name,gpa,semester)

def remove(students,id):
    students.pop(id)

def edit_name(students,id,new_name):
    pass

def search(students, id):
    pass

def run_search(students):
    pass

def run_edit(students):
    pass
    
def same_name(students,first_name,last_name):
    for student in students:
        if first_name == students[student].get_first_name() and last_name == students[student].get_last_name():
            return True
    return False

def run_add(students):
    choice = "y"
    while choice == "y" or choice == "yes":
        print("Enter id of the student, followed by the student's information.")
        id = input("Id:\n")
        first_name = input("First name:\n")
        last_name = input("Last name:\n")
        gpa = input("GPA:\n")
        semester = input("Semester:\n")
        if same_name(students,first_name,last_name):
            print("The student already enrolled. No action is required.")
        elif id in students:
            print("Incorrect Id. Id already exist in the system.")
        else:
            add(students,id,first_name,last_name,gpa,semester)
            print("Student Enrolled in the system")
            print(id,first_name,last_name,gpa,semester,)
        choice = input("Do you want to add a new student?y(yes)/n(no)\n").lower()


def run_remove(students):
    choice = "y"
    while choice == "y" or choice == "yes":
        print("Enter id of the student that you want to remove from the students' registry.")
        id = input("id:\n")
        if id in students:
            remove(students, id)
            print("Student removed")
        else:
            print("No student found")
        choice = input("Do you want to remove more students?y(yes)/n(no)\n").lower()

def printList(students):
    for student in students:
        print(students[student].get_all_attributes())

def saveData(students):
    fid = open('data.txt','w')
    for student in students:
        fid.write(students[student].get_all_attributes())
        fid.write('\n')
    fid.close
