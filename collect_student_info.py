from red_black_tree import Student, Node, rb_tree
import pandas as pd
import os
import glob

tree = rb_tree()
attendance = []
courses = []
database = {}
classCRN = {}

current_directory = os.getcwd()
# Collect the file pathways for the attendance sheet and course sheets
get_files = glob.glob(os.path.join(current_directory, "Attendance Sheet", "*.xlsx"))
for x in get_files:
    attendance.append(x)

get_files = glob.glob(os.path.join(current_directory, "Course Sheets", "*.xlsx"))
# x contains the specific excel file and its pathway
for x in get_files:
    course_info = x.rsplit("\\", 1)[1].rsplit(" ", 1)
    course_info[1] = course_info[1][0:5]
    database.setdefault(x, course_info)
    classCRN.setdefault(course_info[1], course_info[0])
    courses.append(x)
    
# Begin extracting first name, last name, and student id of the course sheets and putting it into RB tree
for x in courses:
    # Reads the file
    file = pd.read_excel(x, dtype={"Student External ID": int, "Student First Name": str, "Student Last Name": str})
    len_row = len(file)
    course_info = database.get(x)
    
    for i in range(0, len_row):
        # Add student in tree if not already there
        if tree.is_empty() == True or tree.find_node(file.iloc[i, 0]) == None:
            tree.insert(file.iloc[i, 0], file.iloc[i, 1], file.iloc[i, 2])
        
        curr_node = tree.find_node(file.iloc[i,0])
        curr_node.student.add_classes(course_info[0])
        curr_node.student.add_crn(course_info[1])

for x in attendance:
    file = pd.read_excel(x, dtype={"Attendance Date": str, "Study Groups": str, "Attended": str, "Number of Group Participants": int, "Attended.1": int})
    len_row = len(file)
    for i in range(0, len_row):
        names = file.iloc[i, 2].split("\n ")
        for j in names:
            if j[0] == " ":
                j = j[1:len(j)]
            name = j.split(", ")
            
            curr_node = tree.find_name(name[1], name[0])
            if curr_node != None:
                curr_node.student.add_attended()
                
            
        
# Both of these code work
tree.print_tree()
# tree.print_specific(first = "Gaston", last = "Vaughan")
    


        