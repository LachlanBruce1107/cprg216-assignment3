from student_class import *
from functions import *

student_list = dict()

fid = open('data.txt','r')
for line in fid:
    list = line.split()
    student_list[list[0]] = (Student(list[0],list[1],list[2],list[3],list[4]))
fid.close()

print('Welcome to the Students Enrollment system')
choice = 'y'
while choice == 'y' or choice == 'yes':
    option = show_menu()
    match option:
        case 1:
            run_add(student_list)
        case 2:
            run_search(student_list)
        case 3:
            run_edit(student_list)
        case 4:
            run_remove(student_list)
        case 5:
            print_list(student_list)
        case 6:
            save_data(student_list)
    
    choice = input("Would you like to continue(y/yes), or exit the program(n/no)? \n")

