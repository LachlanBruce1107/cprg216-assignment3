from studentClass import *
from functions import *

student_list = dict()

fid = open('data.txt','r')
for line in fid:
    list = line.split()
    student_list[list[0]] = (Student(list[0],list[1],list[2],list[3],list[4]))
fid.close()


