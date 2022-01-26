from red_black_tree import Student, Node, rb_tree
import pandas as pd
import os
import glob

tree = rb_tree()
attendance = []
courses = []
database = {}
current_directory = os.getcwd()
# Collect the file pathways for the attendance sheet and course sheets
get_files = glob.glob(os.path.join(current_directory, "Attendance Sheet", "*.xlsx"))
for x in get_files:
    # file = pd.read_excel(x, dtype={"Attendance Date": str, "Study Groups": str, "Attended": str, "Number of Group Participants": int, "Attended.1": int})
    attendance.append(x)
    
get_files = glob.glob(os.path.join(current_directory, "Course Sheets", "*.xlsx"))
for x in get_files:
    course_info = x.split("_")[1].rsplit(" ", 1)
    database.setdefault(x, course_info)
    courses.append(x)
    
# Begin extracting first name, last name, and student id and putting it into RB tree
for x in courses:
    # Read the file
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

tree.print_tree()
tree.print_specific()
    

        